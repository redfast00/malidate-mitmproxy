from . import utils
from . import http_parser

class GenericAttack(object):
    def response(self, flow):
        request = flow.request
        if utils.inscope(request.host):
            self.attack(request)
    
    def generate_hostname(self, tcp_content):
        parsed = http_parser.HTTPRequest(tcp_content)
        attack_name = self.get_attackname()
        return utils.generate_hostname(parsed.url, parsed.method, attack_name)
    
    def tcp_message(self, flow):
        message = flow.messages[-1]
        host = flow.server_conn.address.host
        if message.from_client and utils.inscope(host):
            self.attack(message, host)

    @classmethod
    def get_attackname(cls):
        return cls.__name__
    
    def attack(self, flow, hostname):
        print("Override this, hostname was " + hostname)

class ReplaceHostAttack(GenericAttack):
    def attack(self, message, host):
        new_hostname = self.generate_hostname(message.content).encode('utf-8')
        message.content = message.content.replace(host.encode('utf-8'), new_hostname)
        
class OverrideHostAttack(GenericAttack):
    def attack(self, message, host):
        parsed = http_parser.HTTPRequest(message.content)
        path = parsed.path
        new_path = r'http://' + self.generate_hostname(self, tcp_content)
        message.content = message.content.replace(path, new_path, 1)

attacks = [ReplaceHostAttack, OverrideHostAttack]
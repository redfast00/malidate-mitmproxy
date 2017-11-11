import utils


class GenericAttack(object):
    def response(self, flow):
        request = flow.request
        if utils.inscope(request.host):
            self.attack(request)
    
    def generate_hostname(self, request):
        # Get name of class
        attack = self.__class__.__name__
        return utils.generate_hostname(request.url, request.method, attack)

    def attack(self, request):
        print("Override this")

class ReplaceHostAttack(GenericAttack):
    def attack(self, request):
        print("here")
        request.host = self.generate_hostname(request)
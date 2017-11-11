import fnmatch
import random
import string
import requests

from .config import config
from . import database


def inscope(domain):
    for pattern in config["outscope"]:
        if fnmatch.fnmatch(domain, pattern):
            return False
    for pattern in config["inscope"]:
        if fnmatch.fnmatch(domain, pattern):
            return True
    return False # By default, domains are out of scope

def generate_hostname(url, method, attack):
    # Generate random subdomain
    subdomain = config["secret_prefix"] + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
    full_domain = subdomain + '.' + config['domain']
    database.insert_interaction(url, method, attack, full_domain, get_public_ip())
    return full_domain


def get_public_ip():
    if 'public_ip' not in config:
        t = requests.get('http://eth0.me')
        config['public_ip'] = t.text.strip()
    return config['public_ip']


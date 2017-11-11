"""Module for interacting both with our local database and with
    the remote database (malidate server.
"""

import dataset
import requests
import time
from .config import config

_db = dataset.connect(config["database"])
_clientside = _db["clientside"]

def insert_interaction(url, method, attack, domain_used, own_ip):
    timestamp = time.time()
    _clientside.insert(dict(url=url, method=method, attack=attack,
                            domain_used=domain_used, timestamp=timestamp, own_ip=own_ip))

def get_server_interactions(prefix, verify=None):
    # Only set verify to False when testing!
    r = requests.get('https://export.{}/{}'.format(config['domain'], prefix), verify=verify)
    return r.json()

def search_client_interaction(domainname):
    return _clientside.find_one(domain_used=domainname)
    

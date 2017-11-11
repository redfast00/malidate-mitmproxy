"""Module for interacting both with our local database and with
    the remote database (malidate server.
"""

import dataset
import requests
import time
from .config import config

_db = dataset.connect(config["database"])
_clientside = _db["clientside"]

def insert_interaction(url, method, attack, domain_used):
    timestamp = time.time()
    _clientside.insert(dict(url=url, method=method, attack=attack,
                            domain_used=domain_used, timestamp=timestamp))

    

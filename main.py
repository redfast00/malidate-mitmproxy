from mitmproxy import http
import json
import sys
import argparse

from malidate.attacks import attacks

# Generate list of attacks
attackdict = {attack.get_attackname(): attack for attack in attacks}
list_of_attacks = list(attackdict.keys())

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--attack", dest='attack', choices=list_of_attacks, required=True)
args = parser.parse_args()

def start():
    return attackdict[args.attack]()


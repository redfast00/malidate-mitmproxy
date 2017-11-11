#!/usr/bin/env python3
import dataset
from malidate.database import get_server_interactions, search_client_interaction
from malidate.config import config

server_interactions = get_server_interactions(config["secret_prefix"])
# TODO: use argparse

show_DNS = True
show_same_IP = False
def print_client_data(data, interactiontype):
    print("{method} {url} using {attack} -> {type}".format(
        method=data["method"],
        url=data["url"],
        attack=data["attack"],
        type=interactiontype
    ))

for interaction in server_interactions:
    client_data = search_client_interaction(interaction["name"])
    interactiontype = interaction["type"]
    if interactiontype == "DNS" and not show_DNS:
        continue
    if interaction["ip"] == client_data["own_ip"] and not show_same_IP:
        continue
    print_client_data(client_data, interactiontype)
    
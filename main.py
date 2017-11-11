from mitmproxy import http
import json
import sys
import argparse

from malidate.attacks import ReplaceHostAttack


def start():
    return ReplaceHostAttack()

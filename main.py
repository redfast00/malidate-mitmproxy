from mitmproxy import http
import json
import sys
import argparse

from utils import inscope
from attacks import ReplaceHostAttack



def start():
    return ReplaceHostAttack()

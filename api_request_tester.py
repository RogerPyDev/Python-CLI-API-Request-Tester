import requests
import subprocess
import sys

def test_api(endpoint, method="GET", data=None):
    
    try:
        if method.upper() == "GET":
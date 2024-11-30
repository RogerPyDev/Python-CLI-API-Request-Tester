import requests
import subprocess
import sys

def test_api(endpoint, method="GET", data=None):

    try:
        if method.upper() == "GET":
            response = requests.get(endpoint)
        elif method.upper() == "POST":
            response = requests.post(endpoint, json=data)
        else:
            print(f"Método {method} no soportado.")
            return None, None

        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión: {e}")
        return None, None

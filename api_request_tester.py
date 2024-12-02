import requests
import subprocess
import sys


def test_api(endpoint, method="GET", data=None):

    """
    Envía una solicitud HTTP a un endpoint específico.

    Parámetros:
    - endpoint: URL del API a probar.
    - method: Método HTTP a usar (GET, POST, etc.).
    - data: Datos para enviar en el cuerpo de la solicitud (opcional).

    Retorna:
    - status_code: Código de respuesta HTTP.
    - response_text: Texto de la respuesta.
    """

    try:

        #  Selecciona el m{etodo HTTP}

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


def run_external_test_tool(command):

    try:
        result = subprocess.run(command, shell=True, text=True, shell=True)
        print(f"Resultado del comando '{command}':\n{result.stdout}")
    except Exception as e:
        print(f"Error al ejecutar el comando externo: {e}")


def main():
    print("Bienvenido al Api Request Tester")
    print("1. Probar un endpoint API")
    print("2. Ejecutar una herramienta externa para pruebas")
    print("3. Salir")
    
    while True:
        choice = input("\nSelecciona una opción: ")
        
        if choice == "1":
            
            endpoint = input("Ingresa el URL del endpoint: ")
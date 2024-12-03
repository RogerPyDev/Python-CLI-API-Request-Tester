import requests  # Para interactuar con APIs REST
import subprocess  # Para ejecutar herramientas externas
import sys  # Para manejar argumentos de línea de comandos


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

        #  Selecciona el método HTTP}

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

    """
    Ejecuta una herramienta de prueba externa y muestra el resultado.

    Parámetros:
    - command: Comando de la herramienta externa a ejecutar.
    """

    try:
        result = subprocess.run(command, shell=True, text=True)
        print(f"Resultado del comando '{command}':\n{result.stdout}")
    except Exception as e:
        print(f"Error al ejecutar el comando externo: {e}")


def main():

    # Programa principal para interactuar con el usuario desde la consola.

    print("Bienvenido al Api Request Tester")
    print("1. Probar un endpoint API")
    print("2. Ejecutar una herramienta externa para pruebas")
    print("3. Salir")

    while True:
        choice = input("\nSelecciona una opción: ")

        if choice == "1":

            # Prueba de endpoint API

            endpoint = input("Ingresa el URL del endpoint: ")
            method = input("Ingresa el método HTTP (GET/POST): ").upper()
            if method == "POST":
                data = input("Ingresa los datos en formato JSON (Opcional): ")
                try:
                    data = eval(data) if data.strip() else None  # Convierte string a diccionario
                except Exception:
                    print("Formato JSON inválido.")
                    data = None

            # Llamada a la función para probar el endpoint
            status_code, response_text = test_api(endpoint, method, data)
            if status_code:
                print("\nRespuesta del API:")
                print(f"\nStatus Code: {status_code}")
                print(f"Code:\n{response_text}")
            else:
                print("No se puedo obtener una respuesta del API.")

        elif choice == "2":

            # Ejecución de herramienta externa

            command = input("Ingresa el comando de la herramienta externa: ")
            run_external_test_tool(command)

        elif choice == "3":

            # Salir del programa

            print("¡Gracias por usar el API Request Tester!")
            sys.exit()

        else:
            print("Opción no válida. Inténtalo de nuevo")


if __name__ == "__main__":
    main()

# Python-CLI-API-Request-Tester
CLI para probar APIs REST, desarrollado en Python. Permite enviar solicitudes HTTP (`GET` y `POST`), incluir datos JSON, y ejecutar herramientas externas desde la consola. Ideal para desarrolladores que buscan validar endpoints de forma rápida y eficiente.

# API Request Tester CLI

Una herramienta interactiva basada en la línea de comandos, desarrollada en Python, para probar APIs REST y ejecutar herramientas externas para pruebas adicionales. Ideal para desarrolladores que deseen validar rápidamente endpoints y automatizar tareas básicas relacionadas con APIs.

## **Características**
- Envío de solicitudes HTTP (`GET` y `POST`) a endpoints REST.
- Admite datos JSON para solicitudes `POST`.
- Integración con herramientas externas mediante la ejecución de comandos CLI.
- Fácil de usar, con una interfaz interactiva desde la consola.

## **Requisitos**
- Python 3.7 o superior.
- Bibliotecas adicionales: 
  - [`requests`](https://pypi.org/project/requests/)

## **Instalación**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/RogerPyDev/Python-CLI-API-Request-Tester
   cd api-request-tester-cli
   ```
2. Instala las dependencias:
   ```bash
   pip install requests
   ```

## **Uso**
Ejecuta el programa desde la terminal con el siguiente comando:
```bash
python api_request_tester.py
```

### **Opciones Disponibles**
1. **Probar un Endpoint API**  
   - Ingresa el URL del endpoint.
   - Selecciona el método HTTP (`GET` o `POST`).
   - (Opcional) Proporciona datos JSON para solicitudes `POST`.

2. **Ejecutar una Herramienta Externa**  
   - Ingresa un comando CLI (por ejemplo, `curl`).

3. **Salir**  
   - Finaliza la aplicación.

## **Ejemplo de Uso**

### **Probar un Endpoint API**
#### GET Request:
```plaintext
Ingresa el URL del endpoint: https://jsonplaceholder.typicode.com/posts/1
Ingresa el método HTTP (GET/POST): GET
```
**Salida esperada:**
```plaintext
Respuesta del API:
Status Code: 200
Contenido: {
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

#### POST Request:
```plaintext
Ingresa el URL del endpoint: https://jsonplaceholder.typicode.com/posts
Ingresa el método HTTP (GET/POST): POST
Ingresa los datos en formato JSON (opcional): {"title": "foo", "body": "bar", "userId": 1}
```
**Salida esperada:**
```plaintext
Respuesta del API:
Status Code: 201
Contenido: {
  "id": 101
}
```

### **Ejecutar Herramienta Externa**
```plaintext
Ingresa el comando de la herramienta externa: curl -I https://jsonplaceholder.typicode.com/posts/1
```
**Salida esperada:**
```plaintext
Resultado del comando 'curl -I https://jsonplaceholder.typicode.com/posts/1':
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 292
```

## **Posibles Ampliaciones Futuras**
- Soporte para métodos HTTP adicionales como `PUT` y `DELETE`.
- Manejo avanzado de encabezados personalizados (Headers).
- Validación y almacenamiento temporal de logs de solicitudes.
- Integración con autenticación basada en tokens.


## **Licencia**
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más información.

---

## 🙌 **Agradecimientos**
Este proyecto fue diseñado como parte de un aprendizaje práctico de Python. ¡Espero que te sea útil para gestionar tus sesiones de trabajo!

---

## 📧 **Contacto**
Creador: [Tu Nombre](https://github.com/RogerPyDev)   
GitHub: [Tu Usuario](https://github.com/RogerPyDev)

---

### ¡Apoya mi trabajo!
Si estos proyectos CLI te son útiles y quieres contribuir a su desarrollo continuo, considera apoyarme:  
- ❤️ [Conviértete en mi sponsor en GitHub](https://github.com/sponsors/RogerPyDev)  

Tu apoyo me ayuda a seguir creando herramientas profesionales y compartirlas con la comunidad. ¡Gracias por hacerlo posible! 🙌

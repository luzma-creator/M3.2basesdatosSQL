import requests

# Definir la URL base de MockAPI
url_base = "https://66b4e59f9f9169621ea4c557.mockapi.io/contactos"

# Especificar el ID del registro que deseas obtener
id_registro = 3  # Cambia este número por el ID del registro que necesitas

# Crear la URL completa para acceder al registro específico
url = f"{url_base}/{id_registro}"

# Realizar la solicitud GET a la API para obtener el registro
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta JSON en un diccionario de Python
    registro = response.json()

    # Mostrar todos los campos del registro en formato plano
    for campo, valor in registro.items():
        print(f"{campo}: {valor}")
else:
    print(f"Error al obtener los datos: {response.status_code}")
    if response.status_code == 404:
        print("El recurso no fue encontrado. Verifica la URL y el ID del registro.")
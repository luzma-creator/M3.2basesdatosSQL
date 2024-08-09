import requests

# Definir la URL base de MockAPI
url = "https://66b4e59f9f9169621ea4c557.mockapi.io/contactos"

# Crear el nuevo registro que deseas agregar (dicionario de Python)
nuevo_registro = {
    "nombre": "Luz",
    "pais": "Mexico",
    "estado": "Hidalgo",
    "ciudad": "pachuca"
}

# Realizar la solicitud POST a la API para agregar el nuevo registro
response = requests.post(url, json=nuevo_registro)

# Comprobar si la solicitud fue exitosa
if response.status_code == 201:
    # Mostrar la respuesta del servidor (el nuevo registro creado)
    registro_creado = response.json()
    print("Registro creado exitosamente:")
    for campo, valor in registro_creado.items():
        print(f"{campo}: {valor}")
else:
    print(f"Error al crear el registro: {response.status_code}")
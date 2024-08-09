import requests

# Definir la URL base de MockAPI
url_base = "https://66b4e59f9f9169621ea4c557.mockapi.io/contactos"

# Especificar el ID del registro que deseas modificar
id_registro = 1  # Cambia este número por el ID del registro que necesitas modificar

# Crear la URL completa para acceder al registro específico
url = f"{url_base}/{id_registro}"

# Datos actualizados para el registro
registro_actualizado = {
    "nombre": "Luz",
    "pais": "Mexico",
    "estado": "Hidalgo",
    "ciudad": "pachuca"
}

# Realizar la solicitud PUT a la API para modificar el registro
response = requests.put(url, json=registro_actualizado)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Mostrar la respuesta del servidor (el registro modificado)
    registro_modificado = response.json()
    print("Registro modificado exitosamente:")
    for campo, valor in registro_modificado.items():
        print(f"{campo}: {valor}")
else:
    print(f"Error al modificar el registro: {response.status_code}")
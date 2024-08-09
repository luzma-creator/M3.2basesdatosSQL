import requests

# Definir la URL base de MockAPI
url_base = "https://66b4e59f9f9169621ea4c557.mockapi.io/contactos"

# Especificar el ID del registro que deseas eliminar
id_registro = 1  # Cambia este número por el ID del registro que necesitas eliminar

# Crear la URL completa para acceder al registro específico
url = f"{url_base}/{id_registro}"

# Realizar la solicitud DELETE a la API para eliminar el registro
response = requests.delete(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    print(f"Registro con ID {id_registro} eliminado exitosamente.")
elif response.status_code == 404:
    print(f"Registro con ID {id_registro} no encontrado.")
else:
    print(f"Error al eliminar el registro: {response.status_code}")
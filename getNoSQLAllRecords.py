import requests
import pandas as pd
import json

# Paso 1: Realizar la solicitud GET a la API
url = "https://66b4e59f9f9169621ea4c557.mockapi.io/contactos"
response = requests.get(url)

# Paso 2: Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Paso 3: Obtener los datos en formato JSON
    datos_json = response.json()

    # Paso 4: Mostrar los datos JSON formateados
    print("Datos en formato JSON (formateado):")
    print(json.dumps(datos_json, indent=4))

    # Paso 5: Convertir los datos a un DataFrame de pandas
    df = pd.DataFrame(datos_json)
    print("\nDatos en formato DataFrame:")
    print(df)

    # Paso 6: Exportar los datos a un archivo CSV
    df.to_csv("contactos.csv", index=False)
    print("\nLos datos se han exportado a 'contactos.csv' correctamente.")
else:
    # Paso 7: Manejar errores según el código de estado
    print(f"Error al realizar la solicitud: {response.status_code}")
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# Conecta a MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Cambia la URL si es necesario
db = client["Actividad"]
collection = db["Base"]

# Obtén los datos de MongoDB y conviértelos en un DataFrame
datos = list(collection.find())
df = pd.DataFrame(datos)

# Convierte las columnas LATITUD y LONGITUD a tipo numérico
df['LATITUD'] = pd.to_numeric(df['LATITUD'], errors='coerce')
df['LONGITUD'] = pd.to_numeric(df['LONGITUD'], errors='coerce')

# Elimina filas con valores NaN en LATITUD y LONGITUD
df = df.dropna(subset=['LATITUD', 'LONGITUD'])

# Grafica los datos
plt.figure(figsize=(10, 8))
plt.scatter(df['LONGITUD'], df['LATITUD'], c='blue', marker='o')
plt.title('Ubicación de los escenarios deportivos')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()

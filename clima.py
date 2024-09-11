import argparse
import requests
import json
import os

# Leer y guardar caché
def leer_cache():
    if os.path.exists('cache.json'):
        with open('cache.json', 'r') as f:
            return json.load(f)
    return {}

def guardar_cache(cache):
    with open('cache.json', 'w') as f:
        json.dump(cache, f)

# Obtener clima desde la API y manejar caché
def obtener_clima(ciudad, pais):
    cache = leer_cache()
    clave = f"{ciudad},{pais}"
    
    if clave in cache:
        print(f"Usando datos en caché para {ciudad}, {pais}")
        return cache[clave]
    else:
        api_key = "bb97ffe9de79eec8bf7b6a071f9e3039"  # Sustituye con tu clave de API
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}&units=metric&lang=es"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                cache[clave] = data
                guardar_cache(cache)
                return data
            else:
                print(f"No se encontró la ubicación: {ciudad}, {pais}.")
                return None
        except Exception as e:
            print(f"Error al obtener el clima: {e}")
            return None

# Mostrar datos climáticos de manera clara
def mostrar_clima(datos, formato):
    if formato == "json":
        print(json.dumps(datos, indent=4))
    elif formato == "csv":
        print(f"Ciudad,País,Temperatura,Clima")
        print(f"{datos['name']},{datos['sys']['country']},{datos['main']['temp']}°C,{datos['weather'][0]['description']}")
    else:
        print(f"Clima en {datos['name']}, {datos['sys']['country']}:")
        print(f"Temperatura: {datos['main']['temp']}°C")
        print(f"Condiciones: {datos['weather'][0]['description']}")

# Función principal
def main():
    parser = argparse.ArgumentParser(description="Aplicación CLI para obtener el clima de una ciudad")
    parser.add_argument("ciudad", type=str, help="Nombre de la ciudad")
    parser.add_argument("pais", type=str, help="Nombre del país")
    parser.add_argument("--formato", choices=["json", "csv", "texto"], default="texto", help="Formato de salida (json, csv, texto)")
    
    args = parser.parse_args()
    
    datos = obtener_clima(args.ciudad, args.pais)
    
    if datos:
        mostrar_clima(datos, args.formato)

if __name__ == "__main__":
    main()

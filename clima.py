import argparse
import requests
import json
import os

def leer_cache():
    if os.path.exists('cache.json'):
        with open('cache.json', 'r') as f:
            return json.load(f)
    return {}

def guardar_cache(cache):
    with open('cache.json', 'w') as f:
        json.dump(cache, f)

def obtener_clima(ciudad, pais):
    cache = leer_cache()
    clave = f"{ciudad},{pais}"
    
    if clave in cache:
        print(f"Usando datos en caché para {ciudad}, {pais}")
        return cache[clave]
    else:
        api_key = "bb97ffe9de79eec8bf7b6a071f9e3039"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            cache[clave] = data
            guardar_cache(cache)
            return data
        else:
            print(f"No se encontró la ubicación: {ciudad}, {pais}")
            return None

def main():
    parser = argparse.ArgumentParser(description="Aplicación CLI para obtener el clima de una ciudad")
    parser.add_argument("ciudad", type=str, help="Nombre de la ciudad")
    parser.add_argument("pais", type=str, help="Nombre del país")
    
    args = parser.parse_args()
    datos = obtener_clima(args.ciudad, args.pais)
    if datos:
        print(f"Clima en {args.ciudad}, {args.pais}: {datos['main']['temp']}°C")

if __name__ == "__main__":
    main()

import argparse
import requests

# Definir la función que obtiene el clima de la API
def obtener_clima(ciudad, pais):
    api_key = "bb97ffe9de79eec8bf7b6a071f9e3039"  # Sustituye con tu clave de la API de OpenWeather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            print(f"Clima en {ciudad}, {pais}:")
            print(f"Temperatura: {data['main']['temp']}°C")
            print(f"Condiciones: {data['weather'][0]['description']}")
        else:
            print(f"No se encontró la ubicación: {ciudad}, {pais}.")
    except Exception as e:
        print(f"Error al obtener el clima: {e}")

# Definir la función principal de la CLI
def main():
    parser = argparse.ArgumentParser(description="Aplicación CLI para obtener el clima de una ciudad")
    parser.add_argument("ciudad", type=str, help="Nombre de la ciudad")
    parser.add_argument("pais", type=str, help="Nombre del país")
    
    args = parser.parse_args()
    
    obtener_clima(args.ciudad, args.pais)

if __name__ == "__main__":
    main()

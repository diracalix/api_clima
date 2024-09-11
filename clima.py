import argparse
import requests

def obtener_clima(ciudad, pais):
    api_key = "bb97ffe9de79eec8bf7b6a071f9e3039"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print(f"Clima en {ciudad}, {pais}: {data['main']['temp']}°C")
    else:
        print(f"No se encontró la ubicación: {ciudad}, {pais}")

def main():
    parser = argparse.ArgumentParser(description="Aplicación CLI para obtener el clima de una ciudad")
    parser.add_argument("ciudad", type=str, help="Nombre de la ciudad")
    parser.add_argument("pais", type=str, help="Nombre del país")
    
    args = parser.parse_args()
    obtener_clima(args.ciudad, args.pais)

if __name__ == "__main__":
    main()

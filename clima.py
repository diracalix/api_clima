import argparse

def main():
    parser = argparse.ArgumentParser(description="Aplicación CLI para obtener el clima de una ciudad")
    parser.add_argument("ciudad", type=str, help="Nombre de la ciudad")
    parser.add_argument("pais", type=str, help="Nombre del país")
    
    args = parser.parse_args()
    print(f"Ciudad: {args.ciudad}, País: {args.pais}")

if __name__ == "__main__":
    main()

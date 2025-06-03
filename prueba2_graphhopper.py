import requests

# Token generado en laboratorio para GraphHopper
API_KEY = "b858bd52-ee52-4899-a310-8b74cba6dd41"
BASE_URL = "https://graphhopper.com/api/1/route"

# Diccionario con coordenadas conocidas para las ciudades
# (Se utilizan coordenadas aproximadas para Santiago y Ovalle)
coordenadas = {
    "Santiago": {"lat": -33.4489, "lon": -70.6693},
    "Ovalle": {"lat": -30.5983, "lon": -71.2009}
}

def convertir_tiempo(ms):
    """Convierte milisegundos a horas, minutos y segundos."""
    segundos_totales = ms / 1000
    horas = int(segundos_totales // 3600)
    minutos = int((segundos_totales % 3600) // 60)
    segundos = segundos_totales % 60
    return horas, minutos, segundos

def main():
    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen (o 'q' para salir): ")
        if ciudad_origen.lower() == 'q':
            break
        ciudad_destino = input("Ingrese la Ciudad de Destino (o 'q' para salir): ")
        if ciudad_destino.lower() == 'q':
            break
        
        # Verificamos si las ciudades ingresadas tienen coordenadas definidas
        if ciudad_origen in coordenadas and ciudad_destino in coordenadas:
            punto_origen = coordenadas[ciudad_origen]
            punto_destino = coordenadas[ciudad_destino]
        else:
            print("Una o ambas ciudades no están definidas. Utilice 'Santiago' u 'Ovalle'.")
            continue
        
        # Construir la URL para la solicitud a GraphHopper
        url = f"{BASE_URL}?key={API_KEY}"
        url += f"&point={punto_origen['lat']},{punto_origen['lon']}"
        url += f"&point={punto_destino['lat']},{punto_destino['lon']}"
        url += "&vehicle=car&locale=es&calc_points=false"

        response = requests.get(url)
        data = response.json()
        
        try:
            ruta = data['paths'][0]
            distancia_km = ruta.get('distance', 0) / 1000  # Conversión: metros a kilómetros
            tiempo_ms = ruta.get('time', 0)               # Tiempo en milisegundos
            horas, minutos, segundos = convertir_tiempo(tiempo_ms)
            # Consumo de combustible: Ejemplo de 0.08 litros por km
            combustible = distancia_km * 0.08
            
            # Mostrar resultados formateados
            print(f"\nDistancia: {distancia_km:.2f} km")
            print(f"Duración del viaje: {horas:02d}h {minutos:02d}m {segundos:05.2f}s")
            print(f"Combustible requerido: {combustible:.2f} litros")
            print("\nNarrativa del viaje:")
            print(f"El viaje desde {ciudad_origen} hasta {ciudad_destino} abarca {distancia_km:.2f} km, "
                  f"lo que se traducirá en un tiempo estimado de {horas} horas, {minutos} minutos y {segundos:.2f} segundos. "
                  f"Se requerirán aproximadamente {combustible:.2f} litros de combustible.\n")
        except (KeyError, IndexError):
            print("Error al procesar la respuesta. Verifica las ciudades ingresadas y tu conexión.")

if __name__ == '__main__':
    main()

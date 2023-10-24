import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'



def obtener_info(pais):
    url1 = f'{url_base}/informacion/{pais}'
    response = requests.get(url1)
    
    if response.status_code == 200:
        data = response.json()
        return f'Informacion de {pais}: {data["Informacion"]}'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'
    
def obtener_listas(pais):
    url = f'{url_base}/listas/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'listas mas escuchadas de {pais}: {data["listas"]}'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}' 

def obtener_temperatura(pais):
    url = f'{url_base}/temperature/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Temperatura en {pais}: {data["temperature"]:.2f}°C'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

pais = input("ingrese un pais(Argentina,Chile,Brazil,Colombia o Mexico)")
resultado = obtener_info(pais)
print(resultado)
resultado = obtener_temperatura(pais)
print(resultado)
resultado = obtener_listas(pais)
print(resultado)

# Ejemplos de uso
# paises = ["Argentina", "Brazil", "Chile", "Colombia", "Mexico"]
# for pais in paises:
#     resultado = obtener_temperatura(pais)
#     print(resultado)

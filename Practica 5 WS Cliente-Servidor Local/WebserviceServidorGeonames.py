import http.server
import socketserver
import json
import random

# Datos ficticios de temperatura para países de América Latina
# temperaturas = {
#     "Argentina": random.uniform(5, 30),
#     "Brazil": random.uniform(20, 40),
#     "Chile": random.uniform(5, 25),
#     "Colombia": random.uniform(20, 35),
#     "Mexico": random.uniform(10, 30),
# }
informacion = {
    "Argentina": {"latitud":-34,"longitud":-64},
    "Brazil": {"latitud":-10,"longitud":64},
    "Chile": {"latitud":-3,"longitud":-4},
    "Colombia": {"latitud":34,"longitud":64},
    "Mexico": {"latitud":-4,"longitud":4},
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/informacion/'):
            pais = self.path[13:]
            if pais in informacion:
                data = {"Informacion": informacion[pais]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()
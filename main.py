import requests
import json

class Main:
    
    def start(self) -> None:
        crear_usuario: str = self.crear_usuario()
        obtener_token: dict = self.obtener_token()
        resultado_sin_proteccion: str = self.acceso_sin_proteccion()
        resultado_con_proteccion: str = self.acceso_sin_proteccion()
        
        print(f"La respuesta de 'save-usuario' es: {crear_usuario}")
        print(f"La respuesta de 'iniciar_sesion' es: {obtener_token}")
        print(f"La respuesta de 'acceso_sin_proteccion' es: {resultado_sin_proteccion}")
        print(f"La respuesta de 'acceso_con_proteccion' es: {resultado_con_proteccion}")
    
    def crear_usuario(self) -> str: #save-usuario
        URL: str = "http://localhost:2800/save-usuario"
        headers_envio: dict = {"Content-Type": "application/json"}
        objeto_json: dict = {
            "nombre": "USER",
            "clave": "PASS"
        }
        
        json_envio: str = json.dumps(objeto_json)
        
        try:
            try:
                response: object = requests.post(URL, data = json_envio, headers = headers_envio, timeout = 1)
                codigo: str = str(response.status_code)
                return codigo
            except:
                return "Servidor apagado"
        except:
            return "Error general"
            
    def obtener_token(self) -> dict: #iniciar-sesion
        URL: str = "http://localhost:2800/iniciar_sesion"
        objeto_json: dict = {
            "nombre": "USER",
            "clave": "PASS"
        }
        
        json_envio: str = json.dumps(objeto_json)

        response: object = requests.post(URL, data = json_envio, timeout = 1)
        token: str = response.json().get("token")
        header: dict = {"Authorization": "Bearer " + token}
        return header
    
    def acceso_sin_proteccion(self) -> str: #acceso-sin-proteccion
        URL: str = "http://localhost:2800/acceso-sin-proteccion"
        response: object = requests.get(URL, timeout = 1)
        codigo: str = str(response.status_code)
        return codigo
    
    def acceso_con_proteccion(self) -> str: #acceso-con-proteccion
        URL: str = "http://localhost:2800/acceso-con-proteccion"
        response: object = requests.post(URL, headers = self.obtener_token(), timeout = 1)
        codigo: str = str(response.status_code)
        return codigo
    
main: Main = Main()

main.start()
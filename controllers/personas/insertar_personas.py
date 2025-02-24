import web
from models.personas import Personas

render = web.template.render("views/personas", base="../master")

class InsertarPersonas:
    def __init__(self):
        self.model = Personas()
        
    def GET(self):
        try:
            return render.insertar_personas()
        except Exception as error:
            message = {"error": error.args[0]}
            print(f"ERROR: {message}")
            return message
    
    def POST(self):
        try:
            datos = web.input()  # Capturar datos del formulario
            nombre = datos.nombre.strip()
            telefono = datos.telefono.strip() if "telefono" in datos else ""
            
            # Usar la nueva función del modelo
            resultado = self.model.insertar_persona(nombre, telefono)
            
            if resultado["status"] != 200:
                return resultado["message"]
                
            # Redirigir a la lista de personas
            return web.seeother("/lista_personas")
        except Exception as error:
            return f"Error al guardar: {error}"
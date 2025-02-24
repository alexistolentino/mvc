import web
from models.personas import Personas

# Asegúrate de que la ruta de "views/personas" es la correcta
render = web.template.render("views/personas", base="../master")

class ListaPersonas:
    def GET(self):
        try:
            personas = Personas()
            response = personas.lista_personas()  # Obtén los datos
            if response["status"] == 200:
                datos = response["personas"]
                return render.lista_personas(datos)  # Pasa los datos a la vista
            else:
                return "Error en la obtención de datos"
        except Exception as error:
            print(f"ERROR controllers.personas.lista_personas: {error.args[0]}")
            return "Error en el servidor"
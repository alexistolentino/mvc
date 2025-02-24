import web  # Carga la librería web.py
from controllers.index import Index
from controllers.personas.lista_personas import ListaPersonas
from controllers.personas.insertar_personas import InsertarPersonas

urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
    '/insertar_personas', 'InsertarPersonas',
    '/favicon.ico', 'Favicon',
    "/insertar_personas", "controllers.personas.insertar_personas.InsertarPersonas",
    "/guardar_persona", "controllers.personas.insertar_personas.InsertarPersonas",
    "/ver_persona/(.*)", "VerPersona",
    "/editar_persona/(.*)", "EditarPersona",
    "/eliminar_persona/(.*)", "EliminarPersona"

)

app = web.application(urls, globals())
app = app.wsgifunc()

class Favicon:
    def GET(self):
        web.header('Content-Type', 'image/x-icon')
        return open('demo_MVC/favicon.ico', 'rb').read()

if __name__ == "__main__":
    try:
        web.httpserver.runsimple(app, ("0.0.0.0", 8080))
    except Exception as error:
        print(f"ERROR: {str(error)}")
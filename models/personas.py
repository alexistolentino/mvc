import pyrebase

config = {
    "apiKey": "AIzaSyAw273Ysw9yFZWqageoGMeC-3BaDTmo0ak",
    "authDomain": "bdnube-bc676.firebaseapp.com",
    "databaseURL": "https://bdnube-bc676-default-rtdb.firebaseio.com",
    "storageBucket": "bdnube-bc676.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Personas:
    def __init__(self):
        pass

    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            response = {
                "status": 200,
                "message": "Todo bien :3",
                "personas": dict(personas.val()) if personas.val() else {}
            }
            return response
        except Exception as error:
            response = {
                "status": 400,
                "message": f"Error en el servidor: {error}",
                "personas": {}
            }
            return response
    
    def insertar_persona(self, nombre, telefono=""):
        try:
            # Validación básica
            if not nombre or nombre.strip() == "":
                return {
                    "status": 400,
                    "message": "El nombre es un campo obligatorio",
                    "id": None
                }
            
            # Crear objeto de datos para la nueva persona
            nueva_persona = {
                "nombre": nombre.strip(),
                "telefono": telefono.strip()
            }
            
            # Insertar en Firebase
            resultado = db.child("personas").push(nueva_persona)
            
            # Retornar respuesta exitosa
            return {
                "status": 200,
                "message": "Persona insertada correctamente",
                "id": resultado["name"]  # Esto devuelve el ID generado por Firebase
            }
        except Exception as error:
            # Manejar cualquier error
            return {
                "status": 500,
                "message": f"Error al insertar persona: {error}",
                "id": None
            }

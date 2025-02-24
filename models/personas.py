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
                "personas": dict(personas.val())  # Se corrigió el error de sintaxis
            }
            return response
        except Exception as error:
            response = {
                "status": 400,
                "message": "Error en el servidor",
                "personas": {}
            }
            return response

persona = Personas()
print(f"{persona.lista_personas()}")
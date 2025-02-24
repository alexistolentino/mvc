import web
render = web.template.render('views/personas/', base="../master")

class VerPersona:
    def GET(self, id):
        try:
            ref = db.reference(f'personas/{id}')
            persona = ref.get()

            if not persona:
                return "Persona no encontrada"

            return render.ver_persona(id, persona)

        except Exception as error:
            return f"Error al obtener persona: {error}"

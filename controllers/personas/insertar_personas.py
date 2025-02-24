import web
render = web.template.render("views/personas", base="../master")

class InsertarPersonas:
    def GET(self):
        try:
            return render.insertar_personas()|  
        except Exception as error:
            message = {"error": error.args[0]}
            print(f"ERROR: {message}")
            return message

    def POST(self):
        try:
            datos = web.input()  # Capturar datos del formulario
            nombre = datos.nombre.strip()
            telefono = datos.telefono.strip() if "telefono" in datos else ""

            if not nombre:
                return "El nombre es obligatorio"

            # Guardar en Firebase
            ref = db.reference("personas")
            nueva_persona = ref.push({"nombre": nombre, "telefono": telefono})

            # Redirigir a la lista de personas
            return web.seeother("/lista_personas")
        except Exception as error:
            return f"Error al guardar: {error}"

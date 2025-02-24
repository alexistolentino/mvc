import web

render = web.template.render('views/', base="master")

class Index:
    def GET(self):
        try: 
            return render.index()  # Asegúrate de que `index.html` existe
        except Exception as error:
            message = {
                "error": error.args[0] }
            print(f"ERROR: {message}")
            return message
            
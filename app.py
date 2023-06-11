from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Solution Sprint Fase5 Grupo1."

if __name__ == '__main__':
    app.run()
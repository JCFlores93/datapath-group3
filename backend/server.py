from crypt import methods
import json
from flask import Flask, request, jsonify
from module.database import Database

app = Flask(__name__)
db = Database()

ROWS_PER_REQUEST = 20

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/read_embargos", defaults={"page": 1})
@app.route("/read_embargos/page/<int:page>", methods=["GET"])
def read_embargos(page):
    try:
        start_at = page * ROWS_PER_REQUEST
        print(" GET ", request)
        print(start_at)
        print(page)
        # query = ("SELECT * FROM embargos order by nombre_completo asc limit %s, %s;", (start_at, ROWS_PER_REQUEST))
        query = f"SELECT * FROM embargos order by nombre_completo asc limit {start_at}, {ROWS_PER_REQUEST};"
        result = db.read(query)
        print(result)
    except Exception as e:
        print(e)
        return e
    return jsonify({"rows": result})

@app.route("/read_resultados", defaults={"page": 1})
@app.route("/read_resultados/page/<int:page>", methods=["GET"])
def read_productos(page):
    try:
        start_at = page * ROWS_PER_REQUEST
        print(" GET ", request)
        print(start_at)
        print(page)
        query = ("SELECT * FROM resultados order by encargado asc limit %s, %s;", (start_at, ROWS_PER_REQUEST))
        result = db.read(query)
        print(result)
    except Exception as e:
        return e
    return jsonify({"rows": result})

if __name__ == "__main__":
    app.debug = True
    app.run()
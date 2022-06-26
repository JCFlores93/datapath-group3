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
        query = ("SELECT * FROM embargos order by name asc limit %s, %s;", (start_at, ROWS_PER_REQUEST))
        result = db.read(query)
        print(result)
    except Exception as e:
        return e
    return jsonify({"rows": result})

@app.route("/read_products", defaults={"page": 1})
@app.route("/read_products/page/<int:page>", methods=["GET"])
def read_productos(page):
    try:
        start_at = page * ROWS_PER_REQUEST
        print(" GET ", request)
        print(start_at)
        print(page)
        query = ("SELECT * FROM productos order by name asc limit %s, %s;", (start_at, ROWS_PER_REQUEST))
        result = db.read(query)
        print(result)
    except Exception as e:
        return e
    return jsonify({"rows": result})

@app.route("/add_embargo", methods=["POST"])
def add_embargo():
    if request.method == "POST":
        print("POST")
        try:
            print(request)
            query = '''
                INSERT INTO embargos(
                estado,
                anotacion,
                localidad,
                complejidad,
                detalle_complejidad,
                encargado,
                fecha_recepcion,
                hora_recepcion,
                job_id,
                fecha_embargo,
                id_oracle,
                efectivo,
                tipo_documento,
                numero_documento,
                tipo_cuenta,
                numero_cuenta
                ) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,)
            ''', (
                    request.json['estado'], 
                    request.json['anotacion'], 
                    request.json['localidad'],
                    request.json['complejidad'], 
                    request.json['detalle_complejidad'], 
                    request.json['encargado'],
                    request.json['fecha_recepcion'], 
                    request.json['hora_recepcion'], 
                    request.json['job_id'],
                    request.json['fecha_embargo'], 
                    request.json['id_oracle'], 
                    request.json['efectivo'],
                    request.json['tipo_documento'], 
                    request.json['numero_documento'], 
                    request.json['tipo_cuenta'],
                    request.json['numero_cuenta'],
                )
            db.insert(query)
        except Exception as e:
            print(e)
            return e
    return jsonify({ "add_embargo": request.json["numero_cuenta"]})

if __name__ == "__main__":
    app.debug = True
    app.run()
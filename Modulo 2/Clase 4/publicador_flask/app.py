from flask import Flask, request, jsonify
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db, Usuario, Articulo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

first_request = True

@app.before_request
def create_tables():
    global first_request
    if first_request:
        db.create_all()
        first_request = False

@app.route("/")
def inicio():
    return "Bienvenido al sistema de publicación de artículos(SQLite)"

@app.route("/usuarios", methods=["POST"])
def crear_usuario():
    documento = request.form.get("documento")
    nombre = request.form.get("nombre")
    email = request.form.get("email")

    nuevo_usuario = Usuario(nombre=nombre, documento=documento, email=email)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return f"Usuario {nuevo_usuario.nombre} creado con éxito."

@app.route("/usuarios" ,methods=["GET"])
def listar_usuarios():
    '''
    usuarios = Usuario.query.all()
    return "<br>".join([f"ID: {usuario.id}, Nombre: {usuario.nombre}, Documento: {usuario.documento}, Email: {usuario.email}" for usuario in usuarios])
    '''

    usuarios = Usuario.query.all()
    lista = [
        {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "documento": usuario.documento,
            "email": usuario.email,
            
        }
        for usuario in usuarios
    ]
    return jsonify(lista)

@app.route("/articulos", methods=["POST"])
def crear_articulo():
    titulo = request.form.get("titulo")
    texto = request.form.get("texto")
    usuario_id = request.form.get("usuario_id")

    nuevo_articulo = Articulo(titulo=titulo, texto=texto, usuario_id=usuario_id)
    db.session.add(nuevo_articulo)
    db.session.commit()
    return f"Artículo '{nuevo_articulo.titulo}' creado con éxito."

@app.route("/articulos", methods=["GET"])
def listar_articulos():
    articulos = Articulo.query.all()
    lista = [
        {
            "id": articulo.id,
            "titulo": articulo.titulo,
            "texto": articulo.texto,
            "usuario_id": articulo.usuario_id,
            "fecha_publicacion": articulo.fecha_publicacion
        }
        for articulo in articulos
    ]
    return jsonify(lista)




if __name__ == "__main__":
    app.run(debug=True)
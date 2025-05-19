from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

def now_utc():
    return datetime.now(timezone.utc)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    documento = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    creando_em = db.Column(db.DateTime(timezone=True), default=now_utc)
    modificando_em = db.Column(db.DateTime(timezone=True), default=now_utc, onupdate=now_utc)

    #articulos = db.relationship('Articulo', backref='autor', cascade='all, delete', lazy=True)


class Articulo(db.Model):
    __tablename__ = 'articulos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    fecha_publicacion = db.Column(db.DateTime(timezone=True))

    creando_em = db.Column(db.DateTime(timezone=True), default=now_utc)
    modificando_em = db.Column(db.DateTime(timezone=True), default=now_utc, onupdate=now_utc)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nome}>'
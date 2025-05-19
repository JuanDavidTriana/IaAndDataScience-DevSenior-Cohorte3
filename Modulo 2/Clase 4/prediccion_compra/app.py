from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db
from router import router
from predictor import entrenar_modelo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
app.register_blueprint(router)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
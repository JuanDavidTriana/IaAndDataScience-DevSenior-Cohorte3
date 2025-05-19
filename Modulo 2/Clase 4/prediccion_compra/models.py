from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    AnnualIncome = db.Column(db.Float, nullable=False)
    NumberOfPurchases = db.Column(db.Integer, nullable=False)
    ProductCategory = db.Column(db.Integer, nullable=False)
    TimeSpentOnWebsite = db.Column(db.Float, nullable=False)
    LoyaltyProgram = db.Column(db.Integer, nullable=False)
    DiscountsAvailed = db.Column(db.Integer, nullable=False)
  
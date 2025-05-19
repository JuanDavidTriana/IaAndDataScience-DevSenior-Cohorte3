from flask import Blueprint, request, jsonify
from models import db, Usuarios
from predictor import cargar_modelo, entrenar_modelo

router = Blueprint('router', __name__)
modelo = cargar_modelo()
entrenar_modelo()

@router.route('/usuarios', methods=['POST'])
def agregar_usuario(): 
    data = request.form
    nuevo_usuario = Usuarios(
        age=int(data['Age']),
        gender=data['Gender'],
        AnnualIncome=float(data['AnnualIncome']),
        NumberOfPurchases=int(data['NumberOfPurchases']),
        ProductCategory=data['ProductCategory'],
        TimeSpentOnWebsite=float(data['TimeSpentOnWebsite']),
        LoyaltyProgram=data['LoyaltyProgram'],
        DiscountsAvailed=float(data['DiscountsAvailed'])
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario agregado exitosamente'}), 201

@router.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuarios.query.all()
    usuarios_list = []
    for usuario in usuarios:
        usuarios_list.append({
            'Id': usuario.id,
            'Age': usuario.age,
            'Gender': usuario.gender,
            'AnnualIncome': usuario.AnnualIncome,
            'NumberOfPurchases': usuario.NumberOfPurchases,
            'ProductCategory': usuario.ProductCategory,
            'TimeSpentOnWebsite': usuario.TimeSpentOnWebsite,
            'LoyaltyProgram': usuario.LoyaltyProgram,
            'DiscountsAvailed': usuario.DiscountsAvailed
        })
    return jsonify(usuarios_list)

@router.route('/predecir', methods=['POST'])
def predecir_compra():

    data = request.form

    try:
        age = int(data['Age'])
        gender = int(data['Gender'])
        AnnualIncome = float(data['AnnualIncome'])
        NumberOfPurchases = int(data['NumberOfPurchases'])
        ProductCategory = int(data['ProductCategory'])
        TimeSpentOnWebsite = float(data['TimeSpentOnWebsite'])
        LoyaltyProgram = int(data['LoyaltyProgram'])
        DiscountsAvailed = int(data['DiscountsAvailed'])
    

        X = [[age, gender, AnnualIncome, NumberOfPurchases, ProductCategory, TimeSpentOnWebsite, LoyaltyProgram, DiscountsAvailed]]

        probabilidad_compra = modelo.predict_proba(X)[0][1]

        predicion = probabilidad_compra * 100

        return jsonify({
            'ProbabilidadCompra': f"{predicion}"
        })
    
    except ValueError as e:
        return jsonify({'error': 'Error en los datos de entrada: {}'.format(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error inesperado: {}'.format(e)}), 500
    

@router.route('/predecir/<id>', methods=['GET'])
def predecir_compra_id(id):
    usuario = Usuarios.query.get(id)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    X = [[usuario.age, usuario.gender, usuario.AnnualIncome, usuario.NumberOfPurchases, usuario.ProductCategory, usuario.TimeSpentOnWebsite, usuario.LoyaltyProgram, usuario.DiscountsAvailed]]
    probabilidad_compra = modelo.predict_proba(X)[0][1]
    predicion = probabilidad_compra * 100
    return jsonify({
        'Id': usuario.id,
        'ProbabilidadCompra': f"{predicion}"
    })

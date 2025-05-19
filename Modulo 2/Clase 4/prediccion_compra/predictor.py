import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

def entrenar_modelo():
    # Cargar los datos
    df = pd.read_csv('customer_purchase_data.csv')

    # Seleccionar las características y la variable objetivo 
    x = df[['Age', 'Gender', 'AnnualIncome', 'NumberOfPurchases', 'ProductCategory','TimeSpentOnWebsite','LoyaltyProgram','DiscountsAvailed']]
    y = df['PurchaseStatus']

    # Entrenar el modelo
    model = LogisticRegression()
    model.fit(x, y)

    # Guardar el modelo entrenado
    os.makedirs('static', exist_ok=True)
    joblib.dump(model, 'static/modelo_entrenado.pkl')
    print("Modelo entrenado y guardado como 'modelo_entrenado.pkl' en la carpeta 'static'.")

def cargar_modelo():
    if not os.path.exists('static/modelo_entrenado.pkl'):
        print("No se encontró el modelo entrenado. Entrenando el modelo...")
        entrenar_modelo()
    return joblib.load('static/modelo_entrenado.pkl')
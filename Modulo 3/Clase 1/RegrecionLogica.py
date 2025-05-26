import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression # Importamos el modelo de regresión lineal
from sklearn.model_selection import train_test_split # Para dividir los datos
from sklearn.metrics import mean_squared_error, r2_score # Nuestras métricas de evaluación


df = pd.read_csv('diabetes.csv')

print(df.info())

x = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = df['Outcome']


model = LogisticRegression()  # Creamos el modelo de regresión lineal

# -- dividir los datos --

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"cuantos va entrenar el modelo: {len(x_train)}")
print(f"cuantos va probar el modelo: {len(x_test)}")


model.fit(x_train, y_train)  # Entrenamos el modelo con los datos

# -- predecir con el modelo --

y_pred = model.predict(x_test)

# -- evaluar el modelo --

print("Accuracy:", model.score(x_test, y_test))
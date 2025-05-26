import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # Importamos el modelo de regresión lineal
from sklearn.model_selection import train_test_split # Para dividir los datos
from sklearn.metrics import mean_squared_error, r2_score # Nuestras métricas de evaluación

# -- 1. Preparación de los datos --
# Cargamos el dataset
horas_estudio = np.array([2, 3, 4, 5, 6]) 
calificaciones = np.array([60, 70, 75, 80, 90])

# Creamos un DataFrame
df = pd.DataFrame({
    'HorasEstudio': horas_estudio,
    'Calificaciones': calificaciones
})

print("Datos originales:")
print(df)

x = df[['HorasEstudio']]  # Variable independiente (X)
y = df['Calificaciones']  # Variable dependiente (y)

model = LinearRegression()  # Creamos el modelo de regresión lineal

# -- 2. División de los datos --
model.fit(x, y)  # Entrenamos el modelo con los datos

beta_1_sklearn = model.coef_[0]  # Coeficiente de la variable independiente
beta_0_sklearn = model.intercept_  # Intercepto del modelo

print(f"Coeficiente (beta_1): {beta_1_sklearn}")
print(f"Intercepto (beta_0): {beta_0_sklearn}")

hora_a_predecir = 4  # Horas de estudio para predecir la calificación
calificacion_predicha = model.predict([[hora_a_predecir]])[0]  # Predicción

print(f"Calificación predicha para {hora_a_predecir} horas de estudio: {calificacion_predicha}")

# Visualización de los datos y la línea de regresión

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Datos originales')  # Puntos de datos
plt.plot(x, model.predict(x), color='red', label='Línea de regresión')  # Línea de regresión
plt.title('Regresión Lineal: Horas de Estudio vs Calificaciones')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificaciones')
plt.legend()
plt.show()
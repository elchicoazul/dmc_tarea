# src/evaluate.py
###############################################################
# EVALUATE MODEL - Employee Attrition (Adaptado al ejemplo)
###############################################################

import pandas as pd
import pickle
import os
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Rutas
PROCESSED_PATH = "../data/processed/attrition_processed.csv"
MODEL_PATH = "../models/best_model.pkl"


def eval_model():

    # 1. Cargar dataset procesado
    df = pd.read_csv(PROCESSED_PATH)
    print("Archivo procesado cargado:", PROCESSED_PATH)

    # 2. Cargar modelo entrenado
    model = pickle.load(open(MODEL_PATH, "rb"))
    print("Modelo cargado correctamente:", MODEL_PATH)

    # 3. Separar X, y
    X_test = df.drop("AttritionFlag", axis=1)
    y_test = df["AttritionFlag"]

    # 4. Predicción
    y_pred = model.predict(X_test)

    # 5. Métricas
    print("\n==============================")
    print("  MÉTRICAS DE EVALUACIÓN")
    print("==============================\n")

    cm = confusion_matrix(y_test, y_pred)
    print("Matriz de Confusión:")
    print(cm)

    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))


def main():
    eval_model()
    print("\nFinalizó la evaluación del modelo.\n")


if __name__ == "__main__":
    main()

# src/predict.py
###############################################
# PREDICT - Employee Attrition
###############################################

import pandas as pd
import pickle
import os

MODEL_PATH = "../models/best_model.pkl"
INPUT_PATH = "../data/processed/attrition_processed.csv"
OUTPUT_PATH = "../data/scores/attrition_predictions.csv"


def predict():
    # Leer modelo
    model = pickle.load(open(MODEL_PATH, "rb"))
    print("Modelo cargado correctamente")

    # Cargar dataset para scoring
    df = pd.read_csv(INPUT_PATH)

    X = df.drop("AttritionFlag", axis=1)

    preds = model.predict_proba(X)[:, 1]  # probabilidad de renunciar
    df["AttritionScore"] = preds

    df.to_csv(OUTPUT_PATH, index=False)
    print("Predicciones guardadas en:", OUTPUT_PATH)


if __name__ == "__main__":
    predict()

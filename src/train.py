# src/train.py
###############################################
# TRAIN MODEL - Employee Attrition
###############################################

import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

PROCESSED_PATH = "../data/processed/attrition_processed.csv"
MODEL_PATH = "../models/best_model.pkl"


def train_model():

    df = pd.read_csv(PROCESSED_PATH)
    print("Datos procesados cargados:", df.shape)

    X = df.drop("AttritionFlag", axis=1)
    y = df["AttritionFlag"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Entrenando modelo Random Forest...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Guardar modelo
    pickle.dump(model, open(MODEL_PATH, "wb"))
    print("Modelo guardado en:", MODEL_PATH)


if __name__ == "__main__":
    train_model()

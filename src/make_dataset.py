# src/make_dataset.py
###############################################
# MAKE DATASET - Employee Attrition
###############################################

import pandas as pd
import os

RAW_PATH = "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
PROCESSED_PATH = "../data/processed/attrition_processed.csv"


def make_dataset():
    # 1. Leer archivo
    df = pd.read_csv(RAW_PATH)
    print("Dataset cargado correctamente:", df.shape)

    # 2. Convertir Attrition a binario
    df["AttritionFlag"] = df["Attrition"].map({"Yes": 1, "No": 0})

    # 3. Seleccionar features relevantes
    FEATURES = [
        "Age", "MonthlyIncome", "DistanceFromHome", "JobSatisfaction",
        "EnvironmentSatisfaction", "NumCompaniesWorked", "YearsAtCompany",
        "TrainingTimesLastYear", "OverTime", "AttritionFlag"
    ]

    df = df[FEATURES]

    # 4. Convertir OverTime a dummy
    df["OverTime"] = df["OverTime"].map({"Yes": 1, "No": 0})

    # 5. Exportar
    df.to_csv(PROCESSED_PATH, index=False)
    print("Archivo procesado exportado a:", PROCESSED_PATH)


if __name__ == "__main__":
    make_dataset()

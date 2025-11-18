import subprocess
import sys
import os

# Ruta a tu carpeta src
SRC_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))

# Lista de scripts en orden
scripts = [
    "make.py",
    "train.py",
    "evaluate.py",
    "predict.py"
]

def run_script(script_name):
    script_path = os.path.join(SRC_FOLDER, script_name)

    print("\n==============================")
    print(f"▶ Ejecutando: {script_name}")
    print("==============================\n")

    if not os.path.exists(script_path):
        print(f"❌ ERROR: El archivo no existe: {script_path}")
        sys.exit(1)

    result = subprocess.run([sys.executable, script_path])

    if result.returncode != 0:
        print(f"❌ Error ejecutando {script_name}. Pipeline detenido.")
        sys.exit(result.returncode)

    print(f"✅ {script_name} ejecutado correctamente.\n")


def main():
    print("\n⚙️ INICIANDO PIPELINE COMPLETO\n")

    for script in scripts:
        run_script(script)

    print("\n🚀 PIPELINE COMPLETO FINALIZADO CON ÉXITO\n")


if __name__ == "__main__":
    main()

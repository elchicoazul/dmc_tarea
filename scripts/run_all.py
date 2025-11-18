import subprocess
import sys

scripts = [
    "make.py",
    "train.py",
    "evaluate.py",
    "predict.py"
]

def run_script(script):
    print(f"\n==============================")
    print(f"▶ Ejecutando: {script}")
    print(f"==============================\n")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"❌ Error al ejecutar {script}. Pipeline detenido.")
        sys.exit(result.returncode)

    print(f"✅ {script} ejecutado correctamente.\n")

def main():
    print("\n⚙️ INICIANDO PIPELINE COMPLETO\n")

    for script in scripts:
        run_script(script)

    print("\n🚀 PIPELINE COMPLETO FINALIZADO CON ÉXITO\n")

if __name__ == "__main__":
    main()

import subprocess

# List of (script, config) pairs to run
tasks = [
    ("scripts/layout_detection.py", "configs/layout_detection.yaml"),
    ("scripts/formula_detection.py", "configs/formula_detection.yaml"),
    ("scripts/ocr.py", "configs/ocr.yaml"),
    ("scripts/formula_recognition.py", "configs/formula_recognition.yaml"),
    ("scripts/table_parsing.py", "configs/table_parsing.yaml"),
]

def run_pipeline():
    for script, config in tasks:
        print(f"\n🔧 Running {script} with config {config}...")
        try:
            result = subprocess.run(
                ["python", script, "--config", config],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"✅ Finished {script}\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error in {script}")
            print(e.stderr)

if __name__ == "__main__":
    run_pipeline()
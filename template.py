import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "src/utils/utils.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        print(f"Creating directory: {filedir}")
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        print(f"Creating file: {filepath}")
        with open(filepath, "w") as f:
            pass  # create an empty file

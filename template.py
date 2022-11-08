import os
from pathlib import Path
import logging

logging.basicConfig(
    level= logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the project Name:")
    if project_name != '':
        break

logging.info(f"Createing project by name: {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/{project_name}/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requiremnts.txt",
    "requirments_dev.txt",
    "setup.py",
    "project.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(Path(filepath))
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"createing a directory at: {filedir} for all file: {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already exist at path: {filepath}")


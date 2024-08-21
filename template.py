import os
from pathlib import Path #To take care of OS specific paths like bash or windows in the terminal
import logging 

logging.basicConfig(
    level=logging.INFO,
    format = "[%(asctime)s: %(levelname)s: %(message)s]"
    )

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != "":
        break

logging.info(f"Creating project by name: {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",#to keep action files for checks
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",#to create a repo with env setup like conda envi setup
    "requirements.txt",#main requirements
    "requirements_dev.txt", #used for testing to keep pytest libraries
    "setup.py", #To perform the basic setup
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"#to test the python package on various envs

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a file directory at: {filepath} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created a new file: {filename} at path {filepath}")
    else:
        logging.info(f"File {filename} already exists at path {filepath}")        


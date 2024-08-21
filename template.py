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
    
    f"src/{project_name}/__init__.py",
    
    
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


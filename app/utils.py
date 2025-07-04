import json    
import os
import shutil

FILE_PATH = "dotfiles.json" 

with open(FILE_PATH, 'r') as f:
    json_data = json.load(f)

def get_computers():
    return [item["computer"] for item in json_data]

def get_dotfiles_by_computer(computer: str):
    computer_found = False
    for item in json_data:
        if item["computer"] == computer:
            computer_found = True
            return item["dotfiles"]
    if not computer_found:
        raise ValueError(f"Computer '{computer}' not found in dotfiles data.")

def validate_if_exists(file_path: str):
    if os.path.exists(os.path.expanduser(file_path)):
        print('exists')
        return True
    else:
        print("doesn't exists")
        return False

def validate_files(file_paths: list[str]):
    for file_path in file_paths:
        validate_if_exists(file_path)

def validate_files_by_computer(computer: str):
    validate_files(get_dotfiles_by_computer(computer))

def copy_file(computer: str, file_path: str):
    # Remove leading ~ and expand to absolute path
    abs_path = os.path.expanduser(file_path)
    if file_path.startswith('~'):
        rel_path = file_path[2:] if file_path.startswith('~/') else file_path[1:]
    else:
        rel_path = os.path.relpath(abs_path, os.path.expanduser('~'))
    dest_dir = os.path.join("files", computer, os.path.dirname(rel_path))
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, os.path.basename(rel_path))
    shutil.copy(abs_path, dest_path)
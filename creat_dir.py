import os

def create_dir(path):
    try:
        os.makedirs(path)
        print(f"Папка {path} успешно создана")
    except:
        print(f"Папка {path} уже существует")
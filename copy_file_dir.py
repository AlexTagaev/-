import os
import shutil

def copy_file_dir(path_from, path_to):
  for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in files:
      if name == path_from:
        print(os.path.join(root, name))
        shutil.copy2(os.path.join(root, name), os.path.join(path_to, name))
        break
    for name in dirs:
      if name == path_from:
        shutil.copytree(os.path.join(root, name), os.path.join(path_to, name), dirs_exist_ok=True)
        break
  print(f"Объект {path_from} успешно скопирован в {path_to}")
    
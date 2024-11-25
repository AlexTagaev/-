import os
import shutil

def del_file_dir(path):
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for name in files:
          if name == path:
            os.remove(os.path.join(root, name))
            break
        for name in dirs:
          if name == path:
            shutil.rmtree(os.path.join(root, name))
            break
    print(f"Объект {path} успешно удален")
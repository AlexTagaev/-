import os

def change_dir(path):
  try:
    os.chdir(path)
    print("Вы теперь работаете в директории:")
    print(os.getcwd())
  except:
    print("Проверьте корректность пути или названия директории!")
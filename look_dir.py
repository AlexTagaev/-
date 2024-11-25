import os

def look_dir():
    print('Текущая директория содержит следующие объекты:')
    for name in os.listdir():
      print(name)
import os

def look_corr_dir():
  print('Текущая директория содержит следующие папки:')
  for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in dirs:
      print(name)
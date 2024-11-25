import os

def look_corr_files():
  print('Текущая директория содержит следующие файлы:')
  for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in files:
      print(name)
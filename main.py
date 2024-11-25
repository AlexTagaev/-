from creat_dir import create_dir
from del_file_dir import del_file_dir
from copy_file_dir import copy_file_dir
from look_dir import look_dir
from look_corr_dir import look_corr_dir
from look_corr_files import look_corr_files
from look_platform import look_platform
from change_dir import change_dir
import personal_account
import victory

print('КОНСОЛЬНЫЙ ФАЙЛОВЫЙ МЕНЕДЖЕР')
print('*' * 20)
while True:
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки (в текущей директории)')
    print('6. посмотреть только файлы (в текущей директории)')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        print('Вы выбрали пункт меню "Создать папку"')
        print('-' * 10)
        name = input('Введите название папки: ')
        create_dir(name)
        print()
    elif choice == '2':
        print('Вы выбрали пункт меню "Удалить (файл/папку)"')
        print('-' * 10)
        name = input('Введите название файла/папки: ')
        del_file_dir(name)
        print()
    elif choice == '3':
        print('Вы выбрали пункт меню "Копировать (файл/папку)"')
        print('-' * 10)
        name_old = input('Введите название копируемого файла/папки: ')
        name_new = input('Введите новое название/расположение копируемого файла/папки: ')
        copy_file_dir(name_old, name_new)
        print()
    elif choice == '4':
        print('Вы выбрали пункт меню "Просмотр содержимого рабочей директории"')
        print('-' * 10)
        look_dir()
        print()
    elif choice == '5':
        print('Вы выбрали пункт меню "Посмотреть только папки (в текущей директории)"')
        print('-' * 10)
        look_corr_dir()
        print()
    elif choice == '6':
        print('Вы выбрали пункт меню "Посмотреть только файлы (в текущей директории)"')
        print('-' * 10)
        look_corr_files()
        print()
    elif choice == '7':
        print('Вы выбрали пункт меню "Просмотр информации об операционной системе"')
        print('-' * 10)
        look_platform()
        print()
    elif choice == '8':
        print('Вы выбрали пункт меню "Создатель программы"')
        print('-' * 10)
        print('Создатель программы : Александр Тагаев')
        print()
    elif choice == '9':
        print('Вы выбрали пункт меню "Играть в викторину"')
        print('-' * 10)
        victory
        print()
    elif choice == '10':
        print('Вы выбрали пункт меню "Мой банковский счет"')
        print('-' * 10)
        personal_account
        print()
    elif choice == '11':
        print('Вы выбрали пункт меню "Смена рабочей директории"')
        print('-' * 10)
        name = input('Введите название директории: ')
        change_dir(name)
        print()
    elif choice == '12':
        print('Вы выбрали пункт меню "Выход"')
        break
    else:
        print('Неверный пункт меню')
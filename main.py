from pathlib import Path
import task01
import task02
from colorama import Fore

main_menu = '''1. Підрахунок заробітних плат
2. Котики
3. Структура директорії
4. Бот
5. Вихід'''

print(main_menu)

while True:
    action = input('Введіть, будь ласка, номер завдання, або \'5\' для виходу: ')

    print('\n')

    match action:
        case '1':
            file_path = Path(__file__).with_segments('data/salaries.txt')

            total, average = task01.total_salary(file_path)

            print(f'Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}')
        case '2':
            file_path = Path(__file__).with_segments('data/cats.txt')

            cats = task02.get_cats_info(file_path)

            print(cats)
        case '3':
            print('Будь ласка, запустіть \'task03.py\' з директорією у якості аргументу. Наприклад:')
            print('python ' + Fore.BLUE + 'task03.py ' + Fore.CYAN + '/home/user/documents' + Fore.RESET)
        case '4':
            print('Будь ласка, запустіть \'python task04.py\'')
        case '5':
            break
        case other:
            print(f'{other} is not a task number or \'5\'')

    print('\n')

    input('Натисніть Enter для продовження...')

    print(main_menu)
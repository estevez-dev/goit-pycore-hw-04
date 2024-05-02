from pathlib import Path
import task01

main_menu = '''1. Підрахунок заробітних плат
2. 
3. 
4. 
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
            print('Unimplemented yet')
        case '3':
            print('Unimplemented yet')
        case '4':
            print('Unimplemented yet')
        case '5':
            break
        case other:
            print(f'{other} is not a task number or \'5\'')

    print('\n')

    input('Натисніть Enter для продовження...')

    print(main_menu)
from pathlib import Path
import task01

main_menu = '''1. Total salary calculator
2. 
3. 
4. 
5. Exit'''

print(main_menu)

while True:
    action = input('Please, enter task number to start, or \'5\' to exit: ')

    match action:
        case '1':
            file_path = Path(__file__).with_segments('data/salaries.txt')

            result = task01.total_salary(file_path)

            print(f'total_salary execution result: {result}')
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

    input('Press Enter to continue...')

    print(main_menu)
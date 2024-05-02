import sys
from colorama import Fore
from pathlib import Path

def list_dir(dir, level):
    
    prefix = '  ' * level

    for child in dir.iterdir():
        if child.is_dir():
            print(Fore.BLUE + prefix + child.name + '/' + Fore.RESET)
            list_dir(child, level=level+1)
        else:
            print(Fore.GREEN + prefix + child.name + Fore.RESET)

def main():
    if len(sys.argv) < 2:
        print(Fore.RED + 'Ви забули передати шлях до директорії у якості аргументу' + Fore.RESET)

        return

    dir_path = sys.argv[1]

    directory = Path(dir_path)

    if not directory.exists():
        print(Fore.RED + f'Такого шляху не існує: {dir_path}' + Fore.RESET)

        return

    if not directory.is_dir():
        print(Fore.RED + f'{dir_path} не є директорією' + Fore.RESET)

        return
    
    print(Fore.BLUE + directory.name + '/' + Fore.RESET)
    
    list_dir(directory, 1)

if __name__ == "__main__":
    main()
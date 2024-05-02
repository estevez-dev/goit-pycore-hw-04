def total_salary(path):
    try:
        with open(path, 'r') as database:
            salaries = []

            while True:
                line = database.readline()
                
                if not line:
                    break
                
                data = line.split(',')

                if len(data) == 2 and data[1].isnumeric:
                    salary = int(data[1])

                    salaries.append(salary)
            
            total_salary = sum(salaries)

            if len(salaries) == 0:
                print('Не знайдено жодного запису з заробітною платою')
                return (0, 0)

            return (sum(salaries), total_salary / len(salaries))
    
    except FileNotFoundError:
        print('Файл не знайдено')

    except:
        print('Щось пішло не так')
    
    return (0, 0)
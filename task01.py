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

            return (sum(salaries), total_salary / len(salaries))
    except FileNotFoundError:
        print('Data file not found')

        return ()
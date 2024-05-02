cat = r'''    /\_____/\
   /  o   o  \
  ( ==  ^  == )
   )         (
  (           )
 ( (  )   (  ) )
(__(__)___(__)__)'''

def get_cats_info(path):
    print(cat)

    cats = []

    try:
        with open(path, 'r') as cats_file:
            

            while True:
                cat_line = cats_file.readline()
                
                if not cat_line:
                    break
                
                cat_data = cat_line.split(',')

                if len(cat_data) == 3:
                    cats.append({'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2].removesuffix('\n')})
                else:
                    print(f'Цей котик пошкоджений і не може бути оброблений: {cat_data}')
            
            if len(cats) == 0:
                print('Котиків у файлі не виявлено')
    
    except FileNotFoundError:
        print('Котиків не знайдено')

    except:
        print('Щось пішло не так')
    
    return cats

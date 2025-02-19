def read_file(): 
    '''
    Функция чтения строк из txt и преобразование в список словарей для удобства анализа
    '''
    with open("data_finaly_project.txt", "r") as file:  # 
        purchases=[]
        for row in file:
            stroke = row.replace(" ", "").replace('"','').split(',')
            my_dict = {}
            for item in stroke:
                key, value = item.split(':')
                try:
                    my_dict[key] = float(value)
                except ValueError as e:
                    my_dict[key] = value
            purchases.append(my_dict)
    return purchases

def total_revenue(purchases):
    '''
    Функция принимает список строк и возвращает общую выручку
    '''
    sum=0
    for line in purchases:
        sum = sum + (line['price']*line['quantity'])
    return sum

def items_by_category(purchases):
    '''
    Функция принимает список строк и возвращает словарь {Категория : список уникальных товаров}
    '''
    my_dict = {}
    for line in purchases:
        key=line["category"]
        if key not in  my_dict.keys():
            my_dict[key] = [line['item']]
        else:
            my_dict[key].append(line['item']) 
    return my_dict

def expensive_purchases(purchases, min_price):
    '''
    Функция принимает список строк и минимальную суммму.Возвращает покупки,цена товара которых более "min_price"
    '''
    new_dict = purchases
    for line in new_dict:
        if line['price'] < min_price:
            new_dict.remove(line)
    return new_dict
    
def average_price_by_category(purchases):
    '''
    Функция принимает список строк и возвращает среднюю цену по каждой категории
    '''
    my_dict = {}
    for line in purchases:
        key=line["category"]
        if key not in  my_dict.keys():
            my_dict[key] = line['price']
        else:
            my_dict[key] = (my_dict[key] +  line['price'])/2.0   
    return my_dict

def most_frequent_category(purchases):
    '''
    Функция принимает список строк и возвращает категорию с самыми высокими продажами
    '''
    max_quantity = 0
    for line in purchases:
        if line['quantity'] > max_quantity:
            max_quantity = line['quantity']
            category = line['category']
    return category

min_cost = float(input("Введите минимальную цену для сортировки покупок"))
test=read_file()
print(f"Общая выручка: {total_revenue(test)}")
print(f"Товары по категориям: {items_by_category(test)}")
print(f"Покупки дороже {min_cost}: {expensive_purchases(test,min_cost)}")
print(f"Средняя цена по категориям: {average_price_by_category(test)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(test)}")


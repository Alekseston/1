# Предусловие.
# Задачи 3 и 4 :
# 2) В виде функций - код разбит на функции.
# Отдельные функции можно вынести в другие .py файлы и вызывать их в main.py
# предварительно импортируя в main.py.
def dict_data(**kwargs):
    global c
    c = {**kwargs}
def change():
    b = input()
    if b.strip() == "" or len(b) == 0:
        print('Вы ввели пустое поле. Введите число.')
    else:
        try:
            if int(b) >= 0:
                print('Ты ввёл int (RUB)', b)
                for i, y in c.items():
                    if a:
                        if i == a:
                            r = int(b) / int(y)
                            print('конвертированная сумма в ' + a + ' = int', int(r))
                            break
                    else:
                        r1 = int(b) / int(y)
                        print('конвертированная сумма в ' + i + ' = int', int(r1))
            elif int(b) < 0:
                print('Введите положительное число.')
        except:
            print('Вы ввели не число. Введите число.')


# def main():
#     dict_data(USD=78, EUR=89, CHF=86, GBP=107, CNY=12)
#     # while True:
#     #     print("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")
#     global a
#     a = False
#         #     a = input()
#     #     for i, y in c.items():
#     #         if i == a:
#     #             print('Введите сумму')
#     change()
# if __name__=='__main__':
#     main()

def change_all():
    dict_data(USD=78, EUR=89, CHF=86, GBP=107, CNY=12)
    global a
    a = False
    change()
def change_one():
    dict_data(USD=78, EUR=89, CHF=86, GBP=107, CNY=12)
    while True:
        print("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")
        global a
        a = False
        a = input()
        print('Введите сумму')
        change()

def change_1():
    while True:
        print("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")
        global a
        a = False
        a = input()
        print('Введите сумму')
        change()
def change_all1():
    global a
    a = False
    change()



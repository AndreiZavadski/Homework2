age = int(input('Введите человеческий возраст'))
if age <= 21 and age > 0: #Условие, когда собаке меньше 2 лет
    print(age / 10.5) #Вывод на собачий
elif age > 21: #Условие, когда собака старше 2 лет
    print(2 + (age - 21) / 4) #Вывод на собачий
else:
    print('Неверное утверждение ')

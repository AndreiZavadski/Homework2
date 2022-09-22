compnum = 50
number = int(input('Введите число : '))
attempt = 1  # создаем переменную с количеством попыток
while number > compnum:
    if number > compnum:  # создаем условие при if number > compnum
        print(number, 'это число больше переменной compnum')
        number = int(input('Введите число : '))  # запрашиваем еще одно число
        attempt += 1  # увеличиваем количество попыток
while number < compnum:
    if number < compnum:  # создаем условие при if number < compnum
        print(number, 'это число меньше переменной compnum')
        number = int(input('Введите число : '))  # запрашиваем еще одно число
        attempt += 1  # увеличиваем количество попыток
        continue
else:
    print('Well done you took', attempt, 'attempts')  # выводим результат

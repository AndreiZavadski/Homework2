name = str(input('Введите имя человека, которого Вы хотите пригласить на вечеринку : '))
print(name, 'has been invited')
counter = 1 #создали счетчик
question = str(input('Хотите ли Вы пригласить кого-то еще(y - да) : '))
while question == 'y':
    if question == 'y': #создаем условие для ответа 'y'
        name_1 = str(input('Введите еще одно имя : ')) #запрашиваем еще одно имя
        counter += 1 #увеличиваем счетчик на еще одно имя
        print(name_1, 'has been invited')
        question = str(input('Хотите ли Вы пригласить кого-то еще(y/n) : '))
else:
    print('Количество приглашенных : ', counter)



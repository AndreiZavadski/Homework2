month = str(input('Введите название месяца'))
if month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
    print('31 день')
elif month == 'april' or month == 'june' or month == 'september' or month == 'november':
    print('30 дней')
elif month == 'february':
    print('Месяц может состоять как из 28, так и из 29 дней')
else:
    print('Неверный запрос')

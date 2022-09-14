invoice_amount = int(input('Введите общую сумму счета'))
number_of_participants = int(input('Введите общее количество участников'))
summer = invoice_amount / number_of_participants #Выясним сколько заплатит каждый участник
print(summer)
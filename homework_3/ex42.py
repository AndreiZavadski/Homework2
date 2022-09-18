estimation = str(input('Введите буквенную оценку:'))
if estimation == 'A+' or estimation == 'A':
    print(4.0)
elif estimation == 'A-':
    print(3.7)
elif estimation == 'B+':
    print(3.3)
elif estimation == 'B':
    print(3.0)
elif estimation == 'B-':
    print(2.7)
elif estimation == 'C+':
    print(2.3)
elif estimation == 'C':
    print(2.0)
elif estimation == 'C-':
    print(1.7)
elif estimation == 'D+':
    print(1.3)
elif estimation == 'D':
    print(1.0)
elif estimation == 'F':
    print(0)
else:
    print('неверный ввод')


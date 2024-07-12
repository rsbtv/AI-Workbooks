x = int(input('Введите x: '))
if x < -5:
    print('x принадлежит интервалу (-infinity, -5)')
elif -5 <= x <= 5:
    print('x принадлежит интервалу [-5, 5]')
else:
    print('x принадлежит интервалу (5, +infinity)')

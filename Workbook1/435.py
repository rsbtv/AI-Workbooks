from numpy import e, sin, cos

print("Список команд:\n"
      "1. Сложение\n"
      "2. Вычитание\n"
      "3. Умножение\n"
      "4. Деление\n"
      "5. e^(x+y)\n"
      "6. sin(x+y)\n"
      "7. cos(x+y)\n"
      "8. x^y\n"
      "9. Выход")
while True:
    cmd = int(input("Введите желаемую команду: "))
    if 0 < cmd <= 9:
        if cmd == 9:
            break
        elif cmd == 1:
            x = float(input("Введите 1-ое слагаемое: "))
            y = float(input("Введите 2-ое слагаемое: "))
            print(f"Результат: {x + y}")
        elif cmd == 2:
            x = float(input('Введите уменьшаемое: '))
            y = float(input('Введите вычитаемое: '))
            print(f"Результат: {x - y}")
        elif cmd == 3:
            x = float(input('Введите умножаемое: '))
            y = float(input('Введите множитель: '))
            print(f"Результат: {x * y}")
        elif cmd == 4:
            x = float(input('Введите делимое: '))
            y = float(input('Введите делитель: '))
            if y != 0:
                print(f"Результат: {x * y}")
                break
            else:
                print('Ошибка: делить на ноль нельзя')
        elif cmd == 5:
            x = float(input('Введите x: '))
            y = float(input('Введите y: '))
            print(f"Результат: {e ** (x + y)}")
        elif cmd == 6:
            x = float(input('Введите x: '))
            y = float(input('Введите y: '))
            print(f"Результат: {sin(x + y)}")
        elif cmd == 7:
            x = float(input('Введите x: '))
            y = float(input('Введите y: '))
            print(f"Результат: {cos(x + y)}")
        elif cmd == 8:
            x = float(input('Введите x: '))
            y = float(input('Введите y: '))
            print(f"Результат: {x ** y}")
    else:
        print("Введите команду корректно")

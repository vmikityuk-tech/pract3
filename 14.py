num = input('Введите число: ')
while True:
    if not(num.isdigit()):
        num = input('Ошибка. Попробуйте еще раз. Введите число: ')
    else:
        print(f'Введено целое число: {num}')
        break


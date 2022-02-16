

# Функции программы
# Функция преобразования чисел из различных систем счисления (пункты 1-3 задания)
def mode_1_fcn():
    print('Режим №1: Преобразования десятичных чисел в числа с различными базами.\n')
    number = int(input('Введите десятичное число для преобразования: '))
    base = str(input('Выберите базу для преобразования (b - двоичная, o - восьмеричная, h - шестнадцатиричная): '))

    if base == 'b':
        new_number = bin(number)
    elif base == 'o':
        new_number = oct(number)
    elif base == 'h':
        new_number = hex(number)
    else:
        print('Ошибка! Введена неверная база для преобразования!')
        return

    new_number = new_number[2:]

    print('Преобразованное число: ' + new_number)
    print()

    return


# Функция решения произвольных примеров (пункты 4-6 задания)
def mode_2_fcn():
    print('Режим №2: Расчет произвольных примеров с вводом чисел в различных системах счисления.\n')
    print('Ограничения:\n'
          '\t1. Допускается использование четырех основных действий - сложение, вычитание, умножение, деление;\n'
          '\t2. Допускается использование чисел из различных систем счисления.'
          '\t3. ОБЯЗАТЕЛЕН ВВОД ПРЕФИКСОВ ЧИСЕЛ (0b - двоичная, 0o - восьмеричная, 0x - шестнадцатиричная)!\n')

    solve = str(input('Введите пример: '))

    number = ''
    expression = list()
    for i in range(solve.__len__()):
        if solve[i] == '+' or solve[i] == '-' or solve[i] == '*' or solve[i] == '/' or solve[i] == '=':
            if number.__len__() == 1:
                number = '0' + number

            if number[1] == 'b':
                number = str(int(number, 2))
            elif number[1] == 'o':
                number = str(int(number, 8))
            elif number[1] == 'x':
                number = str(int(number, 16))
            else:
                number = str(int(number))

            expression.append(number)
            expression.append(solve[i])
            number = ''
        else:
            number = number + solve[i]

        if i == solve.__len__()-1:
            if number[1] == 'b':
                number = str(int(number, 2))
            elif number[1] == 'o':
                number = str(int(number, 8))
            elif number[1] == 'x':
                number = str(int(number, 16))
            else:
                number = str(int(number))

            expression.append(number)
            number = ''

    new_expression = ''
    for i in range(expression.__len__()):
        new_expression = new_expression + expression[i]

    result = eval(new_expression)

    print('\nРезультаты расчета:\n' + '\t' + solve + ' = ' + new_expression + ' = ' + str(result))
    print()

    return


# Функция запуска программы
def main():
    print('Режимы работы программы:\n'
          '\t1. Преобразование десятичного числа (п.1, п.2, п.3 ЛР):\n'
          '\t2. Выполнение арифметических примеров (п.4, п.5 ЛР):\n'
          )

    mode = int(input('Выберите режим работы: '))
    print('\n')

    if mode == 1:
        mode_1_fcn()
    elif mode == 2:
        mode_2_fcn()
    else:
        print('Ошибка! Введен неверный режим!')

    input('Работа программы завершена. Для выхода нажмите "Enter"...')


# Запуск потока приложения
if __name__ == '__main__':
    main()

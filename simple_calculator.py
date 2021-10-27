#simple calculator github
a = float(input('Введте вещественное число а'))
b = float(input('Введте вещественное число b'))
operand = input('''Введите операцию с числами (+, -, /, *, mod, pow, div), где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.''')

if (b == 0) and ((operand == 'mod') or (operand == 'div') or (operand == '/')):
    print('Деление на 0!')
else:
    if (operand == '+'):
        print(a + b)
    elif(operand == '-'):
        print(a - b)
    elif (operand == '*'):
        print(a * b)
    elif (operand == '/'):
        print(a / b)
    elif (operand == 'mod'):
        print(a % b)
    elif (operand == 'pow'):
        print(a ** b)
    elif (operand == 'div'):
        print(a // b)

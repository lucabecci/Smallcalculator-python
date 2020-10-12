
#Control del primer valor
first = input('input your first number:')
try:
    first = int(first)
except:
    first = 'error'
if first == 'error':
    print('YOUR FIRST VALUE IS NOT A NUMBER, TRY AGAIN WITH NUMBERS')
    exit()

#Control del segundo valor
second = input('input your second number:')
try:
    second = int(second)
except:
    second = 'error'
if second == 'error':
    print('YOUR SECOND VALUE IS NOT A NUMBER, TRY AGAIN WITH NUMBERS')
    exit()

#Control de la operacion
operation = input('Insert your operation: ')
#checkeando que operador es
if operation == '+':
    print('YOUR ADDED:', first + second)
    exit()
elif operation == '-':
    print('YOUR REST:', first - second)
    exit()
elif operation == '*':
    print('YOUR MULTIPLY:', first * second)
    exit()
elif operation == '/':
    print('YOUR DIVISION:', first / second)
    exit()
else: 
    print('ERROR, YOUR OPERATION SIMBOL IS INCORRECT')
    exit()


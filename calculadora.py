num = int(input('Digite um número: '))
op = str(input('Digite a operação: '))
if op == '+':
    for x in range(11):
        cal = num + x
        print('{} + {} = {}'.format(num, x, cal))

elif op == '-':
    for x in range(11):
        cal = num - x
        print('{} - {} = {}'.format(num, x, cal))

elif op == '*':
    for x in range(11):
        cal = num * x
        print('{} * {} = {}'.format(num, x, cal))

elif op == '/':
    for x in range(1, 11):
        cal = num / x
        print('{} / {} = {:.2f}'.format(num, x, cal))

else:
    print('Operação errada')








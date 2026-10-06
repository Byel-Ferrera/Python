#Calculadora

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

adi = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
divex = n1 // n2
res = n1 % n2

print('1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Potência')
ope = input('Escolha uma operação: ')

while ope not in ('1','2','3','4','5'):
    print('Digite um valor válido')
    ope = input('Escolha uma operação: ')

if ope == '1':
    print(f'O resultado da adição é {adi:g}')
elif ope == '2':
    print(f'O resultado da subtração é {sub:g}')
elif ope == '3':
    print(f'O resultado da multiplicação é {mul:g}')
elif ope == '4':
    print(f'O resultado da divisão é {div:.2f}, ou {divex:g} e seu resto é {res:g}')
elif ope == '5':
    print(f'O resultado da potência é {pot:g}')
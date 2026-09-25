'''
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite outro número:'))

if n1 > n2 and n3:
    print('O primeiro número ({}) é o maior!'.format(n1))
elif n2 > n1 and n3:
    print('O segundo número ({}) é o maior!'.format(n2))
else:
    print('O terceiro número ({}) é o maior!'.format(n3))


result = input('Digite um número:')
while result .isalpha(): 
    print ('tu é abestado é, faz direito!')
    result = input('Digite um número:')


senhacorreta = 'senha'
tentativas = 5

while tentativas > 0:
    senha = input('Digite dua senha:')

    if senha == senhacorreta:
        print('Acesso Liberado!')
        break
    else:
        tentativas -= 1
        print('Senha incorreta! Você ainda tem {} tentativa(s).'.format(tentativas))

if tentativas == 0:
    print ('Acesso Bloqueado.')

# f-string:
     serve pra deixar o código mais mais limpo, e funciona igual o .format
     ex:

     print(f'A soma vale {variável}')

# :.2f:
    pra definir quantas casas decimais eu quero que apareça
    ex:

    print(f'A nota é {variável:.2f}')

'''
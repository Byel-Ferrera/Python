#Cardápio de restaurante

print('Olá! Bem-Vindo(a) ao nosso cardápio digital!\nAtualmente estamos servindo:')
print('-----Cardápio-----\n1- Hambúrguer.\n2- Pizza.\n3- Cachorro quente.\n4- Macarronada.\n5- Panquecas.')

pedido = input('O que deseja? ')

if pedido == '1':
    print('Ótima escolha!')
    pedido = 'Hambúrguer' # pedi ajuda pra fazer essas conversões (não sabia como fazer)

elif pedido == '2':
    print('Ótima escolha!')
    pedido = 'Pizza'

elif pedido == '3':
    print('Ótima escolha!')
    pedido = 'Cachorro-quente'

elif pedido == '4':
    print('Ótima escolha!')
    pedido = 'Macarronada'

elif pedido == '5':
    print('Ótima escolha!')
    pedido = 'Panquecas'

else:
    
    while pedido not in 'Hambúrguer, hambúrguer, Hamburguer, hamburguer, Pizza, pizza, Cachorro quente, cachorro quente, Cachorro-quente, cachorro-quente, Macarronada, macarronada, Panquecas, panquecas':
        print ('Pedido inválido!')
        pedido = input('O que deseja? ')

bebida = input('(Digite sim ou não)\nGostaria de uma bebida? ')

if bebida in ['Sim', 'sim', 'ss', 'yes', 's', 'si', 'sm', 'SS', 'SIM', 'S']:
    print ('Nossas opções de bebida são:')
    print ('1-Suco\n2-Refrigerante\n3-Água.')
    escolha = input('Do que gostaria? ')

    if escolha == '1':
        print (f'{pedido} com suco... Boa escolha!')
    elif escolha == '2':
        print (f'{pedido} com refrigerante... Boa escolha!')
    elif escolha == '3':
        print (f'{pedido} com água... Boa escolha!')
    else:
            while escolha not in ('1','2','3'):
                print ('Por favor, digite um valor válido!')
                escolha = input('Do que gostaria? ')

    print('Ok, seu pedido ficará pronto dentro de alguns minutos. Agradecemos pela preferência!')
    
else:
    print('Ok, seu pedido ficará pronto dentro de alguns minutos. Agradecemos pela preferência!')

#--------------RELATÓRIO---------------
'''
A maior parte foi desenvolvida por mim, só pedi ajuda do chat
pra algumas pequenas coisas, como a conversão do número pro produto
saber se podia colocar if dentro de if e o uso do 'in' e 'not in'.
'''
'''

print('Hello, World!')

nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
dia = input('Digite o dia do seu nascimento:')
mes = input('Digite o mês do seu nascimento:')
ano = input('Digite o ano do seu nascimento:')

print('Olá {}! Fiquei sabendo que você tem {} anos, é verdade? Então deve ter nascido dia {} de {} de {}. Correto?'.format(nome, idade, dia, mes, ano))

Aluno = input('Digite o nome do aluno:')
Nota = float(input('Digite a nota do aluno:'))

if Nota >= 7:
    print('{} está aprovado!'.format(Aluno))
else:
    print('Infelizmente {} está reprovado!'.format(Aluno))

LimiteVelocidade = 60
VelocidadeVeiculo = 30

if VelocidadeVeiculo > LimiteVelocidade:
    print('Sua velocidade ultrapassou o limite permitido. Você será multado!')
else:
    print('Continue seguindo!')

'''
'''
#EXERCÍCIOS

#Exercício 1

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))

if idade >= 18:
    print('{}, você é maior de idade!'.format(nome))
else:
    print('{}, você é menor de idade!'.format (nome))



#Exercício 2

aluno = input('Digite o nome do aluno:')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))
nota4 = float(input('Digite a quarta nota:'))

mediafinal = (nota1 + nota2 + nota3 + nota4) / 4

if mediafinal >= 7:
    print('Parabéns {}! Você tirou {} e está aprovado!'.format (aluno,mediafinal))
else:
    print('Sinto muito {}... Você tirou {} e está reprovado...'.format (aluno,mediafinal))


#Exercício 3

limite = 60
velocidade = int(input('Digite a velocidade do veículo:'))
diferenca = velocidade - limite

if velocidade > limite:
    print('Você foi multado! Ultrapassou {}km/h do limite permitido.'.format(diferenca))
else:
    print('Velocidade permitida.')

#Exercício 4 (precisei de ajuda)

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

soma = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

escolha = input ('Escolha uma operação:')

if escolha == '1':
    print (soma)
elif escolha == '2':
    print (subtração)
elif escolha == '3':
    print (multiplicação)
elif escolha == '4':
    print (divisão)

#Exercício 5

nome = input('Nome do produto:')
preço = int(input('Preço do produto:'))
saldo = int(input('Quanto dinheiro o cliente tem?'))
contaboa = saldo - preço
contaruim = preço - saldo

if saldo == preço:
    print('Compra aprovada!')
if saldo > preço:
    print('Compra aprovada! Seu troco é de R$ {}'.format(contaboa))
if saldo < preço:
    print('Saldo insuficiente! Faltam R$ {}.'.format(contaruim))

'''

# Exercício 6 (está errado, ainda não corrigi)

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura:'))

if idade >= 12 and altura >= 1.40:
    print('{}, você pode entrar no briquedo!'.format(nome))
else:
    print('{}, Você não pode entrar no brinquedo...'.format(nome))
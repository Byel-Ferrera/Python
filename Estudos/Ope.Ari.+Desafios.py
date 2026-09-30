# AULA 07 DE PYTHON CURSO EM VIDEO 
#OPERADORES ARITMETICOS

'''
5+2 == 7
5-2== 2
5*2== 10
5/2== 2.5
5**2== 25
5//2== 2
5%2== 1


#------------DESAFIO N° 5---------------
#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número:'))

sucessor = numero + 1
antecessor = numero - 1

print (f'O número escolhido é {numero}, seu sucessor é {sucessor}, e seu antecessor é {antecessor}.')

#------------DESAFIO N° 6---------------
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número:'))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

print (f'Dobro: {dobro} | Triplo {triplo} | Raiz Quadrada {raiz}.')

#------------DESAFIO N° 7---------------
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2

print(f'Sua média é: {media}')

#---------------Desafio N° 8----------------
#Digitar um valor e mostrar ele convertido em centímetro e milímetro.

metro = int(input('Digite o valor:'))

centimetro = metro * 100
milimetro = metro * 1000

print(f'Em metros: {metro} m \nEm centrímetros: {centimetro} cm \nEm milimetro {milimetro} mm.')

#---------------Desafio N° 9----------------
#Ler um número inteiro qualquer e mostrar na tela a sua tabuada (fazer com as ferramentas que tenho agora).

numero = int(input('Digite um número:'))

tabuada1 = numero * 1 
tabuada2 = numero * 2
tabuada3 = numero * 3 
tabuada4 = numero * 4 
tabuada5 = numero * 5 
tabuada6 = numero * 6 
tabuada7 = numero * 7 
tabuada8 = numero * 8 
tabuada9 = numero * 9 
tabuada10 = numero * 10 

print(f'{numero} x 1 = {tabuada1} \n{numero} x 2 = {tabuada2} \n{numero} x 3 = {tabuada3} \n{numero} x 4 = {tabuada4} \n{numero} x 5 = {tabuada5} \n{numero} x 6 = {tabuada6} \n{numero} x 7 = {tabuada7} \n{numero} x 8 = {tabuada8} \n{numero} x 9 = {tabuada9} \n{numero} x 10 = {tabuada10}

#---------------Desafio N° 10----------------
#Ler quanto dinheiro (em reais) a pessoa tem, e mostrar quantos dólares ela pode comprar. (Considere: US$1,00 = R$3,27)

tem = float(input('Quanto dinheiro você tem? R$'))

if tem >= 3.27:
    calculo = tem / 3.27
    print (f'Você pode comprar {calculo:.2f} dólares!')
else:
    print('Pobre kkkk')
'''
#---------------Desafio N° 11----------------
#Ler a altura e largura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área
#de 2 m2
'''
L = float(input('Digite a largura: '))
H = float(input('Digite a altura: '))

area = L * H
litros = area / 2

print(f'A área é de {area:g} m², e você precisa de {litros:g} para pintá-lo.')
'''
#---------------Desafio 12----------------
#Ler o preço de um produto e mostrar o novo preço com 5% de desconto.
'''
preco = float(input('Digite o preço do produto: '))

desconto = preco * 0.05
valor = preco - desconto

print(f'O valor do produto é de R$ {preco:.2f}, mas com o desconto fica por {valor:.2f}.')
'''
#---------------Desafio 13----------------
#Ler o salário de um funcionário e mostrar o novo salário, com 15% de aumento.
'''
salario = input('Digite seu salário: ')
while ',' in salario:
    print ('Utilize ponto no lugar da vírgula.')
    salario = input('Digite seu salário: ')

salario = float(salario)

aumento = salario * 0.15 #(corrigi com o chat, tinha colocado pra dividir)
valor = salario + aumento

print(f'Com o aumento, seu salário de R$ {salario:.2f}, irá para {valor:.2f}.')
'''

#---------------Desafio 14----------------
#Converter celsius pra farenheit
'''
c = float(input('Informe a temperatura em °C: '))
f = ((9*c)/5)+32

print(f'A temperatura de {c} °C, corresponde a {f} °F.')
'''

#---------------Desafio 15----------------
#Quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar sabendo que o carro custa 60 reais por dia e 0,15 por km rodado.
'''
km = float(input('Quantos km o carro percorreu? '))

dias = int(input('Por quantos dias o carro foi alugado? '))

precokm = 0.15
precodia = 60

calculo1 = km * precokm
calculo2 = dias * precodia
final = calculo1 + calculo2

print(f'Obrigado por utilizar nossos serviços! Vimos que seu aluguel durou {dias} dias, e percorreu {km} km.')

print(f'Nossos valores são:\n{precokm} centavos por km\n{precodia} a diária')

print(f'O total a pagar é de R${final}')
'''


#-------------------------------------------DESAFIO À PARTE (eu propus e fiz)-----------------------------------------------------------
#CRIAR UMA CALCULADORA
'''
n1 = input('Digite um número: ')

while ',' in n1:
    print('Por favor, use ponto (.) no lugar de vírgula (,).')
    n1 = input('Digite um número: ')

n1 = float(n1)

n2 = input('Digite outro número: ')

while ',' in n2:
    print('Por favor, use ponto (.) no lugar de vírgula (,).')
    n2 = input('Digite outro número: ')

n2 = float(n2)    

op = input(' 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n Escolha uma operação: ')

adição = n1 + n2
subtração = n1 - n2
multiplicação = n1 * n2
divisão = n1 / n2

while op not in ('1', '2', '3', '4'):
    print ('Digite um valor válido!')
    op = input('Escolha uma operção: ')

if op == '1':
    print (f'O resultado é: {adição:g}')
elif op == '2':
    print (f'O resultado é: {subtração:g}')
elif op == '3':
    print (f'O resultado é: {multiplicação:g}')
else:
    print (f'O resultado é: {divisão:g}')
'''
#Relatório:
'''
Consegui desenvolver a calculadora com uma certa facilidade e sem ajuda.
Mas algumas coisas que eu quis aperfeiçoar, eu pesquisei.
Coisas como :g, f-string (entender o conceito pra usar), \n eu já sabia, mas n lembrava,
in e not in no while; todas foram pesquisadas. Mas o desafio em si, foi concluído sem ajuda.
'''
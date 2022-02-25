#Jogo Sorteador de Numeros Generico (mega sena, quina, lotomania,...)
from random import randint
sorteados = []
contador = 0
num1 = int(input('Quantos numeros voce quer sortear?')) #num1 é o numero de quantos numeros voce querem que sorteassem
num2 = int(input('Quantos numeros tem no jogo?')) #num2 é o numero de quantos numeros tem ate o sorteo
while contador < num1:
    numero = randint(1,num2)
    if numero not in sorteados:
        sorteados.append(numero)
        print (numero)
        contador = contador + 1


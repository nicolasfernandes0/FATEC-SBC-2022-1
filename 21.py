import requests 
#Bot jogador de 21
#Pede um baralho
import random
fator_de_seguranca = random.randint(0,4)
resposta = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
deck_id = resposta.json()["deck_id"]
mao = 0
tabela_conversao = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
                   '8':8, '9':9, 'ACE':1, 'QUEEN':10,
                   'KING':10, 'JACK':10, '10':10}
while mao < (21 - fator_de_seguranca):
  resposta = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1')
  valor = resposta.json()['cards'][0]['value']
  mao = mao + tabela_conversao[valor]
  print('Carta Sorteada:', valor)
  print('Total da Mao:', mao)
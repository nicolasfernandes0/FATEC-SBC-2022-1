import requests
url = 'https://viacep.com.br/ws/09668010/json'
resposta = requests.get(url)
print('Código de Resposta:', resposta.status_code)
dados = resposta.json()
print('Nome da rua:', dados["logradouro"])
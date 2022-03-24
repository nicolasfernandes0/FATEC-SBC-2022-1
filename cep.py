import requests
url = 'https://viacep.com.br/ws/09051110/json'
resposta = requests.get(url)
print(resposta.text)

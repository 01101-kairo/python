import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)
# print(req.status_code)

dd = req.json()
# print(dd)
valor = float(input('informe valor:\n'))
cotacao = dd['rates']['BRL']
print(f'R${valor} em dola U${(valor/cotacao):.2f}')


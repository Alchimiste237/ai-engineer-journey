import requests

print(f" {"==" * 20} Currency Converter {"==" * 20} ")

amount = float(input("Enter amount: "))
base_code = input('From: ')
code = input('To: ')

url = f"https://open.er-api.com/v6/latest/{base_code.upper()}"
reponse = requests.get(url)
exchange_rate = reponse.json()

print(f" {amount} {base_code} is equivalent to {amount * exchange_rate['rates'][code.upper()] } {code} ")
# https://codeshare.io/j0l0lL
import requests

def change (curr1, amount, curr2):
    curr1 = curr1.upper()
    curr2 = curr2.upper()
    rates = requests.get("https://open.er-api.com/v6/latest/USD").json()["rates"]
    res = amount / rates[curr1] * rates[curr2]
    return res

print("100 USD ->", change("USD", 100, "RUB"), "RUB")
print("100 RUB ->", change("RUB", 100, "EUR"), "EUR")
print("100 EUR ->", change("EUR", 100, "USD"), "USD")
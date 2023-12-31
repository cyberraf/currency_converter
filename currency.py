import requests

API_KEY = 'fca_live_mVTsWR91U85812hNhHKK3OZ4FLVbWgYj0UTaBWvi'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "CAD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        #print(data)
        return data["data"]
    except Exception as e:
        print(str(e))
        return None
    
base = input("Enter the base currency (e.g. USD) or 'q' to quit: ").upper()

data = convert_currency(str(base)).strip
del data[base]

for currency, value in data.items():
    print(f"{currency}: {value}")
    
    #this is a comment test for grafana
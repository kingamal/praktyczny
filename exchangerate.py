from requests import get

code = input("What value do you choose: EUR, USD, CHF. Write it now: ") #other params ["USD", "EUR", "CHF"]
date = "2021-12-15" #change the date

url = f'http://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/'

resp = get(url)
data = resp.json()
currency = data['rates'][0]['mid']

# print(currency)

exchange_rate = "1 {} = {} PLN w dniu {}".format(
                                            data['code'],
                                            currency,
                                            data['rates'][0]['effectiveDate']
                                            )

print(exchange_rate)

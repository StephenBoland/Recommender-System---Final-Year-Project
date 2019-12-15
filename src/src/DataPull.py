import requests


response = requests.get('https://sandbox-api.brewerydb.com/v2/brewery/HaPdSL/beers?key=e39394ae5cad440bca7500ca5281a447')
beerdata = response.json()
print(beerdata)

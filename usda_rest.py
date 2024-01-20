import requests

API_KEY = open("API_KEY", 'r').read().rstrip()

api_url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query=Cheddar%20Cheese"
response = requests.get(api_url)
print(response.json())

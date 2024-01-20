import requests
import pandas as pd

API_KEY = open("API_KEY", 'r').read().rstrip()

api_url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query=Raw%20Broccoli"
api_url_list = f"https://api.nal.usda.gov/fdc/v1/foods/list?api_key={API_KEY}"
#print(api_url)
response = requests.get(api_url)
response_list = requests.get(api_url_list)
print(len(response_list.json()))

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(pd.DataFrame(response_list.json()))

#print(response.json())
#print(response_list.json())


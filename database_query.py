import noms

API_KEY = open("API_KEY", 'r').read()

usda_client = noms.Client(API_KEY)
print(usda_client)
search_results = usda_client.search_query("Raw Broccoli")
print(search_results)

print('Hello Nutrition Tracker')

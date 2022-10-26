# Import the modules
import requests
import json
import GetYelpApi


# Define a business ID
business_id = '4AErMBEoNzbk7Q8g45kKaQ'
unix_time = 1546047836

# Define my API Key, My Endpoint, and My Header
API_KEY = GetYelpApi.api_key
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}
PARAMETERS = {'location':'San Diego',
              'limit': 5}

# Make a request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

# Convert the JSON String
business_data = response.json()

# Convert the JSON String to a python object
business_data2 = json.loads((json.dumps(business_data)))

# print the response
#print(json.dumps(business_data, indent = 3))
filtered_urls = []
filtered_names = []


for biz in business_data['businesses']:
    filtered_urls.append(biz['url'])
    filtered_names.append(biz['name'])

print(*filtered_urls, sep = '\n')


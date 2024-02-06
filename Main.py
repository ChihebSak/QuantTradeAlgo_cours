import requests
from secrets_1 import API_URL

symbol = "AAPL"
api_url = API_URL
data = requests.get(api_url).json();
print(data)

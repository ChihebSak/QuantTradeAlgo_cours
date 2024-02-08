import requests
import secrets_1

symbol = "aapl"
parameters = {
"" : "/core",
"" : symbol
    }

api_url = secrets_1.construct_url(**parameters)
print(api_url)
data = requests.get(api_url).json();
print(data)

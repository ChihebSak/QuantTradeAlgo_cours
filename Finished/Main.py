import requests
import secrets_1

# Get the directory of the current script
# current_directory = os.path.dirname(__file__)

# Concatenate the directory and filename
# file_path = os.path.join(current_directory, "stock_info.csv")

# stocks = pd.read_csv(file_path)

parameters = {
"function" : "TIME_SERIES_INTRADAY",
"symbol" : "IBM",
"interval" : "30min",
"outputsize" : "full"
}

api_url = secrets_1.construct_url(**parameters)
data = requests.get(api_url).json( );


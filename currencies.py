import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_currency_rate(base: str, target: str) -> float:
    api_key = os.getenv('API_KEY')

    url = f"https://api.currencyapi.com/v3/latest?apikey={api_key}&currencies={target}&base_currency={base}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['data'][target]['value']
    except Exception as e:
        print(f"Error fetching currency rate of: {e}")
        return 1.0
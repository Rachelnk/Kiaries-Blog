import requests as requests, json

API = "http://quotes.stormconsultancy.co.uk/random.json"

def get_random_quote():
    '''
    Function to return a Blog post class instance
    '''
    response = requests.get(API)
    if response.status_code == 200:
        quote = response.json()
        return quote


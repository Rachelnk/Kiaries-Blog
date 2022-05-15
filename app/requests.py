import requests as requests, json
from pprint import pprint

API = "http://quotes.stormconsultancy.co.uk/random.json"
class Quote(object):
  def __init__(self, quote, permalink, author, **kwargs):
    self.quote =quote
    self.author = author
    self.permalink=permalink
      
    
def get_random_quote():
  '''
  Method that calls a randomm API endpoint 
  and returns a random quote.
  '''
  response = requests.get(API)
  data = response.json()
  quote = (Quote(**data)) 
  print(quote)
# def __str__(self):
#   return self.author

if __name__ == '_main__':
  get_random_quote()
   
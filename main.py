from flask import Flask, jsonify

from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  
  return rate


app = Flask(__name__)
@app.route('/')

def home():
  return '<h1>currency rate: </h1> <p>example url: /api/v1/usd-eur</p>'

@app.route('/api/v1/<cur1>-<cur2>')

def api(cur1, cur2):
  rate = get_currency(cur1,cur2)
  result_dict = {'input_currency' : cur1 ,'output_currency' : cur2, 'rate' : rate}
  return jsonify(result_dict)


app.run(host = '0.0.0.0')
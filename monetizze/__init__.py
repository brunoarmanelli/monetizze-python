import requests

class Monetizze:
	def __init__(self, key):
		self.key = key

	def get_token(self):
		method_url = 'https://api.monetizze.com.br/2.1/token'
		headers = {'X_CONSUMER_KEY': self.key}

		try:
			r = requests.get(url = method_url, headers = headers)
			data = r.json()
			return data['token']
		except: 
			return None

		
	def get_transactions(self, product=None, transaction=None, email=None, date_min=None, 
			date_max=None, end_date_min=None, end_date_max=None, status=None, 
			forma_pagamento=None, page=None):

		method_url = 'https://api.monetizze.com.br/2.1/transactions'
		headers = {'TOKEN': self.get_token()}
		payload = {}
		
		if product:
			payload['product'] = product
		if transaction:
			payload['transaction'] = transaction
		if email:
			payload['email'] = email
		if date_min:
			payload['date_min'] = date_min
		if date_max:
			payload['date_max'] = date_max
		if end_date_min:
			payload['end_date_min'] = end_date_min
		if end_date_max:
			payload['end_date_max'] = end_date_max
		if status:
			payload['status'] = status
		if forma_pagamento:
			payload['forma_pagamento'] = forma_pagamento
		if page:
			payload['page'] = page
		
		try:
			r = requests.get(url = method_url, headers = headers, params = payload)
			data = r.json()
			return data
		except: 
			return None
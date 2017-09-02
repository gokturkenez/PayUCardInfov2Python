'''
Project: PayU Turkey Card Info v2 Python3 Sample Code
Author: Göktürk Enez
'''
from datetime import datetime
import hmac
import hashlib
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Endpoint
url = 'https://secure.payu.com.tr/api/card-info/v2/'

# PayU Merchant's Secret Key
secret = 'SECRET_KEY'

# Request @params Begin
array = {
    # PayU Merchant's Merchant ID
    'merchant': 'OPU_TEST',
    'extraInfo': 'true',
	'dateTime': datetime.utcnow().strftime('%Y-%m-%dT%X+00:00'),
	'cc_cvv': '000',
	'cc_owner': 'Göktürk Enez',
	'exp_year': '2018',
	'exp_month': '12',
	'cc_number': '4355084355084358',
}
# Initializing the hashstring @param
hashstring = ''

# Sorting Array @params
for k, v in sorted(array.items()):

# Adding the UTF-8 byte length of each field value at the beginning of field value
    hashstring += str(len(v.encode('UTF-8'))) + str(v)
print(hashstring)

# Calculating signature
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.sha256).hexdigest()

# Adding signature @param to request array
array['signature'] = signature

print(signature)

# Sending Request to Endpoint
request = Request(url, urlencode(array).encode())
response = urlopen(request).read().decode()

# Printing result/response
print(response)


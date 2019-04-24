from alpha_vantage.cryptocurrencies import CryptoCurrencies
import time as timer
import socket, requests, lxml
from bs4 import BeautifulSoup
from random import randint
'''
#### CryptoCurrencies Methods:																####
#### get_digital_currency_intraday, 														####
#### get_digital_currency_daily, 															####
#### get_digital_currency_weekly,															####
#### nget_digital_currency_monthly															####
'''

def isBehindFirewall():
	host_name = socket.gethostname()
	host_ip = "-"+socket.gethostbyname(host_name)
	#-test line#print(host_ip)
	if host_ip.find("-10.") > -1:
		return True
	return False

class AlphaInputs():
	link_symbols_crypto = "https://www.alphavantage.co/digital_currency_list/"
	link_markets_crypto = "https://www.alphavantage.co/physical_currency_list/"

	def get_crypto_symbols(self):
		if isBehindFirewall():
			proxies = {
			'http' : 'http://proxy-us.intel.com:911',
			'https' : 'https://proxy-us.intel.com:912',
			}
			r = requests.get(self.link_symbols_crypto,"lxml", proxies=proxies)
		else:
			r = requests.get(self.link_symbols_crypto,"lxml")
		
		soup = BeautifulSoup(r.content).get_text()
		soup = soup.split("\r\n")
		soup.pop(0)
		soup.pop(len(soup)-1)
		out_array = []
		for s in soup:
			#s = s.split(",")
			#out_array.append(s[0])
			s = s.replace(","," : ")
			out_array.append(s)
		return out_array
		#print(out_array)
	def get_crypto_markets(self):
		r = requests.get(self.link_markets_crypto,"lxml")
		soup = BeautifulSoup(r.content).get_text()
		soup = soup.split("\r\n")
		soup.pop(0)
		soup.pop(len(soup)-1)
		out_array = []
		for s in soup:
			#s = s.split(",")
			#out_array.append(s[0])
			s = s.replace(","," : ")
			out_array.append(s)
		return out_array
		#print(out_array)

class Crypto_Generate():

	#~~generates a random api key each time a call is made. The key is not specific, but a current theory is
	#~~too many requests from the same dummykey msy cause issues
	api_key = str(randint(0,320000))
	#~~The CryptoCurrency class takes a minimum of one argument (the api key), but the retry count can be added
	#~~as well. This was added to avoid retrying failed attempts as it caused known good requests to fail directly
	#~~afterwards. 
	crypto = CryptoCurrencies(api_key,0)
	if isBehindFirewall():
		proxies = {
		'http' : 'http://proxy-us.intel.com:911',
		'https' : 'https://proxy-us.intel.com:912',
		}
		crypto.set_proxy(proxies)
	market = "JPY"

	def get_daily(self,symbol,market):
		#-test line#bitcoin_in_usd, meta = self.crypto.get_digital_currency_daily(self.top_ten_crypto[0],self.market)
		#-test line#print("before")
		try:
			#~~The symbol is just the abbreviation of the stock or cryptocurrency type (i.e. Bitcoin = BTC)
			bitcoin_in_usd, meta = self.crypto.get_digital_currency_daily(symbol,market)
		except Exception:
			#~~If an error occurs with the request, all expected return values will be empty (null)
			#-test line#print("`````the error has triggered")
			row_vals = {
			"symbol" : "",
			"name" : "",
			"day_high" : "",			
			"day_low" : "",
			"open_rate" : "",
			"close_rate" : "",
			"change_percentage" : "",
			}
			#-test line#print(f"````the vals:\n{row_vals}")
			return row_vals			
		#-test line#print("after")
		#-test line#print(f"meta - \n{meta}")
		'''
		data:
		{
		'1a. open (JPY)': '591890.67135450', '1b. open (USD)': '5288.51355403', 
		'2a. high (JPY)': '600163.89705459', '2b. high (USD)': '5362.43441200', 
		'3a. low (JPY)': '591313.52667882', '3b. low (USD)': '5283.35679521', 
		'4a. close (JPY)': '596717.82148429', '4b. close (USD)': '5331.64389909', 
		'5. volume': '5486.20139764', 
		'6. market cap (USD)': '29250472.21089060'
		}
		'''

		'''
		meta:
		{
		'1. Information': 'Daily Prices and Volumes for Digital Currency', 
		'2. Digital Currency Code': 'BTC', 
		'3. Digital Currency Name': 'Bitcoin', 
		'4. Market Code': 'USD', 
		'5. Market Name': 'United States Dollar', 
		'6. Last Refreshed': '2019-04-19 (end of day)', 
		'7. Time Zone': 'UTC'
		}
		'''
		bitcoin_in_usd_KEYS = []
		for key in bitcoin_in_usd.keys(): 
			bitcoin_in_usd_KEYS.append(key)

		#-test line#print(bitcoin_in_usd[bitcoin_in_usd_KEYS[0]])
		#-test line#symbol = self.top_ten_crypto[0]
		name = meta['3. Digital Currency Name']
		open_rate = float(bitcoin_in_usd[bitcoin_in_usd_KEYS[0]][f"1a. open ({market})"])
		close_rate = float(bitcoin_in_usd[bitcoin_in_usd_KEYS[0]][f"4a. close ({market})"])
		day_high = float(bitcoin_in_usd[bitcoin_in_usd_KEYS[0]][f"2a. high ({market})"])
		day_low = float(bitcoin_in_usd[bitcoin_in_usd_KEYS[0]][f"3a. low ({market})"])
		change_percentage = ((close_rate - open_rate) / open_rate) * 100

		# for some reason, a for loop doesn't succesfully round the values,
		# so it is done below
		day_high = round(day_high,2)
		day_low = round(day_low,2)
		close_rate = round(close_rate,2)
		open_rate = round(open_rate,2)
		change_percentage = round(change_percentage,2)

		row_vals = {
		"symbol" : symbol,
		"name" : name,
		"day_high" : f'{day_high} {market}',
		"day_low" : f'{day_low} {market}',
		"open_rate" : f'{open_rate} {market}',
		"close_rate" : f'{close_rate} {market}',
		"change_percentage" : f'{change_percentage} %',
		}
		#-test line#print(f"````the vals:\n{row_vals}")
		return row_vals


#-test line#c = Crypto_Generate()
#-test line#print(c.get_daily("BTC","USD"))

#-test line#alphainputs = AlphaInputs()
#-test line#alphainputs.get_crypto_symbols() 
#-test line#alphainputs.get_crypto_markets() 
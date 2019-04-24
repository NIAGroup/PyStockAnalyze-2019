from alpha_vantage.cryptocurrencies import CryptoCurrencies
import time as timer
from random import randint
'''
#### CryptoCurrencies Methods:																####
#### get_digital_currency_intraday, 														####
#### get_digital_currency_daily, 															####
#### get_digital_currency_weekly,															####
#### nget_digital_currency_monthly															####
'''

class Crypto_Generate():

	def isBehindFirewall():
		host_name = socket.gethostname()
		host_ip = "-"+socket.gethostbyname(host_name)
		#-test line#print(host_ip)
		if host_ip.find("-10.") > -1:
			return True
		return False
	markets = [ ["AED", "United Arab Emirates Dirham"], ["AFN", "Afghan Afghani"], ["ALL", "Albanian Lek"], ["AMD", "Armenian Dram"], 
	["ANG", "Netherlands Antillean Guilder"], ["AOA", "Angolan Kwanza"], ["ARS", "Argentine Peso"], ["AUD", "Australian Dollar"], 
	["AWG", "Aruban Florin"], ["AZN", "Azerbaijani Manat"], ["BAM", "Bosnia-Herzegovina Convertible Mark"], ["BBD", "Barbadian Dollar"], 
	["BDT", "Bangladeshi Taka"], ["BGN", "Bulgarian Lev"], ["BHD", "Bahraini Dinar"], ["BIF", "Burundian Franc"], 
	["BMD", "Bermudan Dollar"], ["BND", "Brunei Dollar"], ["BOB", "Bolivian Boliviano"], ["BRL", "Brazilian Real"], 
	["BSD", "Bahamian Dollar"], ["BTN", "Bhutanese Ngultrum"], ["BWP", "Botswanan Pula"], ["BZD", "Belize Dollar"], 
	["CAD", "Canadian Dollar"], ["CDF", "Congolese Franc"], ["CHF", "Swiss Franc"], ["CLF", "Chilean Unit of Account UF"], 
	["CLP", "Chilean Peso"], ["CNH", "Chinese Yuan Offshore"], ["CNY", "Chinese Yuan"], ["COP", "Colombian Peso"], 
	["CUP", "Cuban Peso"], ["CVE", "Cape Verdean Escudo"], ["CZK", "Czech Republic Koruna"], ["DJF", "Djiboutian Franc"], 
	["DKK", "Danish Krone"], ["DOP", "Dominican Peso"], ["DZD", "Algerian Dinar"], ["EGP", "Egyptian Pound"], 
	["ERN", "Eritrean Nakfa"], ["ETB", "Ethiopian Birr"], ["EUR", "Euro"], ["FJD", "Fijian Dollar"], 
	["FKP", "Falkland Islands Pound"], ["GBP", "British Pound Sterling"], ["GEL", "Georgian Lari"], ["GHS", "Ghanaian Cedi"], 
	["GIP", "Gibraltar Pound"], ["GMD", "Gambian Dalasi"], ["GNF", "Guinean Franc"], ["GTQ", "Guatemalan Quetzal"], 
	["GYD", "Guyanaese Dollar"], ["HKD", "Hong Kong Dollar"], ["HNL", "Honduran Lempira"], ["HRK", "Croatian Kuna"], 
	["HTG", "Haitian Gourde"], ["HUF", "Hungarian Forint"], ["IDR", "Indonesian Rupiah"], ["ILS", "Israeli New Sheqel"], 
	["INR", "Indian Rupee"], ["IQD", "Iraqi Dinar"], ["IRR", "Iranian Rial"], ["ISK", "Icelandic Krona"], 
	["JEP", "Jersey Pound"], ["JMD", "Jamaican Dollar"], ["JOD", "Jordanian Dinar"], ["JPY", "Japanese Yen"], 
	["KES", "Kenyan Shilling"], ["KGS", "Kyrgystani Som"], ["KHR", "Cambodian Riel"], ["KMF", "Comorian Franc"], 
	["KPW", "North Korean Won"], ["KRW", "South Korean Won"], ["KWD", "Kuwaiti Dinar"], ["KYD", "Cayman Islands Dollar"], 
	["KZT", "Kazakhstani Tenge"], ["LAK", "Laotian Kip"], ["LBP", "Lebanese Pound"], ["LKR", "Sri Lankan Rupee"], 
	["LRD", "Liberian Dollar"], ["LSL", "Lesotho Loti"], ["LYD", "Libyan Dinar"], ["MAD", "Moroccan Dirham"], 
	["MDL", "Moldovan Leu"], ["MGA", "Malagasy Ariary"], ["MKD", "Macedonian Denar"], ["MMK", "Myanma Kyat"], 
	["MNT", "Mongolian Tugrik"], ["MOP", "Macanese Pataca"], ["MRO", "Mauritanian Ouguiya (pre-2018)"], ["MRU", "Mauritanian Ouguiya"], 
	["MUR", "Mauritian Rupee"], ["MVR", "Maldivian Rufiyaa"], ["MWK", "Malawian Kwacha"], ["MXN", "Mexican Peso"], 
	["MYR", "Malaysian Ringgit"], ["MZN", "Mozambican Metical"], ["NAD", "Namibian Dollar"], ["NGN", "Nigerian Naira"], 
	["NOK", "Norwegian Krone"], ["NPR", "Nepalese Rupee"], ["NZD", "New Zealand Dollar"], ["OMR", "Omani Rial"], 
	["PAB", "Panamanian Balboa"], ["PEN", "Peruvian Nuevo Sol"], ["PGK", "Papua New Guinean Kina"], ["PHP", "Philippine Peso"], 
	["PKR", "Pakistani Rupee"], ["PLN", "Polish Zloty"], ["PYG", "Paraguayan Guarani"], ["QAR", "Qatari Rial"], 
	["RON", "Romanian Leu"], ["RSD", "Serbian Dinar"], ["RUB", "Russian Ruble"], ["RUR", "Old Russian Ruble"], 
	["RWF", "Rwandan Franc"], ["SAR", "Saudi Riyal"], ["SBDf", "Solomon Islands Dollar"], ["SCR", "Seychellois Rupee"], 
	["SDG", "Sudanese Pound"], ["SEK", "Swedish Krona"], ["SGD", "Singapore Dollar"], ["SHP", "Saint Helena Pound"], 
	["SLL", "Sierra Leonean Leone"], ["SOS", "Somali Shilling"], ["SRD", "Surinamese Dollar"], ["SYP", "Syrian Pound"], 
	["SZL", "Swazi Lilangeni"], ["THB", "Thai Baht"], ["TJS", "Tajikistani Somoni"], ["TMT", "Turkmenistani Manat"], 
	["TND", "Tunisian Dinar"], ["TOP", "Tongan Pa'anga"], ["TRY", "Turkish Lira"], ["TTD", "Trinidad and Tobago Dollar"], 
	["TWD", "New Taiwan Dollar"], ["TZS", "Tanzanian Shilling"], ["UAH", "Ukrainian Hryvnia"], ["UGX", "Ugandan Shilling"], 
	["USD", "United States Dollar"], ["UYU", "Uruguayan Peso"], ["UZS", "Uzbekistan Som"], ["VND", "Vietnamese Dong"], 
	["VUV", "Vanuatu Vatu"], ["WST", "Samoan Tala"], ["XAF", "CFA Franc BEAC"], ["XAG", "Silver Ounce"], 
	["XCD", "East Caribbean Dollar"], ["XDR", "Special Drawing Rights"], ["XOF", "CFA Franc BCEAO"], ["XPF", "CFP Franc"], 
	["YER", "Yemeni Rial"], ["ZAR", "South African Rand"], ["ZMW", "Zambian Kwacha"], ["ZWL", "Zimbabwean Dollar"], 
	]

	top_ten_crypto = top_ten_crypto = [
	"BTC",
	"ETH",
	"XRP",
	"BCH",
	"LTC",
	"XLM",
	"ETC",
	"BAT",
	"ZEC",
	"USDC",
	]
	#~~generates a random api key each time a call is made. The key is not specific, but a current theory is
	#~~too many requests from the same dummykey msy cause issues
	api_key = str(randint(0,320000))
	#~~The CryptoCurrency class takes a minimum of one argument (the api key), but the retry count can be added
	#~~as well. This was added to avoid retrying failed attempts as it caused known good requests to fail directly
	#~~afterwards. 
	crypto = CryptoCurrencies(api_key,0)
	if isBehindFirewall():
		proxies = {
		'http' : 'https://proxy-us.intel.com:911',
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
#-test line#c.get_daily("BTC","USD")


'''
User inputs all account information, stock symbol, and variables into form.
Program parses information into correct structs.
Step 1: Add account info to Account dictionary
Step 2: Add stock into from XML to Stock dictionary
Step 3: Run run() with symbol and dictionaries already filled.

Notes:

There needs to be a better Stock API. Maybe look for one in another language.
Are indicators like the MACD derivitaves of common stock info?
'''

import pprint
import math
from decimal import *

#User's account information (pulled from form)
Account = {
	'cash'	:173.36,	#User cash on hand
	'sO'	:20000,		#Shares owned of stock
	'com'	:7,			#Commision Per Trade
	'tAV'	:46599.83	#Total Account Value (Optional)
};

#Raw stock information parsed from XML or API
Stock = {
	'price'			:21.57,	#Current Stock Price
	'divPerShare'	:.1821,	#Dividends payed per share
	'dP'			:12		#Divedends are payed out dP times per year
};

#User defined variables from console input or Front-End form
Variables = {
	'tC'	:4,		#Times Compounded per year (how many purchases per year)
	'years'	:5,		#Years of investment
	'mP'	:0,		#Months passed
	'sP'	:0,		#Shares purchased
	'dE'	:0,		#Dividends Earned
	'tIE'	:0		#Total Interest Earned
};

def calc(Account, Stock, Variables):	#Takes Account, Stock, Variables dicitonaries
	acc = Account
	stock = Stock
	varis = Variables
	varis['mP']+= 12/varis['tC']
	varis['dE'] = acc['sO'] * stock['divPerShare'] * ((12/varis['tC'])/(12/stock['dP']))
	acc['cash'] += varis['dE']
	varis['sP'] = math.floor((acc['cash']-acc['com'])/stock['price'])
	acc['sO'] += varis['sP']
	acc['cash'] -= acc['com']+varis['sP']*stock['price']
	varis['tIE'] += varis['dE']
	if (acc['tAV'] != -1):
		acc['tAV'] += varis['dE']-acc['cash']	

def results(Account, Variables): #takes account & variable dictionaries as parameters
	getcontext().prec = 3
	acc = Account
	varis = Variables
	res = ''
	res+="Purchasing shares... \n" 
	res+='At the end of %i months...\n' % (varis['mP'])
	res+='Dividends collected over the past %d month(s) = $%d\n' % (12/varis['tC'], varis['dE'])
	res+='Shares purchased = %d shares\n' % (varis['sP'])
	res+='Shares owned = %d shares\n' % (acc['sO'])
	res+='Cash = $%d\n' % (acc['cash'])
	res+='Total Brokerage Account Value = $%d\n' % (Decimal(acc['tAV']))
	res+='Total Interest earned = $%d\n' % (Decimal(varis['tIE']))
	print (res)

def run(Account, Stock, Variables):
	i=0
	l = Variables['tC'] * Variables['years']
	while (i<l):
		calc(Account, Stock, Variables)
		#results(Account, Variables)
		i+=1
	
def runForMax(Account, Stock, Variables):
	acc = Account
	stock = Stock
	varis = Variables
	maxVariables = Variables
	maxIE = 0

	i=.5
	while (i<=12):
		acc = Account.copy()
		stock = Stock.copy()
		varis = Variables.copy()
		varis['tC'] = i
		run(acc, stock, varis)
		total = varis['tIE']
		print total
		if (total > maxIE):
			print total
			maxIE = total
			maxAccount = acc
			maxVariables = varis
		i+=.5
	print maxVariables['tC']	
	results(acc, maxVariables)


def main(): #Account acc, Stock sym, Variables varis)
	"""
	#query Stock API for raw data
	#parse raw data to stock dictionary
	if (button=runSettings):
		for (i=0; i<(varis['tC'] * varis['years']); i+=1):
			calc(acc, sym, varis)
			results(acc, varis)
			
	if (button=findMax):
		runForMax(acc, sym, varis)

	"""
	'''
	results(Account, Variables)
	i=0
	l = Variables['tC'] * Variables['years']
	while (i<l):
		calc(Account, Stock, Variables)
		results(Account, Variables)
		i+=1
	'''
	runForMax(Account, Stock, Variables)
main()

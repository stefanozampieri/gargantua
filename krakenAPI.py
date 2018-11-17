# see https://www.kraken.com/help/api for more info on the returns of those functions


import krakenex

#Creation de l'API kraken
#kraken=krakenex.API()

#Chargement du fichier key de kraken(specifique a mon compte)
#kraken.load_key("kraken.key")

#********Balance functions***********
def get_EUR_balance():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	bal = kraken.query_private('Balance')
	bal = bal['result']
	bal = bal['ZEUR']
	kraken.close()
	return bal


def get_XBT_balance():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	bal = kraken.query_private('Balance')
	bal = bal['result']
	bal = bal['XXBT']
	kraken.close()
	return bal


def get_XRP_balance():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	bal = kraken.query_private('Balance')
	bal = bal['result']
	bal = bal['XXRP']
	kraken.close()
	return bal



def get_LTC_balance():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	bal = kraken.query_private('Balance')
	bal = bal['result']
	bal = bal['XLTC']
	kraken.close()
	return bal


def get_XDG_balance():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	bal = kraken.query_private('Balance')
	bal = bal['result']
	bal = bal['XXDG']
	kraken.close()
	return bal


def get_ETH_balance():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	bal = kraken.query_private('Balance')
	bal = bal['result']
	bal = bal['XETH']
	kraken.close()
	return bal

def get_DASH_balance():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	bal = kraken.query_private('Balance')
	bal = bal['result']
	bal = bal['DASH']
	kraken.close()
	return bal

#********Server time functions*************

def get_time():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	t=kraken.query_public('Time')
	t=t['result']['unixtime']
	kraken.close()	
	return t

def get_date():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	t=kraken.query_public('Time')
	t=t['result']['rfc1123']
	kraken.close()	
	return t

#***********Assets functions**********************

def get_assets():
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	t=kraken.query_public('Assets')
	kraken.close()	
	return t

#*************** OHLC data functions *****************

def get_OHLC(pair,since): # Example of pair 'XXBTZEUR' for bitcoin/euro. since is str(unixtime) since when you need the data
	kraken=krakenex.API()
	kraken.load_key("kraken.key")
	t=kraken.query_public('OHLC', data = {'pair': pair , 'since': since })
	kraken.close()	
	return t

import krakenex

#Creation de l'API kraken
#kraken=krakenex.API()

#Chargement du fichier key de kraken(specifique a mon compte)
#kraken.load_key("kraken.key")

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



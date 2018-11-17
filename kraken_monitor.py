#!/usr/bin/env python3

import krakenex
from tkinter import *
import krakenAPI

#Creation de l'API kraken
#kraken=krakenex.API()

#Chargement du fichier key de craken(specifique a mon compte) 
#kraken.load_key("kraken.key")

#Requete d'info privés
#balance = kraken.query_private('Balance')
#orders = kraken.query_private('OpenOrders')

#Garder uniquement les resultats
#balance = balance['result']
#orders = orders['result']


b_eur= krakenAPI.get_EUR_balance()
b_xbt= krakenAPI.get_XBT_balance()
b_xrp= krakenAPI.get_XRP_balance()
b_ltc= krakenAPI.get_LTC_balance()
b_xdg= krakenAPI.get_XDG_balance()
b_eth= krakenAPI.get_ETH_balance()
b_dash= krakenAPI.get_DASH_balance()

#affichage
print("Euro: " + b_eur)
print("Bitcoin: " + b_xbt)
print("Ripple coin: " + b_xrp)
print("Litecoin: " + b_ltc)
print("Dogecoin: " + b_xdg)
print("Ethereum: " + b_eth)
print("Dash: " + b_dash)


#fermeture de session
#kraken.close()




	

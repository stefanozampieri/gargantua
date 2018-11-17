#!/usr/bin/env python3

import krakenAPI


b_eur = krakenAPI.get_EUR_balance()
b_xbt = krakenAPI.get_XBT_balance()
b_xrp = krakenAPI.get_XRP_balance()
b_ltc = krakenAPI.get_LTC_balance()
b_xdg = krakenAPI.get_XDG_balance()
b_eth = krakenAPI.get_ETH_balance()
b_dash = krakenAPI.get_DASH_balance()

unixtime = krakenAPI.get_time()
serverdate = krakenAPI.get_date()

t=krakenAPI.get_OHLC('XXBTZEUR',str(1542416729))

print(t)

#affichage
print("Unix time:   " + str(unixtime))
print("Server date: " + serverdate)
print("*******************************")
print("*       Account balance       *")
print("*******************************")
print("Euro:        " + b_eur)
print("Bitcoin:     " + b_xbt)
print("Ripple coin: " + b_xrp)
print("Litecoin:    " + b_ltc)
print("Dogecoin:    " + b_xdg)
print("Ethereum:    " + b_eth)
print("Dash:        " + b_dash)





	

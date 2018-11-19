#!/usr/bin/env python3

#different pairs we can use:
#
# 'XXBTZEUR' = bitcoin/euro
# 'XXRPZEUR' = ripple coin/euro
# 'XLTCZEUR' = litecoin/euro
# 'XXDGXXBT' = dogecoin/euro
# 'XETHZEUR' = ethereum/euro
# 'DASHZEUR' = Dash/euro

import krakenAPI


b_eur = krakenAPI.get_EUR_balance()
b_xbt = krakenAPI.get_XBT_balance()
b_xrp = krakenAPI.get_XRP_balance()
b_ltc = krakenAPI.get_LTC_balance()
b_xdg = krakenAPI.get_XDG_balance()
b_eth = krakenAPI.get_ETH_balance()
b_dash = krakenAPI.get_DASH_balance()

v_btc = krakenAPI.get_value('XXBTZEUR') 
v_xrp = krakenAPI.get_value('XXRPZEUR')
v_ltc = krakenAPI.get_value('XLTCZEUR')
v_xdg = krakenAPI.get_value('XXDGXXBT')
v_eth = krakenAPI.get_value('XETHZEUR')
v_dash = krakenAPI.get_value('DASHEUR')

unixtime = krakenAPI.get_time()
serverdate = krakenAPI.get_date()



#affichage
print("Unix time:   " + str(unixtime))
print("Server date: " + serverdate)
print("****************************************************************")
print("*       Account balance  at: " + serverdate +"     *")
print("****************************************************************")
print("               Amount          Unit price in Euro      Amount in Euro") 
print("Euro:        " + b_eur + "             1                       " + b_eur )
print("Bitcoin:     " + b_xbt + "       " + v_btc + "             " + str(float(v_btc)*float(b_xbt)))
print("Ripple coin: " + b_xrp + "       " + v_xrp + "             " + str(float(v_xrp)*float(b_xrp)))
print("Litecoin:    " + b_ltc + "       " + v_ltc + "             " + str(float(v_ltc)*float(b_ltc)))
print("Dogecoin:    " + b_xdg + "       " + str(float(v_xdg)*float(v_btc)) + "             " + str(float(v_xdg)*float(b_xdg)*float(v_btc)))
print("Ethereum:    " + b_eth + "       " + v_eth + "             " + str(float(v_eth)*float(b_eth)))
print("Dash:        " + b_dash + "       " + v_dash + "             " + str(float(v_dash)*float(b_dash)))

 



	

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:30:29 2021

@author: camamarshall
"""

import matplotlib.pyplot as plt
import numpy as np
import forex_python
import math
from forex_python.converter import CurrencyRates
import requests

api_url = 'https://xchscan.com/api/chia-price'
raw = requests.get(api_url).json()
price = raw['usd']
c = CurrencyRates()
Currency = c.get_rate('USD', 'AUD')  #convert USD to AUD
price_aud = price * Currency


#Electricity Usage Per Year = (Watts / 1000) * Hours/Day * Days/Week * Weeks/Year = kWh/year"

number_of_drives= 6
HDD_Watts = 8
Desktop_Watts = 171

electricity_usage_year = (Desktop_Watts+(6*HDD_Watts))/1000 * 24 * 7 * 54

# Electricity Cost Per Year = kWh/year * (cents/kWh / 100) = $/year"

electricity_cost_month = 26/100 *  electricity_usage_year/12


# Using Numpy to create an array X
x = np.arange(0,12,1)

# Assign variables to the y axis part of the curve
y = price_aud*0.1713*x
z = electricity_cost_month * x
  
# Plotting both the curves simultaneously
plt.plot(x, y, color='r', label='Chia Value, price='+str(round(price_aud,2)))
plt.plot(x, z, color='g', label='Cost Price')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Months")
plt.ylabel("AUD Dollars")
plt.title("Cost Vs Revenue")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()
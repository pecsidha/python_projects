# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 20:02:34 2020

@author: sidhartha kumar
"""

import math

a = math.sqrt(25)

print(a)

import random

for i in range (20):
    print(random.randint(0,100), end =' ')



import matplotlib.pyplot as plt

# get_ipython().run_line_magic('matplotlib', 'inline')

plt.barh(y=[3,4,5,6], height=[1,0.5,1.2,0.8], width=0.2, align='center')
plt.show()



# import matplotlib.pyplot as plt
# plt.plot(range(10), 'o')


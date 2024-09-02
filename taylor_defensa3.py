# -*- coding: utf-8 -*-
"""taylor_defensa3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZPnGmLCDyW4HwgEccNITDRVz2C4eCGYp
"""

import math
x=math.pi/6
x1=math.pi/5
h=x1-x
n=1
ef=1
fx=math.exp(x)
derivada=math.exp(x)
while ef > 0.0005:
  fx=fx+(derivada/math.factorial(n))*(h**n)
  ef=abs(derivada*(h**n))/math.factorial(n)
  n=n+1
print("con un valor aproximado de: ",fx)
print("con un error de: ",ef)
print("con n iterariciones: ", n-1)
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:55:31 2020

@author: meet
"""




import matplotlib.pyplot as plt

import numpy as np

#first we define the constants
g=9.8 
L=67
R=0.1     #angular speed of earth
lamda= 3 #latitude
k_1=1
k_2=1              


#time
t = np.arange(0,200,0.9)
    
#defining the function
a_=1j*(np.sqrt(g/L)*t)
a=np.exp(a_)


b_=1j*((-1)*np.sqrt(g/L)*t)
b=np.exp(b_)

c_=1j*(R*np.sin(lamda)*(-1)*t)
    
c=np.exp(c_)
u=(k_1*a+k_2*b)*c
#separating the real and complex part  
x=u.real
y=u.imag
plt.xlim(-2.5,2.5)
plt.ylim(-2.5,2.5)
    
#just plotting
plt.plot(x,y,'g')
plt.grid()


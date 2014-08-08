 # -*- coding: utf-8 -*-
"""
@author: youbin
"""

from pylab import *
from DEVICE_2 import *
import sys

def Initial():
    print "Does the input keep at constant?"

def grow(input, dt = 0.1):
    k1 = 1  ## 1/maximum density
    growrate = 0.5
    output_1 = input + growrate*input*(1 - k1*input)*dt
    return output_1

def Calculate(Tmax):

    dt=0.1
    T = arange(0,Tmax,dt)
    x = zeros_like(T)
    y = zeros_like(T)
    
    input = 1
    lenth = len(sys.argv)
    sub1 = zeros(lenth)
    x[0] = 0.02
    n = 0
    sub1[0] = 1
    
    
    for t in T:
        
        od = grow(x[n])
        x[n+1] = od
        
        if lenth >1:
            for i in range(1, lenth):
                #print i
                dev = eval(sys.argv[i])
                #print dev.__doc__
                [sub1[i-1], sub1[i]] = dev(od, sub1[i-1], sub1[i])
            y[n+1] = sub1[lenth-1]
            
        if n >= Tmax/dt - 2:
            break
        else:
            n = n+1
    return [T,x,y]

if __name__=="__main__":
    #Initial()
    
    [T,x_1,x_2] = Calculate(40)
    figure(1)
    xlabel('time')
    ylabel('a.u.')
    ##title('Amplitude of final stage vs. $\mu$')
    plot(T,x_1,label='Density')
    plot(T,x_2,label='output_1')
    legend()
    show()
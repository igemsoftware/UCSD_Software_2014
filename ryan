 # -*- coding: utf-8 -*-
"""
@author: Ryan
Version v1.0

"""

from pylab import *
from DEVICE_2 import *
import sys

def grow(input, dt = 0.1):
    ''' Growing curve'''
    k1 = 1  ## 1/maximum density(OD)
    growrate = 0.5
    output_1 = input + growrate*input*(1 - k1*input)*dt
    return output_1

def Calculate(Tmax = 20):

    '''The input parameter is the maximum time step of experiment.'''
    
## initialization
    dt=0.1
    T = arange(0,Tmax,dt)  ## matrix of time axis
    x = zeros_like(T)  ## matrix of OD
    y = zeros_like(T)  ## matrix of output
    
    input = 1
    lenth = len(sys.argv)
    sub1 = zeros(lenth)
    x[0] = 0.02  ## initial condition of cell density(OD)
    n = 0
    sub1[0] = 1  ## initial concentration of intermediate or inducer
    
## substitution
    for t in T:
        
        ## growing curve
        od = grow(x[n])
        x[n+1] = od
        
        ## device
        if lenth >1:
            for i in range(1, lenth):
                dev = eval(sys.argv[i])  ## load the devices' name from ARGV
                [sub1[i-1], sub1[i]] = dev(od, sub1[i-1], sub1[i])
            y[n+1] = sub1[lenth-1]
            
        if n >= Tmax/dt - 2:
            break
        else:
            n = n+1
    return [T,x,y]

if __name__=="__main__":
    ''' Drawing script'''
    
    [T,x_1,x_2] = Calculate(40)
    figure(1)
    xlabel('time')
    ylabel('OD(a.u.)')
    title('Growing Curve')
    plot(T,x_1,label='OD')
    legend()
    
    figure(2)
    xlabel('time')
    ylabel('output(a.u.)')
    title('Output')
    plot(T,x_2,label='output')
    legend()
    show()

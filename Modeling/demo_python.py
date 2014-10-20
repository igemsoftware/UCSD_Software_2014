 # -*- coding: utf-8 -*-
"""

"""

from pylab import *
from DEVICE import *    ##from DEVICE import *
import sys
import string
import re

def grow(input, dt = 0.1):
    ''' Growing curve'''
    k1 = 1  ## 1/maximum density(OD)
    growrate = 0.1
    output_1 = input + growrate*input*(1 - k1*input)*dt
    return output_1

def Calculate(Tmax = 20, net='network.txt'):    ## Tmax is the total simulation period in real time and net is the name of network file

    '''The input parameter is the maximum time step of experiment.'''
    
## initialization

    ## import the network file
    network_file = open(net)
    network = network_file.readlines()
    LenthOfNetwork = len(network)
    network = []
    network_file = open(net)
    for line in network_file:
        network.append(re.split('[\t \n]',line))
    network_file.close()

    dt=0.1
    T = arange(0,Tmax,dt)  ## matrix of time axis
    OD = zeros_like(T)  ## matrix of OD
    out = zeros_like(T)  ## matrix of output
    
    InputMatrix = [[0 for col in range(2)] for row in range(LenthOfNetwork)] ## matrix of input
    BufferOfOutput = zeros(LenthOfNetwork)  ## array of output
    
    for i in range(LenthOfNetwork):
        InputMatrix[i][0] = string.atof(network[i][2])
        InputMatrix[i][1] = string.atof(network[i][4])
        BufferOfOutput[i] = string.atof(network[i][6])


    OD[0] = 0.02  ## initial condition of cell density(OD)
    n = 0

## substitution
    for t in T:
        
        ## growing curve
        condensity = grow(OD[n])
        OD[n+1] = condensity
    
        ## integrating the ODEs
        if LenthOfNetwork >0:
            for i in range(LenthOfNetwork):
                
                for m in range(LenthOfNetwork):
                    if network[i][1] == network[m][0]:
                        InputMatrix[i][0] = BufferOfOutput[m]
                    if network[i][3] == network[m][0]:
                        InputMatrix[i][1] = BufferOfOutput[m]
            
                dev = eval(network[i][0])  ## load the devices' name as their corresponding function
                [InputMatrix[i][0], InputMatrix[i][1], BufferOfOutput[i]] = dev(condensity, InputMatrix[i][0], InputMatrix[i][1], BufferOfOutput[i])
                
                ## save output data into output array
                if network[i][5] == 'output':
                    out[n+1] = BufferOfOutput[i]
    
        if n >= Tmax/dt - 2:
            break
        else:
            n = n+1

    return [T, OD, out]

if __name__=="__main__":
    ''' Drawing script'''

    [T, OD, z] = Calculate(100, 'network.txt')
    figure(1)
    xlabel('time')
    ylabel('OD(a.u.)')
    title('Growing Curve')
    plot(T/10,OD,label='OD')
    legend()
    
    figure(2)
    xlabel('time')
    ylabel('output(a.u.)')
    title('Output')
    plot(T/10,z,label='output')
    legend()
    
    show()

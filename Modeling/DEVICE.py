# -*- coding: utf-8 -*-
"""
This script includes ODE equations of devices.
Costomer could add their device at the end of this file but new function has to share the same format as our provided examples.
"""

def andgate(od, input1, input2, output1, dt = 0.1):
    ''' This is device_1'''  ## Here is the discription of device
    k1 = 0.7       ## reduction rate of input, range from 0 to infinite; k1=0 means the concentration of input keeps at constant.
    k2 = 0.1       ## production rate of output.
    k3 = 1         ## consuming rate of output by decomposition.
    k4 = 0.3
    input_1 = input1 - k1*od*input1*input2*dt
    input_2 = input2 - k2*od*input1*input2*dt
    output_1 = output1 + (k3*input1*input2*od - k4*od*output1)*dt
    return (input_1, input_2, output_1)

def orgate(od, input1, input2, output1, dt = 0.1):
    ''' This is device_2'''  ## Here is the discription of device
    k1 = 0.7       ## reduction rate of input, range from 0 to infinite; k1=0 means the concentration of input keeps at constant.
    k2 = 0.3       ## production rate of output.
    k3 = 0.5        ## consuming rate of output by decomposition.
    k4 = 0.1
    k5 = 0.4
    input_1 = input1 - k1*od*input1*dt
    input_2 = input2 - k2*od*input2*dt
    output_1 = output1 + (k3*input1 + k4*input2 - k5*output1)*od*dt
    return (input_1, input_2, output_1)

def GFP(od, input1, input2, output1, dt = 0.1):
    ''' This is GFP'''
    k1 = 10000
    k2 = 0.5

    input_1 = input1
    input_2 = input2
    output_1 = output1 + (k1*input1 - k2*output1)*od*dt
    return (input_1, input_2, output_1)

def PBAD(od, input1, input2, output1, dt = 0.1):
    ''' This is PBAD'''
    k1 = 0.5
    k2 = 0.2
    
    input_1 = input1 - k1*od*input1*dt
    input_2 = input2 - k1*od*input2*dt
    output_1 = k2*(input1+input2)*od*dt
    return (input_1, input_2, output_1)

def PT7(od, input1, input2, output1, dt = 0.1):
    ''' This is PT7'''
    k1 = 0.5
    k2 = 0
    k3 = 0.1
    k4 = 0.2

    input_1 = input1 - k1*od*input1*dt
    input_2 = input1 - k2*od*input1*dt
    output_1 = output1 + (k3*input1 - k4*input2)*od*dt
    return (input_1, input_2, output_1)

def T7(od, input1, input2, output1, dt = 0.1):
    ''' This is T7'''
    k1 = 10
    k2 = 0.5

    input_1 = input1
    input_2 = input2
    output_1 = output1 + (k1*input1 - k2*input2*output1)*od*dt
    return (input_1, input_2, output_1)

def araC(od, input1, input2, output1, dt = 0.1):
    ''' This is araC'''
    k1 = 4
    k2 = 1
    
    input_1 = input1
    input_2 = input2
    output_1 = output1 + (k1*input1 - k2*input1*output1)*od*dt
    return (input_1, input_2, output_1)

def LacI(od, input1, input2, output1, dt = 0.1):
    ''' This is araC'''
    k1 = 0.5
    k2 = 0.3
    
    input_1 = input1
    input_2 = input2
    output_1 = output1 + (k1*input1 - k2*input1*output1)*od*dt
    return (input_1, input_2, output_1)

def pTara(od, input1, input2, output1, dt = 0.1):
    ''' This is araC'''
    k1 = 20
    k2 = 1
    k3 = 3
    k4 = 5.2
    k5 = 5
    
    input_1 = input1 - ( k1*input1 )*od*dt
    input_2 = k2*od
    output_1 = output1 + (k3*input1 + k4*input_2*od - k5*output1)*od*dt
    return (input_1, input_2, output_1)

def pET28(od, input1, input2, output1, dt = 0.1):
    ''' This is araC'''
    k1 = 50000
    k2 = 5
    
    input_1 = input1
    input_2 = input2
    output_1 = output1 + (k1*input1 - k2*output1)*od*dt
    return (input_1, input_2, output_1)


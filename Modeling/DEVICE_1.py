# -*- coding: utf-8 -*-
"""
@author: youbin
"""

def device_1(od, input, output, dt = 0.1):
    ''' This device is device_1'''  ## Here is the discription of device
    k1 = 0.3
    k2 = 0.5
    k3 = 0
    input_1 = input - k1*od*input*dt
    output_1 = output + (k2*input*od - k3*od)*dt
    return (input_1, output_1)

def device_2(od, input, output, dt = 0.1):
    ''' This device is device_2'''
    k1 = 0.3
    k2 = 0.5
    k3 = 0
    input_1 = input - k1*od*input*dt
    output_1 = output + (k2*input*od - k3*od)*dt
    return (input_1, output_1)

def device_3(od, input, output, dt = 0.1):
    k1 = 0.3
    k2 = 0.5
    k3 = 0
    input_1 = input - k1*od*input*dt
    output_1 = output + (k2*input*od - k3*od)*dt
    return (input_1, output_1)

def device_4(od, input, output, dt = 0.1):
    k1 = 0.3
    k2 = 0.5
    k3 = 0
    input_1 = input - k1*od*input*dt
    output_1 = output + (k2*input*od - k3*od)*dt
    return (input_1, output_1)

def device_5(od, input, output, dt = 0.1):
    k1 = 0.3
    k2 = 0.5
    k3 = 0
    input_1 = input - k1*od*input*dt
    output_1 = output + (k2*input*od - k3*od)*dt
    return (input_1, output_1)


#!/bin/python3.9
import argparse

parser = argparse.ArgumentParser(description='LIFX CLI')
parser.add_argument('-p', action="store", dest="power", type=int)
parser.add_argument('-t', action="store_true", dest="toggle", default=False)
parser.add_argument('-c', action="store", dest="hue", type=int, default=False)
parser.add_argument('-brightness', action="store_true", dest="brightness", default=False)
parser.add_argument('--polybar', action="store_true", dest="polybar", default=False)
results = parser.parse_args()

from lifxlan import *
lifx = LifxLAN()

light_get = []                                           
light_addr = []
lights = []
with open('/home/trent/Projects/lifx-cli/.mac_addresses') as f:                         
    light_get = f.read().splitlines()

for l in light_get:
    addresses = l.split(' ')
    light_addr.append({'mac':addresses[0],
                   'ip':addresses[1]})

for light in light_addr:
    lights.append(Light(light['mac'],light['ip']))

if(results.power != None):
    for light in lights:
        light.set_power(results.power)

for light in lights:
    power = light.get_power()
    if(results.toggle):
        if power == 0:
            light.set_power(1)
        else: 
            light.set_power(0)

if(results.polybar):
    while(True):
        try:
            if lights[0].get_power() > 0:
                print('%{T2}%{T-}')
            else:
                print('%{T2}%{T-}')
            break
        except:
            print('error')
            pass

if results.brightness:
    print('brightness')







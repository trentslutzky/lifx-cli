from rich.console import Console
from rich.table import Column, Table
from rich import box, print, status
from rich.prompt import Prompt
import time
from time import sleep
import json

console = Console()

from lifxlan import *

lifx = LifxLAN(3)

lights = {}
lights_to_control = []

def main():
    with console.status("[bold #ffe06d]Looking for lights on the network") as status:
        lfx_lights = lifx.get_lights()
        sleep(2)
        numlights = len(lfx_lights)

    for light in lfx_lights:
        ind = lfx_lights.index(light)
        lights[ind] = {}
        lights[ind]['label'] = light.get_label()
        lights[ind]['ip'] = light.get_ip_addr()
        lights[ind]['mac'] = light.get_mac_addr()

    console.print('\nFound',numlights,'lights:',style='#ffe06d')

    table = Table(show_header=True, header_style='bold',box=box.ROUNDED)
    table.add_column(':bulb:')
    table.add_column('Name')
    table.add_column('MAC')
    table.add_column('IP')
    
    for light in lights:
        table.add_row(
            str(light),
            str(lights[light]['label']),
            str(lights[light]['mac']),
            str(lights[light]['ip']),
        )
    console.print(table)

    for light in lights:
        ready = False
        while(not ready):
            console.print('Control',lights[light]['label'],'[Y/n]? :',end='',style='#ffe06d')
            to_control = input()
            if to_control == 'y':
                light_string = lights[light]['mac']+' '+lights[light]['ip']
                lights_to_control.append(light_string)
                ready = True
            elif to_control == 'n':
                ready = True
            else:
                ready = False

    mac_file = open('.mac_addresses','w')
    for mac in lights_to_control:
        mac_file.write(mac)
        mac_file.write('\n')
    mac_file.close()

    new_lights = []
    with open('.mac_addresses') as f:
        new_lights = f.read().splitlines()


if __name__ == "__main__":
    main()



















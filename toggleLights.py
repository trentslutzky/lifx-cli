#!/usr/bin/python3.9

from lifxlan import *

lifx = LifxLAN()

desk_light_mac = "d0:73:d5:3c:c7:96"
desk_light_ip = "192.168.1.29"
main_light_mac = "d0:73:d5:36:92:ac"
main_light_ip = "192.168.1.28"

def main():
    desk_light = Light(desk_light_mac, desk_light_ip)
    main_light = Light(main_light_mac, main_light_ip)

    power = desk_light.get_power()

    if(power == 0):
        desk_light.set_power(1,10,False)
        main_light.set_power(1,10,False)
    else:
        desk_light.set_power(0,10,False)
        main_light.set_power(0,10,False)

if __name__=="__main__":
    main()

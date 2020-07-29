from lifxlan import *
import argparse
import random

lifx = LifxLAN()

desk_light_mac = "d0:73:d5:3c:c7:96"
desk_light_ip = "192.168.1.11"
bed_light_mac = "d0:73:d5:2b:45:89"
bed_light_ip = "192.168.1.2"


def main():    
    h = random.randint(0,65535)
    
    color = [h,6535,65535,0]
    
    desk_light = Light(desk_light_mac, desk_light_ip)
    bed_light = Light(bed_light_mac, bed_light_ip)

    desk_light.set_color(color,200,False)
    bed_light.set_color(color,200,False)

if __name__=="__main__":
    main()

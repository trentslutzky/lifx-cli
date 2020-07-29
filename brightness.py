from lifxlan import *
import argparse

parser = argparse.ArgumentParser(description='set the brightess of the lights')

parser.add_argument('Brightness',
                    metavar='brighness',
                    type=int,
                    help='the target light brightness')

args = parser.parse_args()
brightness = args.Brightness

lifx = LifxLAN()

desk_light_mac = "d0:73:d5:3c:c7:96"
desk_light_ip = "192.168.1.11"
bed_light_mac = "d0:73:d5:2b:45:89"
bed_light_ip = "192.168.1.2"

def main():
    desk_light = Light(desk_light_mac, desk_light_ip)
    bed_light = Light(bed_light_mac, bed_light_ip)

    brightness_formatted = (brightness/100)*(65535)
    
    if brightness_formatted > 65535:
        brightness_formatted = 65535

    desk_light.set_brightness(brightness_formatted,200,False)
    bed_light.set_brightness(brightness_formatted,200,False)

if __name__=="__main__":
    main()

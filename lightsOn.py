from lifxlan import *

lifx = LifxLAN()

desk_light_mac = "d0:73:d5:3c:c7:96"
desk_light_ip = "192.168.1.32"
bed_light_mac = "d0:73:d5:36:92:ac"
bed_light_ip = "192.168.1.30"

def main():
    desk_light = Light(desk_light_mac, desk_light_ip)
    bed_light = Light(bed_light_mac, bed_light_ip)

    desk_light.set_power(1,100,False)
    bed_light.set_power(1,100,False)

if __name__=="__main__":
    main()

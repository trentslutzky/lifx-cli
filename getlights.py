from lifxlan import *

lifx = LifxLAN()

def main():
    lights = lifx.get_lights()
    for light in lights:
        print(light)


if __name__ == "__main__":
    main()

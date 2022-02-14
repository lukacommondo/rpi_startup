import sys
sys.path.append("/home/pi/Modules")
import time
from SHT21 import SHT21


def sht_main():
    sht21 = SHT21()
    x = 0
    while x < 10:
        x += 1
        if x == 6:
            break
        # (temperature, humidity) = sht21.measure(1)
        # print("Temperatura = {}*C Vlaga = {}%)".format(temperature, humidity)
        (temperature, humidity) = sht21.measure(1)      # I2C-1 Port
        print("Temperature: %s °C  Humidity: %s %%" % (temperature, humidity))
        time.sleep(2)
        # print("Temperatura = {}*C Vlaga = {}%)".format(temperature, humidity)
    print("\nZavrseno mjerenje!")


if __name__ == "__main__":
    sht_main()

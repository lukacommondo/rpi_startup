
#import RPi.GPIO as GPIO
#import os
#import time
import Adafruit_DHT

#Odabir senzora iz Adafruit library-ja
DHT_SENSOR = Adafruit_DHT.DHT22


class DHT_22inf:
    def __init__(self, dht_pin):
        self.dht_pin = dht_pin

    def temp_vlaga(self):

        try:
            while True:
                humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, self.dht_pin)

                if humidity is not None and temperature is not None:
                    print("Temperatura = {0:0.1f}*C Vlaga = {0:0.1f}%".format(temperature, humidity))
                else:
                    print("Mjerenje nije bilo uspješno")
        except KeyboardInterrupt:
            print("\nKraj!")


def main():
    x = int(input("Unesite broj pina na koji je DHT spojen: "))
    senzor = DHT_22inf(x)
    senzor.temp_vlaga()


if __name__ == "__main__":
    main()


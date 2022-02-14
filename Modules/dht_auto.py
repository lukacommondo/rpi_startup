
#import RPi.GPIO as GPIO
#import os
#import time
import Adafruit_DHT

#Odabir senzora iz Adafruit library-ja
DHT_SENSOR = Adafruit_DHT.DHT22

class DHT_22:
    def __init__(self, dht_pin):
        self.dht_pin = dht_pin

    def temp_vlaga(self):
        y = 15
        broj = 0
        while broj in range(y):
            broj += 1
            if broj == y:
                break
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, self.dht_pin)
            if humidity is not None and temperature is not None:
                print("{} mjerenje:".format(broj))
                print("Temperatura = {0:0.1f}*C Vlaga = {0:0.1f}%".format(temperature, humidity))
            else:
                print("Mjerenje nije bilo uspješno")
        print("Zavrseno mjerenje!")


def main():
    x = int(input("Unesite broj pina na koji je DHT spojen: "))
    senzor = DHT_22(x)
    senzor.temp_vlaga()


if __name__ == "__main__":
    main()

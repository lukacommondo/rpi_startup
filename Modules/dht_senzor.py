
#import RPi.GPIO as GPIO
#import os
import time
import Adafruit_DHT

#Odabir senzora iz Adafruit library-ja
DHT_SENSOR = Adafruit_DHT.DHT22

class DHT_22:
    def __init__(self, dht_pin):
        self.dht_pin = dht_pin

    def temp_vlaga(self):
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, self.dht_pin)
        if humidity is not None and temperature is not None:
            return "Temperatura = {0:0.1f}*C Vlaga = {0:0.1f}%".format(temperature, humidity)
            time.sleep(1)
        else:
            print("Mjerenje nije bilo uspješno!")

        #print("Zavrseno mjerenje!")


def main():
    define_dht_pin = int(input("Unesite broj pina na koji je DHT spojen: "))
    #pin = 10
    senzor = DHT_22(define_dht_pin)
    senzor.temp_vlaga()


if __name__ == "__main__":
    main()

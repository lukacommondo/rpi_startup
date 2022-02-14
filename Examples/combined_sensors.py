import sys
sys.path.append("/home/pi/Modules")
'''
Dodavanje foldera sa modulima u python path
'''
import time
from dht_auto import DHT_22
from ledimp import LED
import sht21a

print("Ukoliko senzor nije spojen unesite 0")
#Input x
led_pin = int(input("Unesite GPIO pin na koji je spojena LED lampica(BCM logika): "))
#Input y
dht_pin = int(input("Unesite GPIO pin na koji je spojen DHT22 senzor(BCM logika): "))
#Input z
#z = int(input("Unesite GPIO;))

#LED lampica
if led_pin > 0:
    print("\nPokretanje LED lampice:")
    time.sleep(1)
    led = LED(led_pin)
    led.on_off()
else:
    print("\nSenzor 1 nije spojen")
#DHT22 senzor
if dht_pin > 0:
    print("\nPokretanje DHT22 senzora:")
    time.sleep(1)
    senzor = DHT_22(dht_pin)
    senzor.temp_vlaga()
else:
    print("\nSenzor 2 nije spojen!")

print("\nPokretanje SHT21 senzora:")
time.sleep(1)
sht = sht21a.sht_main()
#Završeno ispitivanje
print("\nSvi senzori su ispitani!")






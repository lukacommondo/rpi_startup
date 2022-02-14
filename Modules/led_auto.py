
import RPi.GPIO as GPIO
import time

#Postavljanje da se koristi GPIO logika numeriranja pinova
GPIO.setmode(GPIO.BCM)


class LED:

    def __init__(self, led_pin):
        self.led_pin = led_pin
        """Unosimo na koji je pin LED spojena"""

    def on_off(self):

        x = 10
        while i in range(x):
            i += 1
            if i == 5:
                break
            #Postavljamo odabrani pin kao Output
            GPIO.setup(self.led_pin, GPIO.OUT)
            #Paljenje i gasenje ledice u intervalima od 1 sekunde
            print("{} ciklus:".format(x))
            time.sleep(0.5)
            print("LED on")
            GPIO.output(self.led_pin, GPIO.HIGH)
            time.sleep(1)
            print("LED off")
            GPIO.output(self.led_pin, GPIO.LOW)
            time.sleep(1)
        print("Zavrseno ispitivanje LED lampice!")
        GPIO.cleanup()


def main():
    x = int(input("Unesite broj pina na koju je LED spojena: "))
    #definiranje instance
    led = LED(x)
    #testiranje funkcije on_ff
    led.on_off()


if __name__ == "__main__":
    main()

from serial_protocol import *


def main():


	word = input(f"Input {(recieve_limit)/8}. byte sentance : ")
	tx_buffer = string2bits(word)
	GPIO.output(tx_pin, 1)
	GPIO.output(clock_pin, 0)
	time.sleep(1)
	#GPIO.output(tx_pin, 0)
	transfer_data(tx_buffer)


if __name__ == '__main__':
	main()

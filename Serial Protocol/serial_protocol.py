import RPi.GPIO as GPIO
import time 
import argparse

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

parser = argparse.ArgumentParser(description="Set TX and RX pin for serial comunication protocol")
parser.add_argument("tx_pin", metavar="tx_pin", type=int, help="Input pin used for transfering data")
parser.add_argument("rx_pin", metavar="rx_pin", type=int, help="Input pin used for receiving data")
parser.add_argument("clock_pin", metavar="clock_pin", type=int, help="Input pin used for baud rate sync on TX/RX")
parser.add_argument("baud_rate", metavar="baud_rate", type=int, help="Input data transfer speed")
parser.add_argument("recieve_limit", metavar="recieve_limit", type=int, help="Input rx_buffer limit")

args = parser.parse_args()

baud_rate = args.baud_rate
tx_pin = args.tx_pin 
rx_pin = args.rx_pin
clock_pin = args.clock_pin
recieve_limit = args.recieve_limit

GPIO.setup(tx_pin, GPIO.OUT)
GPIO.setup(rx_pin, GPIO.IN)
GPIO.setup(clock_pin, GPIO.OUT)


def string2bits(word=''):
	'''
	Input: String or multiple strings, space included
	Output: List of bytes as elements, zfill adds aditional 0's for easier iteration
	'''
	return [bin(ord(element))[2:].zfill(8) for element in word]


def original_form(rx_buffer):
	'''
	Input: List in which rx_buffer separates received bytes into singe bits for transfer
	Output: List of bits concatenated into bytes (8-bits), into their original form
	'''
	return [''.join(rx_buffer[i:i + 8]) for i in range(0, len(rx_buffer), 8)]


def bit2string(ordered_rx_buffer):
	'''
	Input: List of received bytes prepared by original_form function
	Output: Characters readable by humans (ascii, utf-8) 
	'''
	return ''.join([chr(int(letter,2)) for letter in ordered_rx_buffer])


def transfer_data(tx_buffer):
	'''
	Input: List of bytes 
	Output: Activates 'clock signal' which synchronizes baud rates on transfering and receiving sides
			Generates 'High' and 'Low' values in respect to bits which are interpreted on the receive end
	'''

	while len(tx_buffer) > 0: 
		
		#if GPIO.output(tx_pin, 0): 

		GPIO.output(clock_pin, 1) 
		time.sleep(1/(baud_rate))
		bit_count = 0

		while bit_count < 8:

			try:

				for data_byte in tx_buffer[:1]:

					for bit in data_byte[:8]:

						if bit == "0":
							
							GPIO.output(tx_pin, 0)

						elif bit == "1":
							
							GPIO.output(tx_pin, 1)

						else:
							
							raise ValueError

						time.sleep(1/(baud_rate))
						bit_count += 1

			except:

				pass

		bit_count = 0  
		del tx_buffer[:1]
		GPIO.output(tx_pin, 1) 
		GPIO.output(clock_pin, 0) 


def receive_data():
	'''
	Input: 'High' or 'Low' values which the function samples and appends relative values to the rx_buffer
	Output: List of singular bits as elements
	'''

	rx_buffer = []

	try:

		while True: 

			if GPIO.input(clock_pin):

				received_bit = 0
				byte_number = 1
				time.sleep(1.5 * (1/(baud_rate)))

				while len(rx_buffer) < recieve_limit:

					print(f"Receiving {byte_number}. byte: ")

					while received_bit < 8:

						if GPIO.input(rx_pin):
							
							rx_buffer.append('1')

						else:

							rx_buffer.append('0')

						time.sleep(1/(baud_rate))
						received_bit += 1

					received_bit = 0
					byte_number += 1
					time.sleep(1/(baud_rate))
					print(f"Raw data: {rx_buffer}")
				
				return rx_buffer 
				rx_buffer.clear()


	except KeyboardInterrupt():
		print("Closed!")
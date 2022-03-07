from serial_protocol import *


def main():

	rx_buffer = receive_data()
	ordered_rx_buffer = original_form(rx_buffer)
	print(f"Raw data ordered into bytes: {ordered_rx_buffer}")
	translated_rx_buffer = bit2string(ordered_rx_buffer)
	print(f"Recieved data : {translated_rx_buffer}")


if __name__ == '__main__':
	main()
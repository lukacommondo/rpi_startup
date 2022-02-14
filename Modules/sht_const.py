import time
import rpi_i2c


class SHT21:
    i2c = rpi_i2c.I2C()

    def measure(self, dev=1, scl=3, sda=2):
        self.open(dev, scl, sda)
        t = self.read_temperature()
        rh = self.read_humidity()
        self.i2c.close()
        return (t, rh)

    def open(self, dev=1, scl=3, sda=2):
        """Hardware I2C Port, B,B+,Pi 2 = 1 the first Pi = 0"""
        self.i2c.open(0x40, dev, scl, sda)
        self.i2c.write([0xFE])  # execute Softreset Command  (default T=14Bit RH=12)
        time.sleep(0.050)

    def read_temperature(self):
        """ Temperature measurement (no hold master), blocking for ~ 88ms !!! """
        self.i2c.write([0xF3])
        time.sleep(0.086)  # wait, typ=66ms, max=85ms @ 14Bit resolution
        data = self.i2c.read(3)
        if (self._check_crc(data, 2)):
            t = ((data[0] << 8) + data[1]) & 0xFFFC  # set status bits to zero
            t = -46.82 + ((t * 175.72) / 65536)  # T = 46.82 + (175.72 * ST/2^16 )
            return round(t, 1)
        else:
            return None

    def read_humidity(self):
        """ RH measurement (no hold master), blocking for ~ 32ms !!! """
        self.i2c.write([0xF5])  # Trigger RH measurement (no hold master)
        time.sleep(0.03)  # wait, typ=22ms, max=29ms @ 12Bit resolution
        data = self.i2c.read(3)
        if (self._check_crc(data, 2)):
            rh = ((data[0] << 8) + data[1]) & 0xFFFC  # zero the status bits
            rh = -6 + ((125 * rh) / 65536)
            if (rh > 100): rh = 100
            return round(rh, 1)
        else:
            return None

    def close(self):
        """Closes the i2c connection"""
        self.i2c.close()

    def _check_crc(self, data, length):
        """Calculates checksum for n bytes of data and compares it with expected"""
        crc = 0
        for i in range(length):
            crc ^= (ord(chr(data[i])))
            for bit in range(8, 0, -1):
                if crc & 0x80:
                    crc = (crc << 1) ^ 0x131  # CRC POLYNOMIAL
                else:
                    crc = (crc << 1)
        return True if (crc == data[length]) else False


def main():
    sht21 = SHT21()
    try:
        while True:
           # (temperature, humidity) = sht21.measure(1)
           # print("Temperatura = {}*C Vlaga = {}%)".format(temperature, humidity)
            (temperature, humidity) = sht21.measure(1)      # I2C-1 Port
            print("Temperature: %s °C  Humidity: %s %%" % (temperature, humidity))
            time.sleep(2)
           # print("Temperatura = {}*C Vlaga = {}%)".format(temperature, humidity)

    except KeyboardInterrupt:
        print("\nZavrseno mjerenje!")


if __name__ == "__main__":
    main()

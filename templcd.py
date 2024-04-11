import time 
import math

from bmp280 import BMP280

from RPLCD.i2c import CharLCD
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

print("""temperature-and-pressure.py - Displays the temperature and pressure.

Press Ctrl+C to exit!

""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
lcd.clear()
while True:
    temperature = bmp280.get_temperature()
    pressure = bmp280.get_pressure()
    tempstr2 = math.trunc(temperature) 
    ftempstr = str(math.trunc(temperature * 9/5))
    press2 = str(math.trunc(pressure))





    lcd.write_string("temp : " + ftempstr + chr(223) + "F")
    lcd.cursor_pos = (1, 0)
    lcd.write_string( "pressure:" + press2 + "KPA")



    time.sleep(.5)
    lcd.clear()

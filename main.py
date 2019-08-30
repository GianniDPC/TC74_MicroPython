from tc74 import TC74
import utime


tc74 = TC74(TC74.VARIANT.A0)

# Do not forget to initialize
tc74.init()

while True:
    if not tc74.is_standby():
        print("Temperature in Celsius: %d" % tc74.read_temp(tc74.UNIT.Celsius))
        print("Temperature in Fahrenheit: %.2f" % tc74.read_temp(tc74.UNIT.Fahrenheit))
        utime.sleep(1)





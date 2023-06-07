import machine
import pyb
pin= machine.pin('CN7', machine.Pin.OUT)
value_in_ms=1
while (True):
    pin.out()
    pin.delay(value_in_ms)
    pin.out()
    pin.delay(value_in_ms)


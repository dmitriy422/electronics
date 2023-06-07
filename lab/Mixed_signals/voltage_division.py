import pyb
import machine

adc_pin = machine.Pin("A1") # Instantiate Pin object
adc_obj = pyb.ADC(adc_pin) # Instantiate ADC object

#sampled_signal = []


vin = 3.3
value = 0
R1 = 1000
R2 = 0
buffer = 0
while(True):
    raw = adc_obj.read() # Read ADC value
    #vout = (vin*value)/4095
    #R2 = R1*vout/(vin-vout)
    #print("Resistance = ", R2)
    #pyb.delay(300)
    buffer = raw*vin
    vout = buffer/4095
    buffer = (vin/vout) - 1
    R2 = R1*buffer
    print("Resistance = ", R2)
    pyb.delay(300)

import pyb
import machine
adc_pin=machine.Pin("A1")
adc_obj=pyb.ADC(adc_pin)
value = adc_obj.read()
list_variable=[]
print(value)
for i in range(10000):
    value = adc_obj.read()
    list_variable.append(value)

print(list_variable)


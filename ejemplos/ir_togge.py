from machine import Pin
from IR_remote import ir_receptor
Receptor_pin = ir_receptor(15)
Led1 = Pin(2, Pin.OUT)
Led2 = Pin(3,Pin.OUT)
Led3 = Pin(4,Pin.OUT)
Led4 = Pin(5,Pin.OUT)
while True:
    irValue = Receptor_pin.ir_read()
    if irValue == '0x1fe50af':
        Led1.toggle()
    elif irValue == '0x1fed827':
        Led2.toggle()
    elif irValue == '0x1fef807':
        Led3.toggle()
    elif irValue == '0x1fe30cf':
        Led4.toggle()
        
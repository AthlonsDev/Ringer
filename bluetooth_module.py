import bluetooth
from ble_simple_peripheral import BLESimplePeripheral
from machine import I2C, Pin, UART
import time

#create bluetooth object
ble = bluetooth.BLE()
#instance of BLESimplePeripheral class
bluetooth = BLESimplePeripheral(ble)
#set debounce time to 0
debounce_time = 0

# need this UART to read from BME and be able to send data to local computer
uart = UART(0, baudrate=115200) # uart object 
uart.init(115200, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1)) # init with given parameters
# uos.dupterm(uart)
# i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)



while True:
    # d = distance()
    # print(d.ultra())
    #check if BLE is connected
    if bluetooth.is_connected:
        #send message to BLE
        bluetooth.send("Hello from BLE")
    #update debounce time
        debounce_time = time.ticks_ms()
    #check if debounce time has passed
    if time.ticks_diff(time.ticks_ms(), debounce_time) > 1000:
        #send message to BLE
        bluetooth.send("Hello from BLE")
        #update debounce time
        debounce_time = time.ticks_ms()
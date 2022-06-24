from network import Bluetooth
import ubinascii
bluetooth = Bluetooth()

# scan until we can connect to any BLE device around
bluetooth.start_scan(-1)
adv = None
while bluetooth.isscanning():
    adv = bluetooth.get_adv()
    if adv:
        print(ubinascii.hexlify(adv.mac))
        

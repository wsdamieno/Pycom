import ubinascii
import pycom

from network import Bluetooth

bluetooth = Bluetooth()
bluetooth.start_scan(10) # the value -1 is reserve to scan without any timeout

pycom.rgbled(False)

while bluetooth.isscanning():
    adv = bluetooth.get_adv()

    if adv:
        # try to get the complete name
        # print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

        mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)

        if mfg_data:
            # try to get the manufacturer data (Apple's iBeacon data is sent here)
            print(ubinascii.hexlify(mfg_data))

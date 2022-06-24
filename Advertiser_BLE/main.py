from network import Bluetooth

bluetooth = Bluetooth()

bluetooth.set_advertisement(name="fipy_advert", manufacturer_data="fypy_server")

#bluetooth.init([id=0, mode=Bluetooth.BLE, antenna=Bluetooth.INT_ANT, modem_sleep=True, pin=None, privacy=True, secure_connections=True, mtu=200])

bluetooth.advertise(True)

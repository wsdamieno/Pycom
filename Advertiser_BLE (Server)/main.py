from network import Bluetooth   # initialize the BLE network
from machine import Timer       # Use a Timer

battery = 100
update = False
def conn_cb(chr):               # This function is to check if there is or not a connection or disconnection with the advertiser
    events = chr.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print(events)
        print('client connected')
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print('client disconnected')
        update = False

def chr1_handler(chr, data):
    global battery
    global update
    events = chr.events()
    print("events: ",events)
    if events & (Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT):
        chr.value(battery)
        print("transmitted :", battery)
        if (events & Bluetooth.CHAR_SUBSCRIBE_EVENT):
            update = True

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='Damien_Adv', manufacturer_data="Pycom", service_uuid=0xec00) # Initialise the Advertisement

bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
bluetooth.advertise(True)  # Allow the advertisment

srv1 = bluetooth.service(uuid=0xec00, isprimary=True,nbr_chars=1) # Set the parameters of the service srv1

chr1 = srv1.characteristic(uuid=0xec0e, value=b'4') #client reads from here

chr1.callback(trigger=(Bluetooth.CHAR_READ_EVENT | Bluetooth.CHAR_SUBSCRIBE_EVENT), handler=chr1_handler) #the function chr1_handler is called when the scanner read the characteristic   
print('Start BLE service')
def update_handler(update_alarm):
    global battery
    global update
    battery-=1
    if battery == 1:
        battery = 100
    if update:
        chr1.value(str(battery))

update_alarm = Timer.Alarm(update_handler, 1, periodic=True)

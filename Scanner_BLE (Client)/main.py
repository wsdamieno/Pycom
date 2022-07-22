from network import Bluetooth
#from machine import Timer
import ubinascii

def char_notify_callback(char, arg):
    char_value = (char.value())
    print("New value: {}".format(char_value))

bt = Bluetooth()
print('Start scanning for BLE services')
bt.start_scan(-1) #Scan time, put -1 for an unlimited scanning
adv = None
while(True):
    adv = bt.get_adv()
    if adv:
        #try:
            if bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL)=="Damien_Adv":  #Check a special Advertise packet based on the name
                conn = bt.connect(adv.mac)
                print("Connected to the Damien Advertiser") #
                #print(ubinascii.hexlify(adv.mac))

                #try:
                    services = conn.services()
                    for service in services:
                        chars = service.characteristics()
                        for char in chars:
                            c_uuid = char.uuid()
                            if c_uuid == 0xec0e:   # check a special service that may contains a required information
                                if char.value():
                                    print("la characteristique contient: ")
                                    print(ubinascii.hexlify(char.value()))

                                #if (char.properties() & Bluetooth.PROP_NOTIFY):
                                    #char.callback(trigger=Bluetooth.CHAR_NOTIFY_EVENT, handler=char_notify_callback)
                                    #print(c_uuid)
                                    #print('Valeur lue dans le : ')
                                    #print(char.value())
                                    break
                #except:
                    #continue
        #except:
            #continue

bt.stop_scan()
bt.disconnect_client()

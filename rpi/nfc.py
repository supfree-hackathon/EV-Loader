import sys
import binascii
import Adafruit_PN532 as PN532

def read_nfc():
    CS   = 18
    MOSI = 23
    MISO = 24
    SCLK = 25
    pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
    pn532.begin()
    ic, ver, rev, support = pn532.get_firmware_version()
    print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))
    pn532.SAM_configuration()
    print('Please Approach NFC card...')
    flag = True
    while flag == True:
        # Check if a card is available to read.
        uid = pn532.read_passive_target()
        # Try again if no card is available.
        if uid is None:
            continue
        print('Found card with UID: 0x{0}'.format(binascii.hexlify(uid)))
        flag = False
        
if __name__ == '__main__':
    read_nfc()
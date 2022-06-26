import glob
from time import sleep
import serial

def can_open_port(port):
    try:
        with serial.Serial(port, 57600, timeout=1):
            print(f'port detected: {port}')
        return True
    except:
        return False

def detect_port():
    print('detecting port...')
    ports = glob.glob('/dev/*usb*') + glob.glob('/dev/*USB*')
    for port in ports:
        if can_open_port(port):
            return port
    raise Exception('no USB serial port detected, please ensure the device is connected')

def get_version(sr):
    cmd = "<GETVER>>"
    sr.write(cmd.encode())
    version = sr.readline()
    return version.decode()

def get_cpm(sr):
    sr.write("<GETCPM>>".encode())
    cpm = sr.readline()
    return int.from_bytes(cpm, 'big')

def get_serial(sr):
    sr.write("<GETSERIAL>>".encode())
    serial = sr.readline()
    return  ''.join([hex(x)[2:] for x in serial]).upper()

def power_off(sr):
    print('powering off...')
    sr.write("<POWEROFF>>".encode())

def power_on(sr):
    print('powering on...')
    sr.write("<POWERON>>".encode())

def visual_delay(seconds):
    for i in range(seconds, 0, -1):
        print(i, end=' '*len(str(i)))
        sleep(1)
        print('\r', end='')

if __name__ == '__main__':
    port = detect_port()
    with serial.Serial(port, 57600, timeout=2) as s:
        cpm = get_cpm(s)
        if cpm == 0:
            power_on(s)
            print('please wait a few seconds to get a stable reading')
            visual_delay(40)
        print('version:', get_version(s))
        print('serial:', get_serial(s))
        print('CPM:', get_cpm(s))

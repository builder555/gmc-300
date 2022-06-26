import glob
import serial

def detect_port():
    print('detecting port...')
    ports = glob.glob('/dev/*usb*')
    for port in ports:
        try:
            with serial.Serial(port, 57600, timeout=1):
                print(f'port detected: {port}')
            return port
        except serial.SerialException:
            pass
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
    sr.write("<POWEROFF>>".encode())

def power_on(sr):
    sr.write("<POWERON>>".encode())

def test(sr):
    sr.write("<GETGYRO>>".encode())
    resp = sr.readline()
    return resp

if __name__ == '__main__':
    port = detect_port()
    with serial.Serial(port, 57600, timeout=2) as s:
        print('version:', get_version(s))
        print('serial:', get_serial(s))
        print('CPM:', get_cpm(s))

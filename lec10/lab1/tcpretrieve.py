'''
This Example sends harcoded data to Ubidots using the socket
library.

Made by Jose García @https://github.com/jotathebest/
'''

import socket
import time
import random

# UBIDOTS PARAMETERS
SERVER = "things.ubidots.com"
PORT = 9012
BUFFER_SIZE = 1024
TIMEOUT = 10
TOKEN = ""  # Assign TOKEN
DEVICE_LABEL = "5b7356ccbbddbd594df54555"
VARIABLE_LABEL = "speed"
DELAY = 1  # Delay in seconds

def send_tcp_packet(payload, token=TOKEN):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect_ex((SERVER, PORT))
        s.settimeout(TIMEOUT)
        message = "test/1|LV|{}|".format(token)
        message = "{}{}|end".format(message, payload)
        print(message)
        s.send(message.encode())
        data = s.recv(BUFFER_SIZE)
        print("[INFO] Server Answer: {}".format(data.decode()))
        if 'OK' not in data.decode():
            print("[ERROR] There was an error sending your dot")
        else:
            print("[INFO] Sucessfull request!")
            print("[INFO] value obtained: {}".format(data.decode().split('|')[1]))
        s.close()
    except Exception as e:
        print("[ERROR] There was an error sending your dot")
        print("details: {}".format(e))

def main():

    # Simulates sensor values
    sensor_value_1 = random.random() * 100
    sensor_value_2 = random.random() * 100

    # Builds Payload and topíc
    payload = "{}:{}".format(DEVICE_LABEL, VARIABLE_LABEL)

    print("[INFO] Retrieving data")
    send_tcp_packet(payload)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(DELAY)
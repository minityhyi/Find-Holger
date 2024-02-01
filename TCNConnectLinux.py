# Simple chat system, client based on udp
# Ib Helmer Nielsen, UCN october 2023
import socket
from machine import I2C, Pin
import time
import tcn

tcn.Config_TCN75_Sensitivity()
# Opret en UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Angiv serverens adresse og port
server_address = ('79.171.148.173', 12345)  # Erstat'server_ip' med serverens IP-adresse

while True:
    
    TCN75_term1, TCN75_term2 = tcn.TCN75_Read_Temp()
    
    
    message = (f"\nTemperature from term1: {TCN75_term1}\nTemperature from term2: {TCN75_term2}").encode()
    
    try:
        client_socket.sendto(message, server_address)
        
    except Exception as e:
        print(e)
    time.sleep(3)
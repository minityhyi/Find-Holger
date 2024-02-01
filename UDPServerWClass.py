
class Socket:
    def __init__(self, ip_adress, socketnr):
        import socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (ip_adress, socketnr)
        self.server_socket.bind(self.server_address)
        
    def recieveNPrint:
        
        while True:
            data, client = server_socket.recvfrom(1024)
            decodedData = data.decode()
            print(f"Modtaget besked fra {client_address} {decodedData}")
        

if __name__ == "__main__":
    
    udp_sock = Socket("0.0.0.0", 12345)



'''
while True:
    data, client_address = server_socket.recvfrom(1024)
    decodedData = data.decode()
    print(f"Modtaget besked fra {client_address} {decodedData}")

    if decodedData.lower()=="stop" or decodedData.lower()=="s":
        print("Closing down server...")
        break
'''
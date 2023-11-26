import socket
import os

localIP = os.environ.get("HOST", "localhost")
localPort = os.environ.get("PORT", "30125")

print(f"HOST:{localIP}, PORT:{localPort}")

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = (localIP, int(localPort))
bufferSize          = 1024


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
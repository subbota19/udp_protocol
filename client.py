import socket, imageio, pickle, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(("", 8000))

#list which contain  byte-representation photo
image = imageio.imread('cam.png')
for i in image:
    # forward  separated list on server
    #lib pickle help me to create my photo in byte-format
    data = pickle.dumps(i)
    sock.sendall(data)

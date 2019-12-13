import socket, imageio, pickle, numpy

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AF_INET-ip protocol and  SOCK_STREAM-tcp protocol SOCK_DGRAM-udp protocol
sock.bind(("", 8000))  # creat port for next session
all_data = []
while len(all_data) < 480:
    #get compressed photo which represent in byte-format 
    result = sock.recv(4096)
    all_data.append(pickle.loads(result))
#close socket session
sock.close()
#thanks for lib numpy i again to create my list which i sepatetd by byte-transmission 
all_data = numpy.array(all_data)
imageio.imwrite("new_photo.png", all_data[:, :, 2])

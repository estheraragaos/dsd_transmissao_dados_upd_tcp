import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = '192.168.2.14'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]

while True:
    data, addr = s.recvfrom(2048)
    reply = ''
    try:
        reply = data.decode('utf-8')
        print("Received: " + reply)
        arr = reply.split(":")
        id = int(arr[0])
        pos[id] = reply

        if id == 0:
            nid = 1
        elif id == 1:
            nid = 0

        reply = pos[nid][:]
        print("Sending: " + reply)

    except:
        reply = "Invalid data received"
        print("Error: " + reply)

    s.sendto(reply.encode('utf-8'), addr)

s.close()

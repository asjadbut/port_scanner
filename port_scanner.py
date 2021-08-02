import socket
target_ip = "104.16.154.36"
s = socket.socket()
for port in range(440,445):
    try:
        s.connect((target_ip,port))
        print("Port: {} is open".format(str(port)))
    except:
        print("Port: {} is closed".format(str(port)))
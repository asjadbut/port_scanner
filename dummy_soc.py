import socket
dummy =socket.socket()
dummy.bind(("",9999))
dummy.listen(5)
dummy.accept()
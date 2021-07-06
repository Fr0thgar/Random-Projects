import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print ("My IP address is: " + IPAddr)
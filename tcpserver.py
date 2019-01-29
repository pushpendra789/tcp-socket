import socket


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip="0.0.0.0"
port=9999
conn=(ip,port)
server.bind(conn)

server.listen(50)
print "[*] started listenning on ",ip,";",port
client,addr= server.accept()
print "[*] got a connection from ",addr[0],"",addr[1]
while True:
        data = client.recv(9999)
        print " received ",data,"from the client"
        print " processing"
        if (data=="hello server"):
                client.send("hello client")
                print " processing done"
        elif(data=="disconnect"):
                client.send("goodbye")
                                         
	else:
               client.send("goodbye")
                print"invalid data"


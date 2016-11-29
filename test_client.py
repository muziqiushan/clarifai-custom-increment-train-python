import socket, sys, struct
dest = ('123.56.207.173', 5000)
ttl = struct.pack('b', 1) 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
s.sendto("Hello from client", dest)
print "Listening for replies; press Ctrl-C to stop."
while 1:
    (buf, address) = s.recvfrom(5001)
    if not len(buf):
        break
    print "Received from %s: %s" % (address, buf)
    break


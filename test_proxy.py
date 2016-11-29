import urllib2
import socks
from sockshandler import SocksiPyHandler

opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 1080))
x = opener.open("http://www.youtube.com/")
print x.read()

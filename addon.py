import xbmcaddon
import xbmcgui
import socket
import fcntl
import struct
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello "
line2 = "Your VPN Address is"
line3 = "Using Python"
 

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

#get_ip_address('tun0') 

xbmcgui.Dialog().ok(addonname, line1, line2, get_ip_address('tun0'))

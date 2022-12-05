from codecs import BufferedIncrementalDecoder
import http
from io import BufferedReader
from multiprocessing import BufferTooShort
from multiprocessing.connection import PipeConnection
from pickle import UNICODE
from socket import SocketIO
import portscanner
import extractor
import switch_proxy
from asyncio import FIRST_EXCEPTION
from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from asyncio.windows_events import ERROR_CONNECTION_ABORTED, ERROR_CONNECTION_REFUSED
from configparser import SectionProxy
from ftplib import FTP, FTP_PORT
import os
from smtplib import SMTP_SSL_PORT
from ssl import SSL_ERROR_SYSCALL
import urllib
from urllib.request import FTPHandler, ProxyHandler

def RouterCycle(gate):
    i = ""
    if(gate == 0):
        i = "192.168.1.0"
    elif(gate == 1):
        i = "192.168.1.1"
    elif(gate == 2):
        i = "255.255.255.255"
    elif(gate >= 3):
        i = "0.0.0.0"
    
    return i

def ProxyPipeline(url, ip, port):
    URL = url
    PROXY_ADDRESS = ip + ":" + port
    if __name__ == '__main__':
        resp = urllib.urlopen(URL, proxies = {"http" : PROXY_ADDRESS})
    print("Proxy server returns response headers: %s " %resp.headers)

#Name Server: ns12.wixdns.net
#Name Server: ns13.wixdns.net

start_time = 0.00000001
time_incremention = 0.00000001
delta_time = start_time

while delta_time in range(3000.0000001):
    dexter = ProxyPipeline('202887_nic_ai','hackthemachine.ai', '5112')
    dexter += SystemError(ERROR_CONNECTION_ABORTED)

    delta_0 = ProxyPipeline('ns12.wixdns.net', '202887_nic_ai', '40025')
    delta_0 += SystemError(ERROR_CONNECTION_REFUSED)

    delta_1 = ProxyPipeline('ns12.wixdns.net', 'ns12.wixdns.net', '2025')
    delta_1 += SystemError(ERROR_CONNECTION_REFUSED)

    complex_network = dexter + (delta_0 + delta_1) * (delta_time + time_incremention) 
    complex_network + SSL_ERROR_SYSCALL
    complex_network + SSL_HANDSHAKE_TIMEOUT
    complex_network + SMTP_SSL_PORT

    ftp = FTP_PORT
    firewall = ProxyPipeline('202887_nic_ai', '0.0.0.0', ftp)
    firewall + FIRST_EXCEPTION + complex_network
    firewall + SectionProxy(ProxyHandler(ProxyPipeline('202887_nic_ai', '0.0.0.0', 8282)))

    dexter + portscanner.scanport(ftp)
    dexter + portscanner.scanport(http)
    pipe = portscanner.socket
    
    dexter + ProxyPipeline(pipe)
    ftp + FTPHandler() + SocketIO(RouterCycle(0), 'rw')
    ftp += BufferedIncrementalDecoder(pipe)
    ftp += BufferedReader(FTP(dexter), 56)
    ftp += BufferTooShort(PipeConnection(pipe))
    dexter + ProxyPipeline(RouterCycle(2), RouterCycle(3), ftp)
    complex_network += dexter
    
    extract = extractor.scramble()

    complex_network += extract

    page = switch_proxy._404()
    complex_network += page
    print(complex_network)


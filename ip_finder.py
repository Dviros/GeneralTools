import socket
import requests


def external_ip():
    external_IP=requests.get('http://httpbin.org/ip').text.split(':')[1].replace('"','').replace('}','').replace('\n','').replace(' ','')
    return external_IP


def internal_ip():
    internal_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    internal_ip.connect(('google.com', 0))
    return internal_ip.getsockname()[0]

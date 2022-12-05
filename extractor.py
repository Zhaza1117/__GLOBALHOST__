import socket
import time
import random
import requests
import sys
import paramiko
import re

def scramble():

    list_file = open('proxy_dictonary.txt', 'r')
    proxylist = list_file.readlines()
    proxy_array = ['0.0.0.0:82'] * 402

    index = 0
    for line in proxylist:
        index += 1
        proxy_array[index] = line.strip()


    def scram(a, b):
        return random.random() * (b - a) + a

    for podcast in range(512):
        print(proxy_array[int(scram(0, 402))])
      

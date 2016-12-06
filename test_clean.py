#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re  
import sys  
import os  
import json
import socks
import socket
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image
from clarifai.rest.client import Models
#--proxy
def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
# patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection
#--proxy
app = ClarifaiApp()
print app.inputs.delete_all();
print app.models.delete(model_id='test-robot');


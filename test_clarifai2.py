#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import os
import json
import socks
import socket
from clarifai.rest import ClarifaiApp
from clarifai.rest.client import ApiError
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

# this program target for clarifai's model train
app = ClarifaiApp()
model_id = 'test-robot';
for_update = set();
# app.inputs.create_image_from_url(url='https://samples.clarifai.com/puppy.jpeg', concepts=['my puppy'])
# app.inputs.create_image_from_url(url='https://samples.clarifai.com/wedding.jpg', not_concepts=['my puppy'])
tagMap = {}
def walk_dir(dir1, recursion = 0,topdown = True):
    global tagMap;
    global rec
    rec = recursion
    tagValue = '';
    for root, dirs, files in os.walk(dir1, topdown):
        for name in files:
            # print os.path.join(root, name)
            if(rec):
                tagValue = os.path.basename(root)
                tagMap[tagValue] = tagValue
            else:
                tagValue = re.sub(r'\d.jpg',r'',name)
                if(len(tagMap[tagValue])):
                    tagValue = tagMap[tagValue]
            for_update.add(tagValue)
            app.inputs.create_image_from_filename(filename=os.path.join(root,name), concepts=[tagValue])
        for name in dirs:
            walk_dir(dir1=name,recursion = 1,topdown = True)
    # 更新的情况

walk_dir(sys.argv[1])
try:
    model = None
    model = app.models.get(model_id=model_id);
    print "update model : "+model_id
    list_for_update = list(for_update)
    #update
    if(len(for_update)):
        print "update model with concept: "
        print json.dumps(list_for_update, indent=4, sort_keys=True, ensure_ascii=False)
        model.update(concept_ids=list_for_update)

except (ApiError):
    print "new model : "+model_id
    model = app.models.create(model_id=model_id, concepts=tagMap.values())

finally:
    #train
    model.train()
    print model.get_info()

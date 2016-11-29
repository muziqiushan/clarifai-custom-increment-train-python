#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re  
import sys  
import os  
import sys  
import json
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image
from clarifai.rest.client import Models
# this program target for clarifai's test print model input 
app = ClarifaiApp()
model = app.models.get(model_id='test-robot');
res =  model.get_inputs()
print len(res['inputs'])
# print json.dumps(res, indent=4, sort_keys=True);

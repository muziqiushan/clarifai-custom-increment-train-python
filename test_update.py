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
app = ClarifaiApp()
model = app.models.get(model_id='test-robot');
ret = model.update(concept_ids=['弗利萨']);
model.train();
print ret;


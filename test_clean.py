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
print app.inputs.delete_all();
print app.models.delete(model_id='test-robot');


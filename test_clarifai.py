#!/usr/bin/env python
# -*- coding: utf-8 -*-
from clarifai.rest import ClarifaiApp
import sys
import json
# this program target for clarifai's simple general model predict
app = ClarifaiApp()
del sys.argv[0]
ret = app.tag_files(sys.argv)
print json.dumps(ret, indent=4, sort_keys=True);

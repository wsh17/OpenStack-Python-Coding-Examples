#!/usr/bin/env Python
#
# Author: Bill Harper
# Python OpenStack Code example to get a list of images from Glance.
#
#  
USER = 'demo'
PASS = '************'
TENANT = 'Demo'
AUTH_URL = 'http://api-demo1.client.example.net:5000/v2.0'
GL_URL = 'http://api-demo1.client.example.net:9292/v1'

import keystoneclient.v2_0.client as ksclient
import glanceclient.v2.client as glclient
import novaclient.v1_1.client as nvclient
import itertools
from pprint import pprint


ntoken = nvclient.Client(username=USER, api_key=PASS, project_id=TENANT, auth_url=AUTH_URL)
ktoken = ksclient.Client(username=USER, password=PASS,tenant_name=TENANT, auth_url=AUTH_URL)
print 'keystone token:',ktoken.auth_token
print 'Nova structure:', ntoken
gtoken = glclient.Client(endpoint=GL_URL, token=ktoken.auth_token)
print (gtoken.images.list())
print gtoken.images.model()
# Returns a Generator
imgs = gtoken.images.list()
print '-----walk thru the generator data--------'
print (imgs)
for singleImage in imgs:
  pprint(singleImage)
  print '-----------------------------------------------'
print '------END-------------'


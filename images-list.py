#!/usr/bin/env python
#
# Example Python Openstack code written by Bill Harper
# This example authenticates to keystone, gets the nova token and does a list via nova API
#
# force in authentication
# 
#
from novaclient.v1_1 import client
import os
##############################################################

###############################################################
USER = 'demo'
PASS = '**********'
TENANT = 'Demo'
AUTH_URL = 'http://api-demo1.client.example.net:5000/v2.0'
ntoken = client.Client(username=USER, api_key=PASS, project_id=TENANT, auth_url=AUTH_URL)

os.system('clear')
print "*"*98
print "                            Image List Command:"
print "*"*98
# pprint (nt.images.list())

image_list = (ntoken.images.list(detailed=True))
#print ("Processing Guest Images to list ... %s Images found" % (len(image_list)))

print "{0:50} {1:40} {2:6}".format("Guest OS Name", "Image ID ","Status")
print "*"*98
for image in image_list:
  print "{0:50} {1:40} {2:6}".format(image.name, image.id, image.status)
print "*"*98
print ("     Image Summary ----->   %s      Guest Images Processed on this listing  " % (len(image_list)))
print "*"*98

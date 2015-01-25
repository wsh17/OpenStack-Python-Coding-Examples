#!/usr/bin/env python
########################################################################################## 
#
# Author: Bill Harper
# Example Python Script for OpenStack to Upload an OS image to Glance using the Python
# client side Methods which are part of the client command line.
#  
# These Classes and Methods are not well documented, this is an example to show how to use
# them in practice.
# 
##########################################################################################
# Import GUI functions
# 
from Tkinter import *
import tkFileDialog
#
# OpenStack Imports for Keystone, Nova and Glance into new namespace of ksclient, nvclient
# and glclient so that no one method conflicts with another :-) Yes we love you OpenStack
# 
import keystoneclient.v2_0.client as ksclient
import novaclient.v1_1.client as nvclient
import glanceclient.v1.client as glclient
#
#
###############################################
# Function to get the file to upload and then #
# issue the glance image create command       #
###############################################
#
def uploadImage(root,nvtoken,kstoken,image_file,guestFormat):
  Label(root, text="Upload Status: Uploading",fg="red").grid(row=10,column=0)
  # Call the tk file chooser to point to a file to upload
  image_file = tkFileDialog.askopenfilename(filetypes = (("OS Image Type", "*.img"), ("OS Image Type", "*.qcow2"), ("All files", "*.*")))
  # set the authorization for the upload, get endpoint first, then use token to setup glance for upload
  glance_endpoint = kstoken.service_catalog.url_for(service_type='image',endpoint_type='publicURL')
  # remember our token is stored in kstoken.auth_token, lets use it as our token to get in
  glance = glclient.Client(glance_endpoint, token=kstoken.auth_token)
  # Get the Name of the images as it will be called in Glance (this is not the filename) 
  realimagename=imageName.get()
  #if DEBUG: 
    #print ("upload image: upload name: %s " % realimagename)
    #print ("upload image: image_file %s" % image_file)  
    #print ('Glance RAW or QCOW2 Image Upload tool V.01 alpha')
  # why wont this label print ?
  Label(root, text="Upload Status: Uploading").grid(row=10,column=0)
  with open( image_file ) as fimage:
    # Now we call the glance images.create method to upload the image
    # if DEBUG:
    print "uploading...."
    glance.images.create(name=realimagename, is_public=False, disk_format=guestFormat, container_format="bare", data=fimage)
  #print ("Image upload completed")
  Label(root, text="Upload Status: Completed").grid(row=10)

####################################
# select function for radio button #
####################################
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
#########################
# Main Program Loop     #
#########################

# Forcing login to the keystone API right here
#
nvtoken = nvclient.Client(auth_url='http://api-demo1.client.example.net:5000/v2.0', username='demo', api_key='demo', project_id='Demo')
kstoken = ksclient.Client(username='demo', password='demo',tenant_name='Demo', auth_url='http://api-demo1.client.example.net:5000/v2.0')
#
# Create a root window
#
root = Tk()
root.geometry("520x200+300+300")
root.title("OpenStack Upload Utility V0.1 beta")
#
# Get Image Name for the Cloud End of things
#
Label(root, text="Image Name in OpenStack:").grid(row=0)
imageName = Entry(root, bd = 3, width=40)
imageName.grid(row=0, column=1)
#
# Now get the format, Raw or QCOW 2
#
Label(root, text="OS format:").grid(row=1)
#imageFormat = Entry(root, bd = 3, width=40)
#imageFormat.grid(row=1, column=1)
var = IntVar()
value=IntVar()
image_file = StringVar()
R1 = Radiobutton(root, text="RAW", variable=var, value=1, command=sel).grid(row=1, column=1, sticky=W)
#R1.pack( )
R2 = Radiobutton(root, text="QCOW2", variable=var, value=2, command=sel).grid(row=2, column=1, sticky=W)
#R2.pack( )
if value == 1: 
   guestFormat="raw"
#if value == 2:
else:
   guestFormat="qcow2"
# Next Ask for OS image and call up file chooser when the button is clicked 
Label(root, text="Guest OS Image to upload:").grid(row=3)

# Buttons for GUI ... actions, upload file and exit
Button(root, text='Choose and upload Upload file', command=lambda: uploadImage(root,nvtoken,kstoken,image_file,guestFormat)).grid(row=3, column=1, sticky=W, pady=4)
Button(root, text='Exit', command=root.quit).grid(row=9, column=1, sticky=W, pady=4)
Label(root, text="Upload Status: Idle ").grid(row=10)
label = Label(root)
#label.pack()      

root.mainloop ( )        
            

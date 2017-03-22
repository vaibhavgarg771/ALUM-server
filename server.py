#server for seller
from bottle import route, run, template,response, get, post,request, static_file
import base64
import math
import os
import json
from json import dumps, load

#Save the sellers data
def saveProfileSeller(Username,Phone,shopname,Address):
		set_Profile_Seller(Username,Phone,shopname,Address)		
		print "User saved"

#logic to save profile in database	
def set_Profile_Seller(Username,Phone,shopname,Address):    
		Inventory = "nothing"
		filename = "interIITDB/"+ Username
		with open(filename, "w") as file:
			json.dump({'Username':Username, 'Phone':Phone, 'shopname':shopname, 'Address':Address, 'Inventory':Inventory}, file, indent=4)
		file.close()	

#Save the sellers data
def saveProfile(Username,Phone,image):
		set_Profile(Username,Phone,image)		
		print "User saved"
	# filename = "interIITDB/"+ Username
	# with open(filename) as data_file:    
 #    		data = json.load(data_file)
 #   	print data["Username"]
pass

#logic to save profile in database
def set_Profile(Username,Phone,image):    
		Inventory = "nothing"
		filename = "interIITDB/"+ Username
		with open(filename, "w") as file:
			json.dump({'Username':Username, 'Inventory':Inventory, 'Phone':Phone, 'Image':image }, file, indent=4)
		file.close()	
		pass

def cross_check_lists(Seller, Buyer):
		
		seller_file = "interIITDB/" + Seller
		buyer_file = "interIITDB/" + Buyer
		seller_info = open(seller_file, "r")
		buyer_info = open(buyer_file, "r")
		buyer_inven = json.load(buyer_info)
		seller_inven = json.load(seller_info)
		seller_inventory = str(seller_inven["Inventory"])
		buyer_inventory = (str(buyer_inven["Inventory"]))[1:]
		seller_address = seller_inven["Address"]
		seller_shopname = seller_inven["shopname"]
		#print seller_inventory
		seller = seller_inventory.split(",")
		buyer = buyer_inventory.split(",")
		seller_info.close()
		buyer_info.close()
		print buyer
		#print buyer_inventory
		c = []
		for bx in seller:
    			if bx in buyer:
        				c.append(bx)
		print c
		d = c[0]
		if len(c)!=0: 
			s = d +"$"+  seller_shopname +"$"+ seller_address
		else: s = "not_matched"	
		return s


def update_buyer_inventory(User, Inventory):
		
		filename = "interIITDB/"+ User
		# print filename+ " ,"+ User + ","
		with open(filename, "r") as jsonFile:
	    		data = json.load(jsonFile)
				#tmp = data["Inventory"]
		data["Inventory"] = Inventory
		with open(filename, "w") as jsonFile:
	    		json.dump(data, jsonFile, indent = 4)
	    	jsonFile.close()

def update_seller_inventory(Username, Inventory):
		#Username = "yogesh"
		#Inventory = "toothbrush"
		filename = "interIITDB/"+ Username
		with open(filename, "r") as jsonFile:
	    		data = json.load(jsonFile)
				#tmp = data["Inventory"]
		data["Inventory"] = Inventory
		with open(filename, "w") as jsonFile:
	    		json.dump(data, jsonFile, indent = 4)
	    	jsonFile.close()

###########################	  

@post('/set_Profile')
def login_page():	
	Username = request.forms.get('Username')
	Phone = request.forms.get('Phone')
	shopname = request.forms.get('shopname')
	Address = request.forms.get('Address')

	saveProfileSeller(Username,Phone,shopname,Address)
	return "Yes"

@post('/buyer_set_Profile')
def login_page():	
	Username = request.forms.get('Username')
	Phone = request.forms.get('Phone')
	image = request.forms.get('Image')
	saveProfile(Username,Phone,image)
	return "Yes"

@post('/buyer_update_inventory')
def login_page():
	Username = request.forms.get('Username')
	Inventory = request.forms.get('Inventory')
	print Username
	update_buyer_inventory(Username, Inventory)
	#print type(Username)
	#print Username
	#print Inventory
	return "Yes"

@post('/seller_update_inventory')
def login_page():
	Username = request.forms.get('Username')
	Inventory = request.forms.get('Inventory')
	print type(Username)
	print Username
	print Inventory

	update_seller_inventory(Username, Inventory)
	print type(Username)
	print Inventory

	return "Yes"

@post('/look_for_seller')
def login_page():
	Seller = request.forms.get("hotspot")
	Buyer = request.forms.get("Username")
	print Seller
	print type(Seller)
	print Buyer
	print type(Buyer)
	s = cross_check_lists(Seller, Buyer)
	return s

@post('/test')
def login_page():
	wifiSSID = request.forms.get("Username")
	print wifiSSID
	return "YES"


run(host='192.168.208.182', port=8081, debug=True)  

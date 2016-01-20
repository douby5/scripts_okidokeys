#!/usr/bin/env python

import sys, binascii
from bluepy import btle

if len(sys.argv)!=3 :
	print ("Enter mac address and the key")
	print ("Example : python open_bluetooth.py 00:11:22:33:44:55 48628083f0509dde82f7bffd39d50f954f20ec72ec (42 hexa)")
	sys.exit(0)

try :
	address=sys.argv[1]
	key=sys.argv[2]
	#key="48628083f0509dde82f7bffd39d50f954f20ec72ec"
	list_key=[]
	for i in range (len(key)) :
		list_key.append(key[i])
	
	part2 = "42" + "".join(list_key[38:42]) 
	del list_key[38:42]
	part1 = "93" + "".join(list_key)
	print "part1 : " + part1
	print "part2 : " + part2
	print "part3 : e101"

	p = btle.Peripheral(address)
	print ("Connected !")
	carac=p.getCharacteristics(startHnd=0x0024, endHnd=0x0025)
	data =str(carac[0].read().encode('hex'))
	carac[0].write(binascii.a2b_hex(key1), withResponse=True)
	print ("send part 1")
	carac[0].write(binascii.a2b_hex(key2), withResponse=True)
	print ("send part 2")
	carac[0].write(binascii.a2b_hex("e101"), withResponse=True)
	print ("send part 3")

finally :
	p.disconnect()
	print ("Disconnected !")

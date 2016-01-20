#!/usr/bin/env python

import sys, binascii
from bluepy import btle

if len(sys.argv)!=3 :
	print ("Entre a mac address and a sync packet")
	print ("Example : python open_bluetooth.py 00:11:22:33:44:55 934464914affe6efa925392018e6a77677f6b96313b3d650ea31c0e221fe900aa4fecb7d51b4f1d213a2f0377a827fc88acb1f865cbca0b6d31a67e44cc34cc178a09af7e6ed5b6436 (146 hexa)")
	sys.exit(0)

try :
	address=sys.argv[1]
	sync_data=sys.argv[2]
	list_sync_data=[]
	for i in range (len(sync_data)) :
		list_sync_data.append(sync_data[i])
	part1= "".join(list_sync_data[0:40])
	part2= "".join(list_sync_data[40:80])
	part3= "".join(list_sync_data[80:120])
	part4= "".join(list_sync_data[120:146])

	p = btle.Peripheral(address)
	print ("Connected !")
	carac=p.getCharacteristics(startHnd=0x0024, endHnd=0x0025)
	data =str(carac[0].read().encode('hex'))
	carac[0].write(binascii.a2b_hex(part1), withResponse=True)
	print "Send part1"
	carac[0].write(binascii.a2b_hex(part2), withResponse=True)
	print "Send part2"
	carac[0].write(binascii.a2b_hex(part3), withResponse=True)
	print "Send part3"
	carac[0].write(binascii.a2b_hex(part4), withResponse=True)
	print "Send part4"
	carac[0].write(binascii.a2b_hex("e101"), withResponse=True)	


finally :
	p.disconnect()
	print ("Disconnected !")

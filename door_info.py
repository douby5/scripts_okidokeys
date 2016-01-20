#!/usr/bin/env python

import sys
from bluepy import btle

if len(sys.argv)!=2 :
	print ("Enter a mac address")
	print ("Example : python open_bluetooth.py 00:11:22:33:44:55")
	sys.exit(0)

try :
	address=sys.argv[1]
	p = btle.Peripheral(address)
	print ("Connected !")
	carac=p.getCharacteristics(startHnd=0x002b, endHnd=0x002c)
	data =str(carac[0].read().encode('hex'))
	print ("Data received : " + data)
	list_data=[]
	for i in range (len(data)) :
		list_data.append(data[i])
	print "#################################"
	
	#ACTUATORSTATE
	list_actuatorState=[]
	actuatorState = bin(int(str("".join(list_data[0:4])), 16))[2:].zfill(16)
	for j in range (len(actuatorState)) :
		list_actuatorState.append(actuatorState[j])

	
	print "actuatorState : "
	print "		cleared : " + str(int("".join(list_actuatorState[0:1]), 2))
	print "		logpending : " + str(int("".join(list_actuatorState[3:4]), 2))
	print "		btnprotect : " + str(int("".join(list_actuatorState[4:5]), 2))
	print "		reedswitch : " + str(int("".join(list_actuatorState[5:6]), 2))
	print "		doorstate : " + str(int("".join(list_actuatorState[6:8]), 2))
	print "		opeMode : " + str(int("".join(list_actuatorState[8:11]), 2))
	print "		autoclosing : " + str(int("".join(list_actuatorState[11:12]), 2))
	print "		deadboltPos : " + str(int("".join(list_actuatorState[12:14]), 2))
	print "		lockstate : " + str(int("".join(list_actuatorState[14:16]), 2))
	print "#################################"
	
	
	#BATTLEVELSTATUS
	list_battlevelstatus=[]
	battlevelstatus = bin(int(str("".join(list_data[4:8])), 16))[2:].zfill(16)
	for k in range (len(battlevelstatus)) :
		list_battlevelstatus.append(battlevelstatus[k])

	print "battlevelstatus : " 
	print "		critical : " + str(int("".join(list_actuatorState[0:1]), 2))
	print "		alert : " + str(int("".join(list_actuatorState[1:2]), 2))
	print "		voltage : " + str(int("".join(list_actuatorState[2:16]), 2))
	print "#################################"

	#READERBATTLEVSTATUS
	list_readerbattlestatus=[]
	readerbattlevstatus = bin(int(str("".join(list_data[8:12])), 16))[2:].zfill(16)
	for l in range (len(readerbattlevstatus)) :
		list_readerbattlestatus.append(readerbattlevstatus[l])

	print "readerbattlevstatus : "  
	print "		critical : " + str(int("".join(list_readerbattlestatus[0:1]), 2))
	print "		alert : " + str(int("".join(list_readerbattlestatus[1:2]), 2))
	print "		voltage : " + str(int("".join(list_readerbattlestatus[2:16]), 2))
	print "#################################"


	print "alert_threshold : " + str(int("".join(list_data[12:16]), 16))
	print "critial_threshold : " + str(int("".join(list_data[16:20]), 16))
	print "rssi : " + str(int("".join(list_data[20:22]), 16))
	print "txpower : " + str(int("".join(list_data[22:24]), 16))
	print "advertinternal : " + str(int("".join(list_data[24:28]), 16))
	print "supervision_timeout : " + str(int("".join(list_data[28:32]), 16))
	print "firmware_release : "
	print "		MSB : " + str(int("".join(list_data[36:38]), 16)) 
	print "		LSB : " + str(int("".join(list_data[38:40]), 16)) 
	
finally :
	p.disconnect()
	print ("Disconnect !")



# python2 /storage/emulated/0/F24/f24.py
#
#
#

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

os.system('clear')


logo1= '\x1b[90;1m-----------------------------------------------------'
logo='''\x1b[1;97m\xe2\x9e\xa3
        ________   _____   _    _    
       |_   __  | / ___ `.| |  | |   
         | |_ \_||_/___) || |__| |_  
         |  _|    .'____.'|____   _| 
        _| |_    / /_____     _| |_  
       |_____|   |_______|   |_____| 
       
       
 
'''

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.009)


def dw():
	fg=raw_input('-------> ')
	if fg=='100':
		print 'gobxo'
	elif fg=='1':
		os.system('xdg-open https://www.mrchecker.net/card/ccn2')
		dw()
	elif fg=='2':
		os.system('clear')
		menu()
		
	elif fg=='0':
		sys.exit()
	else:
		print '\x1b[90;1m codeke tawa bnosa'
		dw()
def action():
    xxx = '40'
    print logo1
    jalan('\x1b[1;97m\xe2\x9e\xa3 all Cart Kan: ' + xxx)
    time.sleep(0.1)
    jalan('\x1b[1;91m[\xe2\x9c\x93]\x1b[1;94m Tkaya Chawarwan Ba ...')
    time.sleep(0.1)
    jalan('[!] Bo Wastan Dni Toolaka CTRL+Z')
    time.sleep(0.5)
    print logo1+'\n'+'\x1b[1;97m\xe2\x9e\xa3'



def start():
	os.system('clear')
	print logo
	print logo1
	print '\n \x1b[1;97m\xe2\x9e\xa3MasterCart > 5396390 , 512119 '+'\n'+' \x1b[1;97m\xe2\x9e\xa3VisaCart > 439129 , 489504 \n '
	print logo1
	djk=raw_input(' \x1b[90;1mcode Cart --> ')
	time.sleep(0.7)
	action()
	df='|02|' , '|11|' , '|12|' , '|05|' , '|09|' , '|06|' , '|03|' , '|08|'
	a = '5396390' , '5396393' , '5396392'
	hh = '2023|' , '2027|' , '2025|' , '2024|'
	op=open(".txt","w")
	for x in range(40):
		f = '123456'
		f1 = '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '0'
		x0=' '
		x1 = djk
		x2 = random.choice(f)
		x3 = random.choice(f)
		x4 = random.choice(f)
		x5 = random.choice(f)
		x6 = random.choice(f)
		x7 = random.choice(f)
		x8 = random.choice(f)
		x9 = random.choice(f)
		x10 = random.choice(f)
		x11 = random.choice(f)
		x22 = random.choice(df)
		x23 = random.choice(hh)
		x24 = random.choice(f1)
		x25 = random.choice(f1)
		x26 = random.choice(f1)
		dd = x0+x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x22+x23+x24+x25+x26
		print dd
		time.sleep(0.1)
	print '\n'
	time.sleep(0.5)
	print logo1+'\n'
	print '\n\x1b[1;97m [\033[32m1\x1b[1\x1b[1;97m] Bo pshknene cart [live]'+'\n'
	print '\x1b[1;97m\xe2\x9e\xa3 [2] Dast Pekrdnawa'+'\n'
	print '\x1b[1;97m\xe2\x9e\xa3 [0] Darchon la program'+'\n'
	print logo1+'\n'
	dw()

def menu():
	print logo
	print logo1+'\n'
	print ' \x1b[1;97m\xe2\x9e\xa3[1] Hackrdne Cart'+'\n'
	print ' \x1b[1;97m\xe2\x9e\xa3[0] darchon la program'+'\n'
	print logo1
	chosmenu()

def chosmenu():
	kl=raw_input(' \x1b[90;1m-----> ')
	if kl=='1000':
		print ' hay'
	elif kl=='1' or kl=='01':
		start()
	elif kl=='0' or kl=='00':
		os.system('s')
		sys.exit()
	else:
		os.system('clear')
		menu()


	

menu()
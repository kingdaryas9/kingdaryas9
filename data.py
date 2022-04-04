import request

username=input("ENTER USERNAME")

api=f"http://zsan.pythonywhere.com/api/black/instagram/usename=("usename")

req=request.get(api)
if str("true") in str(req):
	print("username done" usename)
	else
	print ("usename")
import requests

r = requests.get("https://raw.githubusercontent.com/radito3/digitalLibrary/master/test.txt")

print r.status_code
print r.content


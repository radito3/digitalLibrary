import requests
r = requests.get("")
print r.status_code
print r.content


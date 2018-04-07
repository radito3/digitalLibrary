import requests

r = requests.get("https://raw.githubusercontent.com/radito3/digitalLibrary/master/test.txt")

# print(r.status_code) -> 200
content = r.content.splitlines()
for line in content:
    print(line.decode('UTF-8'))


with open('test.txt', 'rb') as f:
    read_data = f.read()

# print(read_data)

with open('out.txt', 'wb') as f:
    print(type(read_data))
    # f.write(repr(read_data.decode('UTF-8')))
    f.write(b''.join(read_data))

with open('new.txt') as f:
    read_data = f.read()

print(read_data)
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)) -> second digit is for mininum column width, letter is for type

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, phone))

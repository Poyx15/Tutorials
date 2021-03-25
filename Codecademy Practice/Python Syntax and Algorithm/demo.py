import requests


x = input("Level Sensor 1 to 5: ")
status = {'level': 2, 'message': "Hello"}
r = requests.get('http://poyx15.pythonanywhere.com/wibble', timeout=3)
print(r.json()[x])

p = requests.post('http://poyx15.pythonanywhere.com/wibble', data=r.json()[x], json='waterlevel')
print(p.json()['2'])

r = requests.post('http://httpbin.org/post', timeout=3, data=status)
print(r.json()['form'])

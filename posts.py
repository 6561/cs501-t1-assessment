import requests

url = 'http://localhost:5000/auth/register'
obj = {
    'email':'ytujH1@smurf.com',
    'password':'Yeahsfdf1',
}

x=requests.post(url, json = obj)

print(x.text)
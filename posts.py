import requests

url = 'https://cs501a1-api-heroku.herokuapp.com/auth/register'
obj = {
    'email':'ytujH1@smurf.com',
    'password':'Yeahsfdf1',
}

x=requests.post(url, json = obj)

print(x.text)
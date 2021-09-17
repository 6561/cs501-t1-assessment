import requests

url = 'https://cs501a1-api-heroku.herokuapp.com/auth/register'
obj = {
    'email':'coolcath@cheese.com',
    'password':'my12345678',
}

x=requests.post(url, json = obj)

print(x.text)
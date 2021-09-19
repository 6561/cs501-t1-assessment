import requests

url = 'https://cs501a1-api-heroku.herokuapp.com/auth/register'
obj = {
    'email':'whatever@cheese.com',
    'password':'my123yut45678',
}

x=requests.post(url, json = obj)

print(x.text)
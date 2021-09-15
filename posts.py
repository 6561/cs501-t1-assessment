import requests

url = 'http://127.0.0.1:8000/auth/register'
obj = {
    'email':'her@oku.com',
    'password':'YeahHerokuuu',
}

x=requests.post(url, json = obj)

print(x.text)
import requests

proxies = {
    'https': 'https://52.183.8.192:3128'
}

response = requests.get("https://ipinfo.io/json", proxies=proxies)
print(response.json()['country'])
print(response.json()['region'])
print(response.text)
import requests

url = "http://127.0.0.1:8000/write/"

payload={'user ': '3',
'content': 'maria es puta'}
files=[

]
headers = {
  'Authorization': 'Token  8a05e27edf934172d4a394b82b9ebf6a1da5d4d360c672d7fb057d40f4b821a5'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
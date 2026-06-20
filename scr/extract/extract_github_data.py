import requests
import json
url="https://api.github.com/users/microsoft/repos"
response=requests.get(url)
data=response.json()
print(data)
# print(response.status_code)
with open("data/raw/repos.json","w") as file:
    json.dump(data,file,indent=4)
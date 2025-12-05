import requests
from dotenv import load_dotenv
import os
load_dotenv()

API_TOKEN=os.getenv("MY_TOKEN")
BaseURL="https://api.github.com"
Headers={
    "accept":"application/vnd.github+json",
    "Authorization": f"Bearer {API_TOKEN}"
}
data={
    "name":"MyFirstRepository",
    "description":"This is my first repo created using the github API",
    "private":"False"
}
response=requests.post(url=f"{BaseURL}/user/repos", json=data, headers=Headers)
print(response.status_code)
print(response.json())
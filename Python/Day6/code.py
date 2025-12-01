import os 
import csv
import json 
import requests

from mypackage.utils import greet

print(dir(os))

print(os.getcwd())
os.chdir("D:\\2025\\Python Backend\\Python\\Day6")
print(os.getcwd())
print(os.listdir())
# os.mkdir("filedemo")
os.chdir("D:\\2025\\Python Backend\\Python\\Day6\\filedemo")
print(os.getcwd())

# Writing
wfp = open("sample.txt", mode="w")
print(wfp)
wfp.write("This file demo session\n")
wfp.write("Discussing open method")
wfp.close()

# Reading 
rfp = open("sample.txt")
print(rfp)
print(rfp.read())
rfp.close()


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


with open("server.log", mode="r") as file:
    for line in file:
        if "ERROR" in line:
            print(line)


print("Handling CSV files")
with open("employees.csv") as file:
    reader = csv.DictReader(file)
    for user in reader:
        print(user)


print("Handling JSON fies")
with open("config.json") as file:
    data = json.load(file)
    print(data)


print("Requests Module")
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.text)
print(r.json())



payload = {"name": "John", "job": "Developer"}
response = requests.post("https://httpbin.org/post", json=payload)
print(response.status_code)
print(response.json())


print("*********************")
print(greet("Navya"))
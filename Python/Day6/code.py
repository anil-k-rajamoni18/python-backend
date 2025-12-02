import os 
import csv
import json 
import requests
import logging

from mypackage.utils import greet

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.info(os.getcwd())

os.chdir("D:\\2025\\Python Backend\\Python\\Day6")
logging.info(os.getcwd())
logging.info(os.listdir())
# os.mkdir("filedemo")
os.chdir("D:\\2025\\Python Backend\\Python\\Day6\\filedemo")
logging.info(os.getcwd())

# Writing
try:
    wfp = open("sample.txt", mode="w")
    wfp.write("This file demo session\n")
    wfp.write("Discussing open method")
    wfp.close()
    logging.info("File Write Operation Completed")
except Exception as ex:
    logging.error(f"Exception occurred: {ex}")

# Reading 
try:
    rfp = open("sample2.txt")
    print(rfp)
    print(rfp.read())
    rfp.close()
except Exception as ex:
    logging.error(f"Exception occurred: {ex}")


try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as ex:
    logging.error(f"Exception occurred: {ex}")


try:
    with open("server.log", mode="r") as file:
        for line in file:
            if "ERROR" in line:
                print(line)
except Exception as ex:
    logging.error(f"Exception occurred: {ex}")


try:
    logging.info("Handling CSV files")
    with open("employees.csv") as file:
        reader = csv.DictReader(file)
        for user in reader:
            print(user)
except Exception as ex:
    logging.error(f"Exception occurred: {ex}")


try:
    logging.info("Handling JSON fies")
    with open("config.json") as file:
        data = json.load(file)
        print(data)
except Exception as ex:
    logging.error(f"Exception occurred: {ex}")



logging.info("Requests Module GET Call")
try:
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    print(r.status_code)
    print(r.headers)
    print(r.encoding)
    print(r.text)
    print(r.json())
except Exception as ex:
    logging.error(f"Exception occurred: {ex}")


logging.info("Request Module POST call")
payload = {"name": "John", "job": "Developer"}
try: 
    response = requests.post("https://httpbin.org/post", json=payload)
    print(response.status_code)
    print(response.json())

except Exception as ex:
    logging.error(f"Exception occurred: {ex}")

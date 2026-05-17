# open("filename", "mode")  # mode: r, w, a, r+, w+, a+
import os
from datetime import datetime
from urllib import response

from poetry import json

print(os.getcwd())  # get current working directory
os.chdir("Python\\Day6\\filedemo")

print(os.getcwd())

def read_file():
    file = None
    try:
        file = open("sample.txt", "r")
        # print(file)
        
        # print(file.read()) # read the entire file
        
        # print(file.readline())  # read the first line
        # print(file.readline())  # read the second line

        # print(file.readlines())  # read all lines and return a list

        # first 10 characters
        # print(file.read(10))

        for line in file:
            read_line = line.strip()
            for ch in read_line:
                if ch.isupper():
                    print(ch, end="")

    except FileNotFoundError:
        print("File not found.")
    
    finally:
        if file:
            file.close()



def write_file():
    file = None
    try:
        file = open("example.txt", "a")
        file.write("Today we are discussing File Handling\n")
        file.writelines(["This is line 1\n", "This is line 2\n", "This is line 3\n"])
        file.write(f"File created on: {datetime.now()}\n")
    except Exception as e:
        print("An error occurred:", e)

    finally:
        if file:
            file.close()


def read_server_log():
    file = None
    try:
        file = open("server.log", "r")
        for line in file:
            if "ERROR" in line:
                print(line.strip())
    except FileNotFoundError:
        print("Server log file not found.")
    finally:
        if file:
            file.close()


def read_csv_file():
    file = None
    try:
        file = open("employees.csv", "r")
        for line in file:
            print(line.strip().split(","))
    except FileNotFoundError:
        print("CSV file not found.")
    finally:
        if file:
            file.close()


def read_csv_file_2():
    import csv
    file = None
    try:
        file = open("employees.csv", "r")
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row['name'], row['email'])
    except FileNotFoundError:
        print("CSV file not found.")
    finally:
        if file:
            file.close()
            

def write_csv_file():
    import csv
    file = None
    try:
        file = open("employees.csv", "a")
        csv_writer = csv.writer(file)
        csv_writer.writerow(["John Doe", "john.doe@example.com", "Engineering"])
    except FileNotFoundError:
        print("CSV file not found.")
    finally:
        if file:
            file.close()


def read_json_file():
    import json
    file = None
    try:
        file = open("config.json", "r")
        data = json.load(file)
        print(data)
    except FileNotFoundError:
        print("JSON file not found.")
    finally:
        if file:
            file.close()


def write_json_file():
    import json
    file = None
    data = {"name": "Rahul", "skills": ["Python", "AWS"]}

    try:
        file = open("personal.json", "w")
        json.dump(data, file, indent=9)
    except FileNotFoundError:
        print("JSON file not found.")
    finally:
        if file:
            file.close()


def make_api_call():
    import requests
    import json
    API_URL = "https://fakerapi.it/api/v1/companies?_quantity=5"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        with open("companies.json", "w") as file:
            json.dump(data, file, indent=4)
    
        print("Data fetched and saved to companies.json")
    else:
        print("Failed to fetch data from API.")


def make_post_api_call():
    import requests
    API_URL = "https://httpbin.org/post"
    payload = {"name": "Kumar", "age": 30}
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        print("POST request successful. Response:")
        print(response.json())
    else:
        print("Failed to make POST request.")


def make_api_call_with_httpclient():
    import http.client
    import json

    conn = http.client.HTTPSConnection("fakerapi.it")
    conn.request("GET", "/api/v1/companies?_quantity=5")
    response = conn.getresponse()
    
    if response.status == 200:
        data = json.loads(response.read())
        with open("companies_httpclient.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data fetched and saved to companies_httpclient.json")
    else:
        print("Failed to fetch data from API.")
    
    conn.close()



def download_image_file():
    import requests
    image_url = "https://plus.unsplash.com/premium_photo-1690571200236-0f9098fc6ca9?q=80&w=1332&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    
    response = requests.get(image_url)
    #print(response.content)# print first 20 bytes of the image content
    
    if response.status_code == 200:
        with open("image1.png", "wb") as file:
            file.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download image.")


# read_file()
# write_file()

# read_server_log()

# read_csv_file()

# read_csv_file_2()

# write_csv_file()
# read_csv_file_2()

# read_json_file()
# write_json_file()

# make_api_call()
# make_post_api_call()

# make_api_call_with_httpclient()

download_image_file()

print("\n**********")
print("Successfully performed operation.")
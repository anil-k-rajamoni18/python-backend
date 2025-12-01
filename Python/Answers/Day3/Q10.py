config = {
  "server": {
    "host": "localhost",
    "ports": {
      "http": 80,
      "https": 443
    }
  }
}
#Get HTTP & HTTPS port values
ports=[value for value in config["server"]["ports"].values()]
print(ports)

#Add a new port "ssh": 22
config["server"]["ports"]["ssh"]=22
print(config)

#List all keys present inside "server"
keys=list(config["server"].keys())
print(keys)
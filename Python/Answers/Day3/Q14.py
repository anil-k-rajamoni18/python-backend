
#NEED TO REWORK TO HANDLE ALL THE CASES


data = {
  "transaction": {
    "id": "TXN001",
    "amount": 1500,
    "metadata": {
      "customer": {
        "id": 22,
        "name": "John    Doe",
        "phones": ["+91 99999 11111", "  +91 88888 22222 "]
      },
      "location": {
        "country": " India ",
        "state": "Karnataka"
      }
    }
  }
}

#Write a recursive function to trim all string values regardless of nesting level.
def get_strings(data):
    for key,value in data.items():
        if isinstance(value,dict):
            get_strings(value)
        elif isinstance(value,list):
            for i in range(len(value)):
                if(isinstance(value[i],str)):
                    value[i]=value[i].strip()
                elif isinstance(value[i],dict):
                     get_strings(value[i])
        else:
            if isinstance(value, str):
                data[key]=value.strip()

get_strings(data)            
print(data)

#Convert all phone numbers to: +91XXXXXXXXXX format.
def formatnumber(data):
    for key, value in data.items():
        if isinstance(value,dict):
            formatnumber(value)
        elif isinstance(value,list):
            for i in range(len(value)):
                if isinstance(value[i],str):
                    cleaned = value[i].strip()
                    if(cleaned.startswith("+91")):
                        value[i]=cleaned.replace(" ","")
        elif isinstance(value,str):
            cleaned = value.strip()
            if cleaned.startswith("+91"):
                data[key]=cleaned.replace(" ","")

formatnumber(data)
print(data)
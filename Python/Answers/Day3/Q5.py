log_data = [
  "ERROR Disk failure",
  "WARNING Low memory",
  "ERROR Network timeout",
  "INFO System rebooted",
  "ERROR Disk failure",
]

errorCount=0
warningCount=0
infoCount=0
#Count frequency of each log level (ERROR, WARNING, INFO)
for log in log_data:
    if "ERROR" in log:
        errorCount+=1
    elif "WARNING" in log:
        warningCount+=1
    elif "INFO" in log:
        infoCount+=1

print(f"frequency of Error is {errorCount}")
print(f"frequency of Warning is {warningCount}")
print(f"frequency of Info is {infoCount}")

#Count the most repeated message (full text)
"""
maxRepeatedString=0
for log in log_data:
    if log_data.count(log)>maxRepeatedString:
        maxRepeatedString=log_data.count(log)

"""

#frequency dictionary to store log and its frequency
freq={}
for log in log_data:
    freq[log]=freq.get(log,0)+1

mostRepeatedKey=max(freq, key=freq.get)
mostRepeatedKeyValue=freq[mostRepeatedKey]
print(mostRepeatedKey)
print(mostRepeatedKeyValue)


#Find all unique messages
uniqueMessages=[log for log,count in freq.items() if count==1]
print(uniqueMessages)



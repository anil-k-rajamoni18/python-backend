responses = ["Yes ", " No", "YES", "no", " yes", " NO "]

#Normalize to lowercase
responses=[response.lower() for response in responses]
print(responses)

#Strip spaces
responses=[response.strip() for response in responses]
print(responses)
#Count how many "yes" responses
noOfYes=responses.count("yes")
print(f"No of yes responses is {noOfYes}")
#Convert into booleans (yes → True, no → False)
for i in range(len(responses)):
    if responses[i]=="yes":
        responses[i]="True"
    else:
        responses[i]="False"
print(responses)
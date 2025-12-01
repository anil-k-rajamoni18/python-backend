countries = {
  "IN": "India",
  "US": "United States",
  "CA": "Canada"
}

#Create reverse mapping: "India" → "IN"
#Ensure values are unique before reversing
countriesFullNames=list(countries.values())

reverseMapping={value:key for key,value in countries.items() if countriesFullNames.count(value)==1}
print(reverseMapping)


#Sort reversed dictionary by key (country name)
sortedreverseMapping=dict(sorted(reverseMapping.items()))
print(sortedreverseMapping)
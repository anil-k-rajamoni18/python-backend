"""
1️⃣ Build a Unit Conversion Service (Backend Simulation)
Write functions to convert: km → miles, Celsius → Fahrenheit, kg → pounds.

Requirements:
Each conversion function must accept default arguments.
Write a wrapper function: convert(value, type="km_to_miles").
Return results rounded to 2 decimals.

"""
def km_to_miles(km=0)
  
#wrapper function
def convert(value, type="km_to_miles"):
    if type=="km_to_miles":
       return km_to_miles(value)
    
    elif type=="cls_to_fahren":
       return ls_to_fahren(value)
    else:
       return kg_to_pounds(value)
       

result=convertMetrics(100,"cls_to_fahrein")
print(result)
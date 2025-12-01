products = [
  {"id": 101, "name": "Laptop", "price": 75000},
  {"id": 102, "name": "Mouse", "price": 500},
  {"id": 103, "name": "Keyboard", "price": 1200},
]

#Build a dict {id: price} using comprehension
pricesDictionary= {product["id"]:product["price"] for product in products}
print(pricesDictionary)

#Find the most expensive product
expensiveProduct=max(pricesDictionary,key=pricesDictionary.get)
print(f"Most Expensive product is {expensiveProduct}")

#Increase all prices by 10%
for id in pricesDictionary:
    pricesDictionary[id]=pricesDictionary[id]+(0.1*pricesDictionary[id])

print(f"After increasing the price by 10%: {pricesDictionary}")

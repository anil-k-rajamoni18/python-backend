# def apply_twice(func, value):
#     return func(func(value))


# result = apply_twice(lambda x: x + 3, 5)
# print(result)


def outer():
    name = "naUya  "
    def inner():
        nonlocal name
        name = name.strip().upper()
        print(f"Helllo User: {name}")
    return inner


res = outer() 
print(res)
res()


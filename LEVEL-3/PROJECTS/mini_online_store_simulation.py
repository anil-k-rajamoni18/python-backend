# 🔹 Global product inventory (Variable Scope)
inventory = {
    "Electronics": {
        "Laptop": 800,
        "Phone": 500
    },
    "Clothing": {
        "T-Shirt": 20,
        "Jeans": 40
    },
    "Books": {
        "Fiction": 15,
        "Non-fiction": 25
    }
}

cart = []

# 🔹 Recursion: Display nested product categories
def display_inventory(category_dict, indent=0):
    for key, value in category_dict.items():
        if isinstance(value, dict):
            print("  " * indent + f"[{key}]")
            display_inventory(value, indent + 1)
        else:
            print("  " * indent + f"- {key}: ${value}")

# 🔹 Function with return value
def get_price(product_name):
    for category in inventory.values():
        if isinstance(category, dict):
            for name, price in category.items():
                if name == product_name:
                    return price
    return None

# 🔹 Function with input and return
def add_to_cart(product_name, quantity):
    price = get_price(product_name)
    if price:
        cart.append({"item": product_name, "qty": quantity, "price": price})
        return f"Added {quantity} x {product_name} to cart."
    else:
        return f"{product_name} not found in inventory."

# 🔹 Closure: Discount calculator
def discount_coupon(percent):
    def apply_discount(total):
        return total - (total * percent / 100)
    return apply_discount


# 🔹 Nested function: Checkout
def checkout():
    def calculate_total():
        return sum(item['price'] * item['qty'] for item in cart)

    print("\n🧾 Your Cart:")
    for item in cart:
        print(f"{item['qty']} x {item['item']} @ ${item['price']} each")

    total = calculate_total()
    print(f"Total before discount: ${total:.2f}")

    use_coupon = input("Apply 10% discount coupon? (yes/no): ").lower()
    if use_coupon == "yes":
        apply_10 = discount_coupon(10)
        total = apply_10(total)
        print("✅ Coupon applied.")

    print(f"💰 Final Amount to Pay: ${total:.2f}")

# 🔹 Function with no arguments and no return
def greet_user():
    print("👋 Welcome to the Mini Online Store!")

# 🔹 Main Flow
def main():
    greet_user()
    while True:
        print("\n📦 Available Products:")
        display_inventory(inventory)

        action = input("\nChoose an action - [add] to cart, [checkout], or [exit]: ").lower()
        if action == "add":
            item = input("Enter product name to add: ").strip()
            qty = int(input("Enter quantity: "))
            print(add_to_cart(item, qty))
        elif action == "checkout":
            checkout()
            break
        elif action == "exit":
            print("👋 Thanks for visiting!")
            break
        else:
            print("❗ Invalid action. Try again.")

# 🔹 Run the store
main()

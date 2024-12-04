# Function with Mixed Parameters
def order_summary(name, *items, address="Unknown", **extra_details):
    print(f"Customer: {name}")
    print(f"Items Ordered: {items}")
    print(f"Delivery Address: {address}")
    print("Extra Details:", extra_details)

# Call the function
order_summary("Alice", "Pizza", "Burger", address="123 Street", payment="Card")

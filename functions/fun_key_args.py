# Function with Variable-Length Keyword Arguments (**kwargs)
def display_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

# Pass keyword arguments
display_details(name="Alice", age=30, city="New York")

# Ex1 Create a Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")

# Ex2 Function with Multiple Parameters
def add_numbers(a, b):
    return a + b

# Call the function with two arguments
result = add_numbers(5, 10)
print("Sum:", result)

# Ex3 Function with Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Call the function without arguments
greet()

# Call the function with an argument
greet("Bob")

# Ex4 Function with Keyword Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Call the function using keyword arguments
display_info(age=25, name="Charlie")

# Pass a Function as an Argument
def apply_operation(a, b, operation):
    return operation(a, b)

# Define some operations
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Pass functions as arguments
print("Addition:", apply_operation(5, 10, add))
print("Multiplication:", apply_operation(5, 10, multiply))

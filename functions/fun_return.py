# Returning Multiple Values
def calculate(a, b):
    sum_ = a + b
    product = a * b
    return sum_, product

# Unpack the returned tuple
s, p = calculate(5, 10)
print("Sum:", s, "Product:", p)

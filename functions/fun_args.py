# Function with Variable-Length Arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

# Pass multiple arguments
result = sum_all(1, 2, 3, 4, 5)
print("Sum:", result)

#  Lambda (Anonymous) Functions

# A lambda function is a small anonymous function that can have any number of arguments but only one expression.

# Regular function
def square(x):
    return x * x

# Lambda function
square_lambda = lambda x: x * x

print("Square:", square(5))
print("Square (Lambda):", square_lambda(5))

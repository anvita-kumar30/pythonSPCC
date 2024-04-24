def original_expression(x):
    # Compute x^2 using exponentiation
    return x ** 2

def strength_reduction_expression(x):
    # Compute x^2 using x * x (strength reduction)
    return x * x

# Test the original expression and strength reduction expression
input_value = 5

# Compute x^2 using original expression
original_result = original_expression(input_value)

# Compute x^2 using strength reduction expression
reduction_result = strength_reduction_expression(input_value)

# Print the results
print(f"Original expression result for {input_value}^2:", original_result)
print(f"Strength reduction expression result for {input_value}^2:", reduction_result)

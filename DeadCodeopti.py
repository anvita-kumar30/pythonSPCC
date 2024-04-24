def perform_dead_code_elimination(sample_code):
    lines = sample_code.strip().split('\n')
    used_variables = set()
    optimized_lines = []

    # Traverse the sample code to identify used variables
    for line in lines:
        line = line.strip()
        if '=' in line:
            lhs, rhs = line.split('=')
            assigned_var = lhs.strip()
            used_variables.add(assigned_var)

            # Check if any variable on the right-hand side is used
            tokens = rhs.split()
            for token in tokens:
                if token.isalnum():  # Check if token is a variable
                    used_variables.add(token)

    # Filter out the lines that contain used variables
    for line in lines:
        line = line.strip()
        if '=' in line:
            lhs, rhs = line.split('=')
            assigned_var = lhs.strip()
            if assigned_var in used_variables:
                optimized_lines.append(line)

    return '\n'.join(optimized_lines)

# Sample code with dead code
sample_code = """
    t1 = 4 * i
    t2 = 3 * j
    t3 = t1 + t2
    x = a[t3]
    y = b[t2]
    z = t1 + t2
    w = x + y
"""

# Perform dead code elimination (DCE)
optimized_code = perform_dead_code_elimination(sample_code)

# Print the original code
print("Original Code:")
print(sample_code)

# Print the optimized code after Dead Code Elimination
print("\nOptimized Code (after Dead Code Elimination):")
print(optimized_code)

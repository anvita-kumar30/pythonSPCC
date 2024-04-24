def perform_global_cse(sample_code):
    lines = sample_code.strip().split('\n')
    expressions = []
    expression_map = {}
    optimized_lines = []

    for line in lines:
        line = line.strip()
        if '=' in line:
            expressions.append(line.split('='))

    for assignment in expressions:
        if len(assignment) == 2:
            lhs, rhs = assignment
            if rhs not in expression_map:
                expression_map[rhs] = lhs
                optimized_lines.append(f"{lhs}={rhs}")
            else:
                optimized_lines.append(f"{lhs}={expression_map[rhs]}")

    return '\n'.join(optimized_lines)

# Sample code to optimize
sample_code = """t1 = a * (b + c)
t2 = 12 / a
t3 = t1 + (d * e)
t4 = a * (b + c)
t5 = t2 + (d * e)
t6 = 15 / a
"""

# Perform global common subexpression elimination (GCSE)
optimized_code = perform_global_cse(sample_code)
# Print the original code
print("Original Code:")
print(sample_code)
# Print the optimized code
print("Optimized Code:")
print(optimized_code)

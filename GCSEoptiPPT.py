def perform_global_cse(sample_code):
    lines = sample_code.strip().split('\n')
    expressions = []
    expression_map = {}
    optimized_lines = []
    for line in lines:
        line = line.strip()
        if '=' in line:
            expressions.append(line.split('='))
        expressions.append(line)
    for assignment in expressions:
        if len(assignment) == 2:
            lhs, rhs = assignment
            if rhs not in expression_map:
                expression_map[rhs] = lhs
                optimized_lines.append(f"{lhs}={rhs}")
            else:
                optimized_lines.append(f"{lhs}={expression_map[rhs]}")
    return '\n'.join(optimized_lines)
sample_code = """t6=4*i
x=a[t6] 
t7=4*i
t8=4*j 
t9=a[t8] 
a[t7]=a[t8]
t10=4*j 
a[t10]=a[t6]
"""
# Perform global common subexpression elimination (GCSE)
optimized_code = perform_global_cse(sample_code)
# Print the original code
print("Original Code:")
print(sample_code)
# Print the optimized code
print("Optimized Code:")
print(optimized_code)

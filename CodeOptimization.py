import re


def optimize_code(code):
    # Regular expression to match simple arithmetic expressions
    expr_pattern = re.compile(r'(\d+)\s*([+\-*/])\s*(\d+)')

    # Find all matches of arithmetic expressions in the code
    matches = expr_pattern.findall(code)

    # Iterate over each match and perform constant folding
    for match in matches:
        left_operand = int(match[0])
        operator = match[1]
        right_operand = int(match[2])

        # Evaluate the arithmetic expression
        if operator == '+':
            result = left_operand + right_operand
        elif operator == '-':
            result = left_operand - right_operand
        elif operator == '*':
            result = left_operand * right_operand
        elif operator == '/':
            result = left_operand / right_operand  # Assuming Python 3 division

        # Replace the original expression with the evaluated result in the code
        code = code.replace(' '.join(match), str(result))

    return code


# Example usage:
if __name__ == "__main__":
    original_code = "10 + 20 * 2 - 5 / 1"
    optimized_code = optimize_code(original_code)

    print("Original Code:", original_code)
    print("Optimized Code:", optimized_code)

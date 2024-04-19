def generate_tac(expression):
    # Operator precedence dictionary
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    # Function to generate a new temporary variable (t1, t2, ...)
    temp_count = 1
    def new_temp():
        nonlocal temp_count
        temp_var = f"t{temp_count}"
        temp_count += 1
        return temp_var

    # Stack to handle operators and operands
    operator_stack = []
    output_queue = []
    tokens = expression.split()

    try:
        for token in tokens:
            if token.isalnum():  # Operand (variable or constant)
                output_queue.append(token)
            elif token in precedence:  # Operator
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    if len(output_queue) < 2:
                        raise ValueError("Insufficient operands for operator.")
                    operand2 = output_queue.pop()
                    operand1 = output_queue.pop()
                    temp = new_temp()
                    tac_statement = f"{temp} = {operand1} {operator_stack.pop()} {operand2}"
                    output_queue.append(temp)
                    print(tac_statement)
                operator_stack.append(token)
            elif token == '(':  # Left parenthesis
                operator_stack.append(token)
            elif token == ')':  # Right parenthesis
                while operator_stack and operator_stack[-1] != '(':
                    if len(output_queue) < 2:
                        raise ValueError("Insufficient operands for operator.")
                    operand2 = output_queue.pop()
                    operand1 = output_queue.pop()
                    temp = new_temp()
                    tac_statement = f"{temp} = {operand1} {operator_stack.pop()} {operand2}"
                    output_queue.append(temp)
                    print(tac_statement)
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()  # Remove the '(' from stack

        # Process remaining operators in the stack
        while operator_stack:
            if len(output_queue) < 2:
                raise ValueError("Insufficient operands for operator.")
            operand2 = output_queue.pop()
            operand1 = output_queue.pop()
            temp = new_temp()
            tac_statement = f"{temp} = {operand1} {operator_stack.pop()} {operand2}"
            output_queue.append(temp)
            print(tac_statement)

        if len(output_queue) != 1 or operator_stack:
            raise ValueError("Invalid expression format.")

    except Exception as e:
        print(f"Error: {e}")

# Test the TAC generation function
if __name__ == "__main__":
    # Input expression
    expression = "a * (b + c) - d / e"

    print("Generated Three Address Code (TAC):")
    generate_tac(expression)

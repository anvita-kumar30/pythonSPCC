class ThreeAddressGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        # Generate a new temporary variable name t0, t1, t2, ...
        temp_name = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_name

    def generate(self, op, arg1, arg2, result):
        # Generate a three-address code instruction
        instruction = (op, arg1, arg2, result)
        self.code.append(instruction)

    def generate_expression(self, postfix_expression):
        # Parse and generate three-address code for the given postfix expression
        tokens = postfix_expression.split()
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                # If the token is a number, push it onto the stack
                stack.append(token)
            else:
                # Otherwise, it's an operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression format")

                arg2 = stack.pop()
                arg1 = stack.pop()
                result_temp = self.new_temp()

                # Generate code for the operation
                self.generate(token, arg1, arg2, result_temp)

                # Push the result back onto the stack
                stack.append(result_temp)

        if len(stack) != 1:
            raise ValueError("Invalid expression format")

        return stack.pop()

    def print_code(self):
        # Print the generated three-address code
        for instr in self.code:
            print(instr)


# Example usage:
if __name__ == "__main__":
    generator = ThreeAddressGenerator()

    # Example postfix expression: "2 3 + 4 5 - *"
    postfix_expression = "2 3 + 4 5 - *"
    result = generator.generate_expression(postfix_expression)

    # Print the generated three-address code
    generator.print_code()

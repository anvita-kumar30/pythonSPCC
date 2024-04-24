class TACGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []
    def generate_tac(self, expression):
        self.temp_count = 0
        self.code = []
        tokens = self.tokenize(expression)
        output_queue = []
        operator_stack = []
        for token in tokens:
            if token.isdigit():
                output_queue.append(token)
            elif token in {'+', '-', '*', '/'}:
                while (operator_stack and self.has_higher_precedence(operator_stack[-1], token)):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
        while operator_stack:
            output_queue.append(operator_stack.pop())
        self.build_tac(output_queue)
        return self.code
    def tokenize(self, expression):
        tokens = []
        current_number = ''
        for char in expression:
            if char.isdigit():
                current_number += char
            else:
                if current_number:
                    tokens.append(current_number)
                    current_number = ''
                tokens.append(char)
        if current_number:
            tokens.append(current_number)
        return tokens
    def has_higher_precedence(self, op1, op2):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        if op1 in precedence and op2 in precedence:
            return precedence[op1] >= precedence[op2]
        else:
            return False
    def build_tac(self, tokens):
        operand_stack = []
        for token in tokens:
            if token.isdigit():
                operand_stack.append(token)
            elif token in {'+','-', '*', '/'}:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result_var = f't{self.temp_count}'
                self.temp_count += 1
                self.code.append((token, operand1, operand2, result_var))
                operand_stack.append(result_var)
if __name__=="__main__":
    tac_generator = TACGenerator()
    expression = "5 * (3 + 4) - 2 / 1"
    tac = tac_generator.generate_tac(expression)
    print("Three Address Code (TAC) for expression: ", expression)
    for quad in tac:
        print(quad)
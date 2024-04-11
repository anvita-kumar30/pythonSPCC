import re


# Class to represent a Macro
class Macro:
    def __init__(self, name, params, definition):
        self.name = name
        self.params = params
        self.definition = definition


# Multi-pass macroprocessor function
def multi_pass_macroprocessor(input_file):
    macro_definitions = {}
    expanded_code = []

    # Pass 1: Identify and store macro definitions
    with open(input_file, 'r') as file:
        inside_macro = False
        current_macro_lines = []

        for line in file:
            line = line.strip()

            if line.startswith("MACRO"):
                # Start of a macro definition
                macro_header = line[len("MACRO"):].strip()
                if '(' not in macro_header or ')' not in macro_header:
                    print(f"Error: Invalid macro definition format - {line}")
                    return None

                macro_name, macro_params = macro_header.split('(')
                macro_params = macro_params[:-1].strip()  # Remove closing parenthesis

                inside_macro = True
                current_macro_lines = []
            elif line == "MEND":
                # End of a macro definition
                inside_macro = False
                macro_definitions[macro_name] = Macro(macro_name, macro_params.split(','), current_macro_lines)
            elif inside_macro:
                # Collect lines inside a macro definition
                current_macro_lines.append(line)

    # Pass 2: Expand macros in the code
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith("MACRO"):
                # Skip macro definition lines in Pass 2
                continue
            elif line == "MEND":
                # Skip MEND lines in Pass 2
                continue
            else:
                # Check if the line contains a macro call
                for macro_name in macro_definitions:
                    if macro_name in line:
                        # Replace macro call with expanded macro code
                        macro = macro_definitions[macro_name]
                        expanded_code.extend(expand_macro(macro, line))
                        break
                else:
                    # Append line as is if no macro call found
                    expanded_code.append(line)

    return expanded_code


# Helper function to expand a macro call
def expand_macro(macro, macro_call):
    expanded_lines = []

    # Replace macro parameters with actual arguments in the macro definition
    arguments = macro_call.split()[1:]  # Extract arguments from macro call
    macro_definition = macro.definition[:]

    for i, arg in enumerate(arguments):
        for j, line in enumerate(macro_definition):
            # Replace parameter with argument in each line of macro definition
            macro_definition[j] = re.sub(r'\b' + macro.params[i] + r'\b', arg, line)

    expanded_lines.extend(macro_definition)
    return expanded_lines


# Example usage:
if __name__ == "__main__":
    input_file = "input2.asm"
    expanded_code = multi_pass_macroprocessor(input_file)

    if expanded_code is not None:
        print("Expanded Code:")
        for line in expanded_code:
            print(line)

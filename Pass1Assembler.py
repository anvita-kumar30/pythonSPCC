import re
def pass1_assembler(input_file):
    symbol_table = {}
    location_counter = 0
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith(';'):
                # Skip empty lines and comments
                continue
            # Remove inline comments
            line = line.split(';')[0].strip()
            # Split line into label, instruction/directive, and operands
            label, _, rest = line.partition(' ')
            fields = rest.split()

            if label:
                # Store label in symbol table with current location counter
                if label in symbol_table:
                    print(f"Error: Duplicate label '{label}'")
                    return None
                symbol_table[label] = location_counter

            if fields:
                opcode = fields[0].upper()

                if opcode == 'ORG':
                    # Set location counter to specified origin
                    location_counter = int(fields[1], 16) if len(fields) > 1 else 0
                else:
                    # Increment location counter based on instruction length (assume fixed length)
                    location_counter += 1

    return symbol_table


# Example usage:
if __name__ == "__main__":
    input_file = "input.asm"
    symbol_table = pass1_assembler(input_file)

    if symbol_table:
        print("Symbol Table:")
        for label, address in symbol_table.items():
            print(f"{label}: {hex(address)}")

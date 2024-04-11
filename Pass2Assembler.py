def pass2_assembler(input_file, symbol_table):
    machine_code = []

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

            if fields:
                opcode = fields[0].upper()

                if opcode == 'ORG':
                    # Skip ORG directive in Pass 2
                    continue
                elif opcode == 'LOAD':
                    operand = fields[1]
                    if operand in symbol_table:
                        address = symbol_table[operand]
                        machine_code.append(f"01 {hex(address)[2:]}")  # Generate LOAD instruction
                    else:
                        print(f"Error: Undefined symbol '{operand}'")
                        return None
                elif opcode == 'ADD':
                    operand = fields[1]
                    if operand in symbol_table:
                        address = symbol_table[operand]
                        machine_code.append(f"02 {hex(address)[2:]}")  # Generate ADD instruction
                    else:
                        print(f"Error: Undefined symbol '{operand}'")
                        return None
                elif opcode == 'STORE':
                    operand = fields[1]
                    if operand in symbol_table:
                        address = symbol_table[operand]
                        machine_code.append(f"03 {hex(address)[2:]}")  # Generate STORE instruction
                    else:
                        print(f"Error: Undefined symbol '{operand}'")
                        return None
                elif opcode == 'HALT':
                    machine_code.append("00")  # Generate HALT instruction
                elif opcode == 'DATA':
                    value = int(fields[1])
                    machine_code.append(f"{hex(value)[2:].zfill(2)}")  # Generate DATA value
                elif opcode == 'RESW':
                    num_words = int(fields[1])
                    for _ in range(num_words):
                        machine_code.append("00")  # Reserve memory with zeros (dummy data)

    return machine_code


# Example usage:
if __name__ == "__main__":
    input_file = "input.asm"
    symbol_table = {
        'START': 0x0,
        'LOAD' : 0x1000,
        'ADD': 0x1001,
        'STORE': 0x1002,
        'X': 0x1003,
        'Y': 0x1004,
        'HALT': 0x1005,
        'B': 0x1005
    }

    machine_code = pass2_assembler(input_file, symbol_table)

    if machine_code:
        print("Generated Machine Code:")
        for code in machine_code:
            print(code)

def process_pass1(input_code):
    mdt = []
    mnt = {}
    ala = {}
    lines = input_code.strip().split('\n')
    line_number = 0
    current_macro_name = None
    parameters = []
    macro_definition = []

    for line in lines:
        line_number += 1
        line = line.strip()

        if line.startswith("MACRO"):
            # Parse macro definition
            parts = line.split()
            if len(parts) < 2:
                print(f"Error: Invalid macro definition at line {line_number}")
                continue

            macro_name = parts[1]
            parameters = parts[2:] if len(parts) > 2 else []
            current_macro_name = macro_name
            macro_definition = []
            ala[macro_name] = []
            continue

        if line.startswith("MEND"):
            # End of macro definition, store in MDT and update MNT
            mdt.append(macro_definition)
            mnt[current_macro_name] = {
                'index': len(mdt) - 1,
                'parameters': parameters
            }
            current_macro_name = None
            parameters = []
            macro_definition = []
            continue

        if current_macro_name:
            # Inside macro definition, collect lines
            macro_definition.append(line)

            # Populate ALA with parameter labels during Pass 1
            for param in parameters:
                ala[macro_name].append(param)

    print("Macro Definition Table (MDT):")
    for idx, entry in enumerate(mdt):
        print(f"{idx}: {' | '.join(entry)}")

    print("\nMacro Name Table (MNT):")
    for macro_name, info in mnt.items():
        print(f"{macro_name}: {info}")

    print("\nArgument List Array (ALA):")
    for macro_name, arg_labels in ala.items():
        print(f"{macro_name}: {arg_labels}")

if __name__ == "__main__":
    input_code = """
    MACRO ADD A, B
        MOV A, B
    MEND

    MACRO MULT C, D, E
        MUL C, D, E
    MEND
    """
    process_pass1(input_code)

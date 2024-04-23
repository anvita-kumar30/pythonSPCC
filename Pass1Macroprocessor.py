def process_pass1(input_code):
    mdt = []  # Macro Definition Table
    mnt = {}  # Macro Name Table
    ala = {}  # Argument List Array
    lines = input_code.strip().split('\n')
    line_number = 0
    current_macro_name = None
    parameters = []
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
            parameters = [param.strip('&') for param in parts[2:]]  # Extract parameter names without '&'
            current_macro_name = macro_name
            mdt.append([macro_name])  # Initialize macro definition list with macro name
            ala[macro_name] = {}  # Initialize argument list dictionary
            continue
        if line.startswith("MEND"):
            # End of macro definition
            if current_macro_name is None:
                print(f"Error: MEND found without matching MACRO at line {line_number}")
                continue
            mnt[current_macro_name] = {
                'index': len(mdt) - 1,
                'parameters': parameters
            }
            current_macro_name = None
            continue
        if current_macro_name:
            # Inside macro definition, process macro body lines
            mdt[-1].append(line)
            # Parse parameter assignments in macro invocations
            parts = [part.strip() for part in line.split(',')]
            for part in parts:
                if '=' in part:
                    arg_name, arg_value = part.split('=')
                    ala[current_macro_name][arg_name.strip()] = arg_value.strip()
    # Print Macro Definition Table (MDT)
    print("\nMacro Definition Table (MDT):")
    print("Index\t\tName")
    for idx, definition in enumerate(mdt, start=1):
        name = definition[0]
        arguments = '\n\t\t\t\t'.join(definition[1:])
        print(f"{idx}\t\t{name}\t{arguments}")
    # Print Macro Name Table (MNT)
    print("\nMacro Name Table (MNT):")
    print("Index\tName\tMDT index")
    for idx, (macro_name, info) in enumerate(mnt.items(), start=1):
        print(f"{idx}\t\t{macro_name}\t{idx}")
    # Print Dummy ALA in Pass 1
    print("\nDummy Argument List Array (ALA) in Pass 1:")
    print("Index\tArguments")
    for idx, (macro_name, arg_dict) in enumerate(ala.items(), start=1):
        arguments = ', '.join(arg_dict.keys())
        print(f"{idx}\t\t{arguments}")
if __name__ == "__main__":
    input_code = """
    MACRO INCR &ARG1, &ARG2, &ARG3
        A 1, &ARG1=A
        A 2, &ARG2=B
        A 3, &ARG3=C
    MEND

    INCR &ARG1, &ARG2, &ARG3
    """
    process_pass1(input_code)

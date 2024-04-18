def calculate_first_set(grammar):
    first = {}

    def is_terminal(symbol):
        return symbol.islower()

    def calculate_first(non_terminal):
        if non_terminal in first:
            return first[non_terminal]

        first_set = set()

        # Process each production of the non-terminal
        for production in grammar[non_terminal]:
            first_symbol = production[0]

            if is_terminal(first_symbol):
                # Terminal symbol found, add to FIRST set
                first_set.add(first_symbol)
            else:
                # Non-terminal symbol found, recursively calculate FIRST set
                if first_symbol != non_terminal:  # Avoid direct left recursion
                    first_set.update(calculate_first(first_symbol))

                # Check if FIRST(symbol) contains ε, consider next symbol in the production
                if 'ε' in first_set:
                    if len(production) > 1:
                        first_set.update(calculate_first(production[1]))
                    else:
                        first_set.add('ε')

        first[non_terminal] = first_set
        return first_set

    # Initialize FIRST sets for all non-terminals
    for non_terminal in grammar:
        calculate_first(non_terminal)

    return first

grammar = {
    'S': ['aAB', 'bBC', 'cC'],
    'A': ['d', 'ε'],
    'B': ['e', 'f'],
    'C': ['g', 'ε']
}

first_sets = calculate_first_set(grammar)

print("FIRST sets:")
for non_terminal, first_set in first_sets.items():
    sorted_elements = sorted(first_set)
    print(f"FIRST({non_terminal}) = {first_set}")

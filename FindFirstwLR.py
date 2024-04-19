def eliminate_left_recursion(grammar):
    non_terminals = list(grammar.keys())
    for A in non_terminals:
        productions = grammar[A]
        alpha = []
        beta = []

        # Classify productions into alpha and beta
        for production in productions:
            if production[0] == A:
                alpha.append(production[1:])
            else:
                beta.append(production)

        if alpha:
            # Create a new non-terminal A' for indirect left recursion
            A_dash = A + "'"
            grammar[A] = [production + (A_dash,) for production in beta]
            # Update grammar with new productions for A'
            grammar[A_dash] = [production + (A_dash,) for production in alpha] + [('ε',)]
    return grammar

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

def process_grammar_with_left_recursion(grammar):
    print("Original Grammar:")
    print_grammar(grammar)

    eliminate_left_recursion(grammar)

    print("\nGrammar without Left Recursion:")
    print_grammar(grammar)

    first_sets = calculate_first_set(grammar)

    if first_sets is not None:
        print("\nFIRST sets:")
        for non_terminal, first_set in first_sets.items():
            sorted_elements = sorted(first_set)
            print(f"FIRST({non_terminal}) = {sorted_elements}")
    else:
        print("\nError: Failed to compute FIRST sets for the grammar.")

def print_grammar(grammar):
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join([''.join(prod) for prod in productions])}")

grammar = {
    'A': [('A', 'a'), ('A', 'b'), ('c',), ('d', 'A')],
    'B': [('B', 'b'), ('B', 'c'), ('d',)]
}

process_grammar_with_left_recursion(grammar)

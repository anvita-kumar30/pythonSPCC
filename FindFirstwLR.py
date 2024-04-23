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
            grammar[A_dash] = [production + (A_dash,) for production in alpha] + [('#',)]
    return grammar
def calculate_first_set(grammar):
    first = {}
    def is_terminal(symbol):
        return symbol.islower() or symbol == '#'
    def calculate_first(non_terminal):
        if non_terminal in first:
            return first[non_terminal]
        first_set = set()
        for production in grammar[non_terminal]:
            first_symbol = production[0]
            if is_terminal(first_symbol):
                # Terminal symbol found, add to FIRST set
                first_set.add(first_symbol)
            else:
                if first_symbol != non_terminal:  # Avoid direct left recursion
                    first_set.update(calculate_first(first_symbol))
                # Check if FIRST(symbol) contains ε (epsilon)
                has_epsilon = True
                for symbol in production:
                    if symbol == '#':
                        continue  # Skip epsilon to consider next symbol
                    if symbol in grammar:
                        first_set.update(calculate_first(symbol) - {'#'})
                        if '#' not in calculate_first(symbol):
                            has_epsilon = False
                            break
                if has_epsilon:
                    first_set.add('#')  # Add epsilon to FIRST(non_terminal)
        first[non_terminal] = first_set
        return first_set
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
    print("\nFIRST sets:")
    for non_terminal, first_set in first_sets.items():
        sorted_elements = sorted(first_set)
        print(f"FIRST({non_terminal}) = {sorted_elements}")
def print_grammar(grammar):
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join([''.join(prod) for prod in productions])}")
grammar = {
    'A': [('A', 'a'), ('A', 'b'), ('c',), ('d', 'A')],
    'B': [('B', 'b'), ('B', 'c'), ('d',)]
}
process_grammar_with_left_recursion(grammar)

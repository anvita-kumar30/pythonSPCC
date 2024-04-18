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

def print_grammar(grammar):
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join([''.join(prod) for prod in productions])}")

grammar = {
    'A': [('A', 'a'), ('A', 'b'), ('c',), ('d', 'A')],
    'B': [('B', 'b'), ('B', 'c'), ('d',)]
}

print("Original Grammar:")
print_grammar(grammar)

eliminate_left_recursion(grammar)

print("\nGrammar without Left Recursion:")
print_grammar(grammar)

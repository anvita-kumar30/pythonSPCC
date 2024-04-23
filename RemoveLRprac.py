def eliminate_left_recursion(grammar):
    non_terminals = list(grammar.keys())
    for A in non_terminals:
        productions = grammar[A]
        alpha = []
        beta = []
        for production in productions:
            if production[0] == A:
                alpha.append(production[1:])
            else:
                beta.append(production)
        if alpha:
            A_dash = A + "'"
            grammar[A] = [production + (A_dash,) for production in beta]
            grammar[A_dash] = [production + (A_dash,) for production in alpha] + [('#',)]
    return grammar
def print_grammar(grammar):
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal} -> {' | '.join([''.join(prod) for prod in productions])}")
def process_grammar_with_lr(grammar):
    print("Original Grammar:")
    print_grammar(grammar)
    eliminate_left_recursion(grammar)
    print("\nAfter eliminating LR:")
    print_grammar(grammar)
grammar = {
    'A': [('A', 'a'), ('A', 'b'), ('c',), ('d', 'A')],
    'B': [('B', 'b'), ('B', 'c'), ('d',)]
}
process_grammar_with_lr(grammar)
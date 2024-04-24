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


# Example grammar
grammar = {
    'S': ['Aa', 'Bb'],
    'A': ['cA', 'd'],
    'B': ['e']
}
# grammar = {
#     'S': ['aAB', 'bBC', 'cC'],
#     'A': ['d', '#'],
#     'B': ['e', 'f'],
#     'C': ['g', '#']
# }
first_sets = calculate_first_set(grammar)
print("FIRST sets:")
for non_terminal, first_set in first_sets.items():
    sorted_elements = sorted(first_set)
    print(f"FIRST({non_terminal}) = {sorted_elements}")

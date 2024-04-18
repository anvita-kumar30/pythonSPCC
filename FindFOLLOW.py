def calculate_follow_set(grammar, start_symbol, first_sets):
    follow = {non_terminal: set() for non_terminal in grammar.keys()}
    follow[start_symbol].add('$')

    def is_terminal(symbol):
        return symbol.islower()

    def update_follow(non_terminal, production, idx):
        if idx == len(production):
            return  # Reached end of production, no additional follow symbols

        current_symbol = production[idx]

        if is_terminal(current_symbol):
            # Current symbol is a terminal, add to FOLLOW(non_terminal)
            follow[non_terminal].add(current_symbol)
        else:
            # Current symbol is a non-terminal
            if idx == len(production) - 1:
                # Last symbol in production, add FOLLOW(non_terminal) to FOLLOW(current_symbol)
                follow[current_symbol].update(follow[non_terminal])
            else:
                # More symbols after current_symbol, consider FIRST of the next symbol
                next_symbol = production[idx + 1]

                if is_terminal(next_symbol):
                    # Next symbol is a terminal, add to FOLLOW(current_symbol)
                    follow[current_symbol].add(next_symbol)
                else:
                    # Next symbol is a non-terminal, add FIRST(next_symbol) to FOLLOW(current_symbol)
                    follow[current_symbol].update(first_sets[next_symbol])

                    if 'ε' in first_sets[next_symbol]:
                        # Production can derive ε, consider FOLLOW(non_terminal)
                        follow[current_symbol].update(follow[non_terminal])

    # Iterate over grammar productions to compute FOLLOW sets
    for non_terminal, productions in grammar.items():
        for production in productions:
            for idx, symbol in enumerate(production):
                if not is_terminal(symbol):
                    update_follow(symbol, production, idx + 1)
    return follow

if __name__ == "__main__":
    grammar = {
        'S': ['Aa', 'Bb'],
        'A': ['cA', 'd'],
        'B': ['e']
    }

    start_symbol = 'S'

    first_sets = {
        'S': {'c', 'd', 'e'},
        'A': {'c', 'd'},
        'B': {'e'}
    }

    follow_sets = calculate_follow_set(grammar, start_symbol, first_sets)

    print("FOLLOW sets:")
    for non_terminal, follow_set in follow_sets.items():
        print(f"FOLLOW({non_terminal}) = {follow_set}")

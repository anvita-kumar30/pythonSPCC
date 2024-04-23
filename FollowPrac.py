def calculate_follow_set(grammar, start_symbol, first_sets):
    follow = {non_terminal: set() for non_terminal in grammar.keys()}
    follow[start_symbol].add('$')
    def is_terminal(symbol):
        return symbol.islower()
    def update_follow(non_terminal, production, idx):
        if idx == len(production):
            return
        current_symbol = production[idx]
        if is_terminal(current_symbol):
            follow[non_terminal].add(current_symbol)
        else:
            if idx == len(production) - 1:
                follow[current_symbol].update(follow[non_terminal])
            else:
                next_symbol = production[idx + 1]
                if is_terminal(next_symbol):
                    follow[current_symbol].add(next_symbol)
                else:
                    follow[current_symbol].update(first_sets[next_symbol])
                    if '#' in first_sets[next_symbol]:
                        follow[current_symbol].update(follow[non_terminal])
    for non_terminal, productions in grammar.items():
        for production in productions:
            for idx, symbol in enumerate(production):
                if not is_terminal(symbol):
                    update_follow(symbol, production, idx+1)
    return follow


if __name__=="__main__":
    grammar = {
        'S': ['Aa', 'Bb'],
        'A': ['cA', 'd'],
        'B': ['e']
    }
    print("Grammar:")
    for non_terminal, productions in grammar.items():
        print(f"{non_terminal}: {productions}")
    start_symbol = 'S'
    first_sets = {
        'S': ['c', 'd', 'e'],
        'A': ['c', 'd'],
        'B': ['e']
    }
    print("First set of the grammar:")
    for non_terminal, productions in first_sets.items():
        print(f"{non_terminal}: {productions}")
    follow_sets = calculate_follow_set(grammar, start_symbol, first_sets)
    print("Follow set:")
    for non_terminal, productions in follow_sets.items():
        print(f"{non_terminal}: {productions}")

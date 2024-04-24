def createLL1ParsingTable(rules, nonterm_userdef, term_userdef, firsts, follows):
    parsing_table = {nonterm: {term: None for term in term_userdef} for nonterm in nonterm_userdef}
    for nonterm in nonterm_userdef:
        for rule in rules:
            if rule.startswith(nonterm):
                production = rule.split(' -> ')[1].strip()
                production_parts = production.split(' | ')
                for part in production_parts:
                    first_set = set()
                    for symbol in part.split():
                        if symbol in term_userdef:
                            # Add the terminal symbol to the FIRST set and break the loop
                            first_set.add(symbol)
                            break
                        elif symbol in nonterm_userdef:
                            # Union the FIRST set of the non-terminal with the current FIRST set
                            first_set |= firsts[symbol] - {'#'}
                            if '#' not in firsts[symbol]:
                                break
                    # If the loop completes without breaking, add '#' (epsilon) to the FIRST set
                    else:
                        first_set |= {'#'}
                    for term in first_set:
                        if term != '#':
                            parsing_table[nonterm][term] = part.split()
                    if '#' in first_set:
                        # Add the production part to the LL(1) parsing table for each terminal in FOLLOW(nonterm)
                        for term in follows[nonterm]:
                            parsing_table[nonterm][term] = ['#']
    print("\nLL(1) Parsing Table:")
    print("".ljust(10), end='')
    for term in term_userdef:
        print(term.ljust(10), end='')
    print()
    for nonterm in nonterm_userdef:
        print(nonterm.ljust(10), end='')
        for term in term_userdef:
            if parsing_table[nonterm][term] is not None:
                print(f"{nonterm} -> {' '.join(parsing_table[nonterm][term])}".ljust(10), end='')
            else:
                print("".ljust(10), end='')
        print()
rules = [
    "S -> A | B C",
    "A -> a | b",
    "B -> p | #",
    "C -> c"
]
nonterm_userdef = ['S', 'A', 'B', 'C']
term_userdef = ['a', 'b', 'c', 'p', '$']
firsts = {
    'S': {'a', 'b', 'p', 'c'},
    'A': {'a', 'b'},
    'B': {'p', '#'},
    'C': {'c'}
}
follows = {
    'S': {'$'},
    'A': {'$'},
    'B': {'c'},
    'C': {'$'}
}
createLL1ParsingTable(rules, nonterm_userdef, term_userdef, firsts, follows)

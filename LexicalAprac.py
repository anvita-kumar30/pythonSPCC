def is_alphabet(c):
    return ('a' <= c <= 'z') or ('A' <= c <= 'Z')
def is_number(c):
    return ('0' <= c <= '9') or (c == '.')
def main():
    print("Enter input: ")
    user_input = input().strip()
    keywords = ['int', 'float', 'const', 'return']
    operators = ['+', '-', '*', '/', '=']
    i = 0
    while i < len(user_input):
        c = user_input[i]
        if c==' ':
            i+=1
            continue
        elif is_alphabet(c):
            token = ""
            while i<len(user_input) and is_alphabet(user_input[i]):
                token += user_input[i]
                i+=1
            if token in keywords:
                print(token + " is a keyword")
            else:
                print(token + " is a variable")
            if i<len(user_input) and user_input[i]==';':
                print("; is a separator")
            i-=1
        elif is_number(c):
            number=""
            while i<len(user_input) and is_number(user_input[i]):
                number+=user_input[i]
                i+=1
            print(number + " is a constant")
            if i<len(user_input) and user_input[i] == ';':
                print("; is a separator")
            i-=1
        elif c in operators:
            if c=='=':
                print(c + " is an assignment operator")
            else:
                print(c+" is an operator")
        i+=1
if __name__=="__main__":
    main()
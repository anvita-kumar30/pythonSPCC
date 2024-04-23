def process_pass1(input_code):


if __name__=="__main__":
    input_code = """
    MACRO INCR &ARG1, &ARG2, &ARG3
        A 1, &ARG1
        A 2, &ARG2
        A 3, &ARG3
    MEND

    INCR &ARG1 = A, &ARG2 = B, &ARG3 = C

    INCR &ARG1 = A, &ARG3 = C, &ARG2 = B
    """
    process_pass1(input_code)
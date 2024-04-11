; Sample input2.asm file with macro definitions and calls

MACRO ADDLOOP (COUNT, VALUE)
    LDA VALUE
    ADD COUNT
    STA VALUE
MEND

ORG 1000

    ; Macro call to ADDLOOP
    ADDLOOP 3, 50

    ; Another macro call to ADDLOOP
    ADDLOOP 5, 30

    HLT

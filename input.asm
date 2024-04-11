; Sample input.asm file for Pass 1 of the assembler

START ORG 1000    ; Set origin to memory address 1000

    LOAD A, X     ; Load contents of memory location X into register A
    ADD B         ; Add contents of memory location B to register A
    STORE A, Y    ; Store contents of register A into memory location Y

X   DATA 200      ; Define label X with data value 200
Y   RESW 1        ; Define label Y as a reserved word (1 word allocation)

    HALT          ; Halt execution

B   DATA 50       ; Define label B with data value 50

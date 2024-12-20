import re
from itertools import product

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def solve(file_name):
    lines = getLines(file_name)
    print(lines)

    digit = re.compile(r'\d+')
    A = int(digit.search(lines[0]).group(0))
    B = int(digit.search(lines[1]).group(0))
    C = int(digit.search(lines[2]).group(0))

    program = [int(i) for i in re.findall(r'(\d+)', lines[4])]

    combo = [0, 1, 2, 3, "A", "B", "C", "R"]
    opcodes = ["adv", "bxl", "bst", "jnz", "bxc", "out", "bdv", "cdv"]

    comboOpcodes = [0, 2, 5,6,7] # adv, bst, out, (dbv, cdv)

    output = []
    instruction = 0
    while instruction < len(program):
        print(f'{program[instruction:instruction+2]=}')
        opcode = program[instruction]
        instruction +=1
        operand = program[instruction]
        instruction +=1
        if opcode in comboOpcodes:
            if operand == 4:
                operand = A
            elif operand == 5:
                operand = B
            elif operand == 6:
                operand = C
        print(f'BEFORE: {A}, {B}, {C}')
        if opcode == 0:
            val = adv(A, operand)
            A = val
        elif opcode == 1:
            val = bxl(B, operand)
            B = val
        elif opcode == 2:
            val = bst(operand)
            B = val
        elif opcode == 3:
            isZero, jump = jnz(A, operand)
            if not isZero:
                instruction = jump
        elif opcode == 4:
            val = bxc(B,C)
            B = val
        elif opcode == 5:
            val = out(operand)
            output.append(val)
            #print("added: " , val)
        elif opcode == 6:
            val = bdv(A, operand)
            B = val
        elif opcode == 7:
            val = adv(A, operand)
            C = val

        print(f'AFTER: {A}, {B}, {C}')
                
    #print(output)
    #print(A,B,C,program)

    output = ','.join([str(s) for s in output])
    return [A, B, C, output]


    #Combo operands 0 through 3 represent literal values 0 through 3.
    #Combo operand 4 represents the value of register A.
    #Combo operand 5 represents the value of register B.
    #Combo operand 6 represents the value of register C.
    #Combo operand 7 is reserved and will not appear in valid programs.
    
    #The adv instruction (opcode 0) performs division. 
    #The numerator is the value in the A register.
    # The denominator is found by raising 2 to the power of the instruction's combo operand. 
    #(So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
    #The result of the division operation is truncated to an integer and then written to the A register.
    #
def adv(A, operand):
    return int(A / (2 ** operand))
    #The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand,
    # then stores the result in register B.
def bxl(B, operand):
    return B ^ operand
    #
    #The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits),
     #then writes that value to the B register.
def bst(operand):
    return operand % 8
    #
    #The jnz instruction (opcode 3) does nothing if the A register is 0. However,
    # if the A register is not zero,
    # it jumps by setting the instruction pointer to the value of its literal operand;
    # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
def jnz(A, operand):
    return A == 0, operand
    #
    #The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C,
    # then stores the result in register B.
    # (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(B,C):
    #ignore operand
    return B ^ C
    #
    #The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
    # then outputs that value. (If a program outputs multiple values, they are separated by commas.)
def out(operand):
    remainder = operand % 8
    return remainder
    #
    #The bdv instruction (opcode 6) works exactly like the adv instruction 
    #except that the result is stored in the B register.
    # (The numerator is still read from the A register.)
def bdv(A, operand):
    return adv(A, operand)
    #
    #The cdv instruction (opcode 7) works exactly like the adv instruction 
    #except that the result is stored in the C register.
    # (The numerator is still read from the A register.)
def cdv(A, operand):
    return adv(A, operand)
    
if __name__ == "__main__":
    data = solve("input_a.txt")
    print(data)

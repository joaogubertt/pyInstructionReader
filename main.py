import os

instructionsLoaded = 0
cyclesA = 0
cyclesB= 0
tClock = 0
execTime = 0    #exec time = instructionsLoaded * clock
count = 0
cpiA = 0
cpiB = 0
dumpPath = 'dump.txt'
 #Remove spaces at the beginning and at the end of the string (in this case each line is a String)
with open(dumpPath, 'r') as dumpFile:
    instructions = [instruction.strip() for instruction in dumpFile]

tClock = int(input("Tempo de Clock: "))
os.system('cls')
print("Organização A:")
rA = int(input("r: "))
uA = int(input("u: "))
jA = int(input("j: "))
bA = int(input("b: "))
sA = int(input("s: "))
arithmeticA = int(input("arithmetic: "))
ecallA = int(input("ecall: "))
loadA = int(input("load: "))
os.system('cls')
print(uA, jA, arithmeticA, rA, bA, sA, loadA, ecallA, cyclesA)
print("Organização B:")
rB = int(input("r: "))
uB = int(input("u: "))
jB = int(input("j: "))
bB = int(input("b: "))
sB = int(input("s: "))
arithmeticB = int(input("arithmetic: "))
ecallB = int(input("ecall: "))
loadB = int(input("load: "))

def cyclesCount(u, j, arithmetic, r, b, s, load, ecall):
    cycles = 0
    for i in range(len(instructions)): 
        if (instructions[i][25:32] == "0110111" or instructions[0][25:32] == "0010111"):
            cycles = cycles + u
        elif(instructions[i][25:32] == "1101111"):
            cycles = cycles + j
        elif(instructions[i][25:32] == "1100111" or instructions[i][25:32] == "0010011"):
            cycles = cycles + arithmetic
        elif(instructions[i][25:32] == "0110011"):
            cycles = cycles + r
        elif(instructions[i][25:32] == "1100011"):
            cycles = cycles + b
        elif(instructions[i][25:32] == "0100011"):
            cycles = cycles + s
        elif(instructions[i][25:32] == "0000011"):
            cycles = cycles + load
        elif(instructions[i][25:32] == "1110011"):
            cycles = cycles + ecall
    return cycles
    
cyclesA = cyclesCount(uA, jA, arithmeticA, rA, bA, sA, loadA, ecallA)
cyclesB = cyclesCount(uB, jB, arithmeticB, rB, bB, sB, loadB, ecallB)
instructionsLoaded = len(instructions)
cpiA = cyclesA/instructionsLoaded
cpiB = cyclesB/instructionsLoaded
print(cyclesA)
print(cyclesB)
print(instructionsLoaded)

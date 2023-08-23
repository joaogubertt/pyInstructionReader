import os

instructionsLoaded = 0
cyclesA = 0
cyclesB= 0
tClockA = 0
tClockB = 0
execTime = 0    #exec time = instructionsLoaded * clock
count = 0
cpiA = 0
cpiB = 0
performanceA = 0
performanceB = 0
dumpPath = 'dump.txt'
 #Remove spaces at the beginning and at the end of the string (in this case each line is a String)
with open(dumpPath, 'r') as dumpFile:
    instructions = [instruction.strip() for instruction in dumpFile]


print("Organização A:")
tClockA = int(input("Tempo de Clock: "))
rA = int(input("r: "))
uA = int(input("u: "))
jA = int(input("j: "))
bA = int(input("b: "))
sA = int(input("s: "))
arithmeticA = int(input("arithmetic: "))
ecallA = int(input("ecall: "))
loadA = int(input("load: "))
os.system('cls')

print("Organização B:")
tClockB = int(input("Tempo de Clock: "))
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
cpiA = cyclesA/instructionsLoaded #average cycle per instruction A
cpiB = cyclesB/instructionsLoaded #average cycle per instruction B
print("Ciclos da CPU A: ", cyclesA)
print("Ciclos da CPU B: ", cyclesB)
performanceA = tClockA * cyclesA
performanceB = tClockB * cyclesB
if performanceA > performanceB:
    dif = performanceA/performanceB
    print("O Desempenho da organização B é ", dif, " vezes mais rápido que A")
elif performanceB/performanceA:
    dif = performanceB/performanceA
    print("O Desempenho da organização A é ", dif, " vezes mais rápido que A")
else:
    print("Ambas organizações possuem o mesmo desempenho")  

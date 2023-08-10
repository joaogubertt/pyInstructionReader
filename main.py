u = 2
j, b= 3, 3
r, s, arithmetic, ecall = 4, 4, 4, 4
load = 5
instructionsLoaded = 0
cycles = 0
execTime = 0    #exec time = instructionsLoaded * clock
nomes = ["joaopedrogubertt", "pedro"]

dumpPath = 'dump.txt'
 #Remove spaces at the beginning and at the end of the string (in this case each line is a String)
with open(dumpPath, 'r') as dumpFile:
    instructions = [instruction.strip() for instruction in dumpFile]

for i in range(len(instructions)):
    if (instructions[i][25:32] == "0110111" or instructions[0][25:32] == "0010111"):
        cycles = cycles + u
    elif(instructions[i][25:32] == "1101111"):
        cycles = cycles + j
    elif(instructions[i][25:32] == "1100111" or instructions[i][25:32] == "0010011"):
        cycles = cycles + arithmetic
    elif(instructions[i][25:32] == ""):
        cycles = cycles + r
    elif(instructions[i][25:32] == ""):
        cycles = cycles + b
    elif(instructions[i][25:32] == ""):
        cycles = cycles + s
    elif(instructions[i][25:32] == ""):
        cycles = cycles + load
    elif(instructions[i][25:32] == ""):
        cycles = cycles + ecall
    
print(instructions[0][25:32])
print(cycles)
# To Do ✔:
# Make the comparisons
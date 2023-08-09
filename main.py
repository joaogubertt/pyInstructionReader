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

if (instructions[0][24:31] == "0001001"):
    print('oi')

print (type(instructions[0][25:31]))
print(instructions[0][24:31])
# To Do ✔:
# Make the comparisons
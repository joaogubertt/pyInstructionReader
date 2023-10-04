import os

#TRATAR BRANCH NOP - ok
#FORWARDING IMPLEMENTACAO - ok 
#REORDENACAO IMPLEMENTACAO

nopInstruction = "00000000000000000000000000010011"
instructionsLoaded = 0
cyclesA = 0
cyclesB= 0
tClockA = float(0.00)
tClockB = float(0.00)
execTime = float(0.00)    #exec time = instructionsLoaded * clock
count = 0
cpiA = 0
cpiB = 0
performanceA = float(0.00)
performanceB = float(0.00)
dumpPath = 'dump.txt'
typeInstruction = []

with open(dumpPath, 'r') as dumpFile:
    instructionsReaded = [instruction.strip() for instruction in dumpFile]

def cyclesCount(u, j, arithmetic, r, b, s, load, ecall, instructions):
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
    os.system('cls')
    cycles = 0
    for i in range(len(instructions)): 
        if (instructions[i][25:32] == "0110111" or instructions[0][25:32] == "0010111"):
            cycles = cycles + u
            typeInstruction.append('u')
        elif(instructions[i][25:32] == "1101111"):
            cycles = cycles + j
            typeInstruction.append('j')
        elif(instructions[i][25:32] == "1100111" or instructions[i][25:32] == "0010011"):
            cycles = cycles + arithmetic
            typeInstruction.append('a')
        elif(instructions[i][25:32] == "0110011"):
            cycles = cycles + r
            typeInstruction.append('r')
        elif(instructions[i][25:32] == "1100011"):
            cycles = cycles + b
            typeInstruction.append('b')
        elif(instructions[i][25:32] == "0100011"):
            cycles = cycles + s
            typeInstruction.append('s')
        elif(instructions[i][25:32] == "0000011"):
            cycles = cycles + load
            typeInstruction.append('l')
        elif(instructions[i][25:32] == "1110011"):
            cycles = cycles + ecall
            typeInstruction.append('e')
    return cycles

def monocycleCalc(uA, jA, arithmeticA, rA, bA, sA, loadA, ecallA, uB, jB, arithmeticB, rB, bB, sB, loadB, ecallB, instructions):
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
    
def nopInsertion(instructions):
    #instructions[i][25:32] == "0100011"
    #13:18 != 20:25 13:18!=20:25
    #rd = 20:25
    #rs1 = 13:18 
    #rs2 = 7:12
    instructionsWithNop = instructions.copy()
    counter = 0
    nopCounter = 0
    for i in instructions:
        cl1 = counter -1
        cl2 = counter -2
        print("rs1 instrucao: " + str(counter) + " " + i[13:18] + " rs2 instrucao: "+ str(counter) + " " + i[7:12] + "\n")
        if counter == 0:
            zero = 0
        elif counter == 1:
            #print("rd - 1 " + instructions[cl1][20:25] + "\n")
            #print("rs1 instrucao: " + str(counter) + " " + i[13:18] + " rs2 instrucao: "+ str(counter) + " " + i[7:12] + "\n")
            if instructions[counter][13:18] == instructionsWithNop[nopCounter-1][20:25] or instructions[counter][7:12] == instructionsWithNop[nopCounter-1][20:25]:
                #print("instrucao " + str(counter) + instructionsWithNop[counter][13:18] + " = " + "instruccao " + str(counter -1) + instructionsWithNop[counter-1][20:25])
                #print("  ou instrucao " + str(counter) + instructionsWithNop[counter][7:12] + " = " + "instruccao " + str(counter -1) + instructionsWithNop[counter-1][20:25])
                for ins in range(2):
                    instructionsWithNop.insert(nopCounter, nopInstruction)
                    nopCounter += 1
        else:
            #print("rd - 1 " + instructions[cl1][20:25])
            #print("rd - 2 " + instructions[cl2][20:25])
            if instructions[counter][13:18] == instructionsWithNop[nopCounter-1][20:25] or instructions[counter][7:12] == instructionsWithNop[nopCounter-1][20:25]:
                for ins in range(2):
                    instructionsWithNop.insert(nopCounter, nopInstruction)
                    nopCounter += 1
            if instructions[counter][13:18] == instructionsWithNop[nopCounter-2][20:25] or instructions[counter][7:12] == instructionsWithNop[nopCounter-2][20:25]:
                instructionsWithNop.insert(nopCounter, nopInstruction)  
                nopCounter += 1
        counter += 1
        nopCounter += 1
    print(instructionsWithNop)
    print(counter, " || ", nopCounter, "\n")
    return instructionsWithNop

def pipelineCyclesCounter(instructionsSet):
    #tcpu = i * cpi *tclock
    i = len(instructionsSet)
    cpipipeline = (5+1*(i-1))/i
    tclock = float(input("Entre com o tempo de clock máximo de seu programa (em segundos): "))
    cpi = float((5 + 1*(i - 1)) / i)
    tcpu = float(i * cpi * tclock)
    print("Tempo de execução do programa na arquitetura pipeline: ", tcpu)
    return tcpu

def forwarding(instructions):
    instructionsWithForwarding = instructions.copy()
    counter = 0
    nopCounter = 0
    for i in instructions:
        if counter != 0:
            if counter == 1:
                #print("instrucao " + str(counter) + instructionsWithForwarding[counter][13:18] + " = " + "instruccao " + str(counter -1) + instructionsWithForwarding[counter-1][20:25])
                #print("  ou instrucao " + str(counter) + instructionsWithForwarding[counter][7:12] + " = " + "instruccao " + str(counter -1) + instructionsWithForwarding[counter-1][20:25])
                if instructions[counter][13:18] == instructionsWithForwarding[nopCounter-1][20:25] or instructions[counter][7:12] == instructionsWithForwarding[nopCounter-1][20:25] and instructionsWithForwarding[counter-1][25:32] == "0000011":
                    for ins in range(2):
                        instructionsWithForwarding.insert(nopCounter, nopInstruction)
                        nopCounter += 1
            else:
                if instructions[counter][13:18] == instructionsWithForwarding[nopCounter-1][20:25] or instructions[counter][7:12] == instructionsWithForwarding[nopCounter-1][20:25] and instructionsWithForwarding[counter-1][25:32] == "0000011":
                    instructionsWithForwarding.insert(nopCounter, nopInstruction)
                    nopCounter += 1
        counter += 1
        nopCounter += 1
    print(instructionsWithForwarding)
    print(counter, " || ", nopCounter, "\n")
    return instructionsWithForwarding

def instructionReorderingNop(instructions):
    #Aqui o conceito é basicamente mudar as instruções de local de modo a diminuir a quantidade de NOP  
    #Aqui não é utilizado o conceito de forwarding
    reorderedInstructions = instructions.copy()
    aux = None
    counter = 0
    result = []
    listLastIndexItem = len(reorderedInstructions) - 1
    for i in reorderedInstructions:
        if (counter == 0):
            zero = 0
        elif(counter == listLastIndexItem):
            zero = 0
        else:
            if (reorderedInstructions[counter][13:18] == reorderedInstructions[counter-1][20:25] or reorderedInstructions[counter][7:12] == reorderedInstructions[counter-1][20:25]):
               aux = reorderedInstructions[counter]
               reorderedInstructions[counter] = reorderedInstructions[counter + 1] 
               reorderedInstructions[counter + 1] = aux
               aux = reorderedInstructions[counter + 1]
               reorderedInstructions[counter + 1] = reorderedInstructions[counter + 2] 
               reorderedInstructions[counter + 2] = aux
               counter = - 1
            elif (reorderedInstructions[counter][13:18] == reorderedInstructions[counter-2][20:25] or reorderedInstructions[counter][7:12] == reorderedInstructions[counter-2][20:25] and counter > 1):
               aux = reorderedInstructions[counter]
               reorderedInstructions[counter] = reorderedInstructions[counter + 1] 
               reorderedInstructions[counter + 1] = aux
            else:
                counter += 1 
    #print(reorderedInstructions)
    result = nopInsertion(reorderedInstructions)
    print(result)

def instructionReorderingForwarding(instructions):  
    reorderedInstructions = instructions.copy()
    aux = None
    counter = 0
    listLastIndexItem = len(reorderedInstructions) - 1
    for i in reorderedInstructions:
        if (counter == 0):
            zero = 0
        elif(counter == listLastIndexItem):
            zero = 0
        else:
            if (reorderedInstructions[counter][13:18] == reorderedInstructions[counter-1][20:25] or reorderedInstructions[counter][7:12] == reorderedInstructions[counter-1][20:25]):
               aux = reorderedInstructions[counter]
               reorderedInstructions[counter] = reorderedInstructions[counter + 1] 
               reorderedInstructions[counter + 1] = aux
               aux = reorderedInstructions[counter + 1]
               reorderedInstructions[counter + 1] = reorderedInstructions[counter + 2] 
               reorderedInstructions[counter + 2] = aux
               counter = - 1
            elif (reorderedInstructions[counter][13:18] == reorderedInstructions[counter-2][20:25] or reorderedInstructions[counter][7:12] == reorderedInstructions[counter-2][20:25] and counter > 1):
               aux = reorderedInstructions[counter]
               reorderedInstructions[counter] = reorderedInstructions[counter + 1] 
               reorderedInstructions[counter + 1] = aux
            else:
                counter += 1 
    #print(reorderedInstructions)
    result = (forwarding(reorderedInstructions))
    print(result)

instructionReorderingNop(instructionsReaded)
#pipelineCyclesCounter(forwarding(instructionsReaded))
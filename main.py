dumpPath = 'dump.txt'
 #Remove spaces at the beginning and at the end of the string (in this case each line is a String)
with open(dumpPath, 'r') as dumpFile:
    instructions = [instruction.strip() for instruction in dumpFile]

# To Do ✔:
# Make the comparisons
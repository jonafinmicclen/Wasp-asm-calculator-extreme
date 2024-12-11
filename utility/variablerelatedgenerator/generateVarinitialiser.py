varnames = []
start = 0x10F0

with open('utility/variablerelatedgenerator/allvars.txt', 'r') as file:
    for line in file:
        if ':' in line:
            varnames.append(line.split(':')[0])

with open('utility/variablerelatedgenerator/variableinitialiser.txt', 'w') as file:
    for name in varnames:
        file.write(f'{name}: DC.W {hex(start)}\n')
        start += 1
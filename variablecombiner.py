allvars = []

with open('allvariables.txt', 'r') as file:
    for line in file:
            
        allvars.append(line.split(':')[0])
        
allvarsunique = list(set(allvars))
allvarsunique.remove('\n')


countFrom = 0x1FFF

with open('uniquevarespreformatted.txt', 'w') as file:
    for varname in allvarsunique:
        file.write(f'{varname}: DC.W {hex(countFrom).upper()}\n')
        countFrom -= 1
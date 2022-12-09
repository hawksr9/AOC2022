#sourcefile = open(r'C:\Users\srost\Downloads\input.txt', 'r')
#elfcontent = [line.strip() for line in sourcefile[:1]]
#elfcontent = sourcefile.readlines()
#sourcefile.close
with open(r'C:\Users\srost\Downloads\input.txt', 'r') as f:
    lines = f.readlines()
    elfcontent = [entry.strip() for entry in lines]

each_elf = []
total = 0

for line in elfcontent:
    if line != '':
        total += int(line)
    elif line == '':
        each_elf.append(total)
        total = 0
each_elf.append(total)
print(max(each_elf))



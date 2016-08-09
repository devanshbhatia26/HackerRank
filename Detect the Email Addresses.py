import re
pattern = re.compile(r'([\w_\.]+)@([\w\.]+)(\w)')
lines = ' '
for i in range(input()):
    lines+=raw_input()
    lines+=' '
#print pattern.findall(lines)
print ";".join(sorted(list(set([i[0]+'@'+i[1]+i[2] for i in pattern.findall(lines)]))))

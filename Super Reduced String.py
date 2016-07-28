import re
pattern = re.compile(r'([a-z])(\1)')
s =  raw_input()
while pattern.search(s):
    s = re.sub(r'([a-z])(\1)','',s)
if not s:
    print "Empty String"
else:
    print s
    
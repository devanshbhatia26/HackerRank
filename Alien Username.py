import re
pattern = re.compile(r'^[_\.][0-9]+[a-zA-Z]*(_)?$')
for _ in range(input()):
    if pattern.search(raw_input()):
        print "VALID"
    else:
        print "INVALID"

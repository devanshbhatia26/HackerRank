import re
tags = re.compile(r'<\s*/?\s*([a-z0-9]+)[^>]*\s*/?\s*>')
lines = ''
for i in range(input()):
    lines+=raw_input()
    lines+=' '
print ";".join(sorted(list(set(tags.findall(lines)))))


import re
lines = ''
for _ in range(input()):
    lines+=raw_input()
    lines+=' '
lines = lines.split()
for _ in range(input()):
    word = raw_input()
    ans = 0
    i = word.index('our')
    string=r'^'
    if i==0:
        string+=r'(our|or)'+word[3:]
    else:
        string+= word[:i]+r'(our|or)'
    if i<(len(word)-3) and i!=0:
        string+=word[i+3:]
    string+="$"
    pattern = re.compile(string)
    for w in lines:
        if pattern.search(w):
            ans+=1
    print ans

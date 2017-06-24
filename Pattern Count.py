import sys

def patternCount(s):
    st = []
    ans = 0
    for i in s:
        if i == '1':
            if len(st)>=2 and st[-1]=='0' and st[-2]=='1':
                ans +=1
            st.append('1')
        elif i == '0':
            if st and not st[-1]=='0':
                st.append('0')
        else:
            st = []
    return ans
                
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)


for i in range(input()):
    s = raw_input()
    stack = []
    flag = 1
    for char in s:
        if char=="(" or char=="[" or char=="{":
            stack.append(char)
        elif stack and((char==")" and stack[-1]=="(") or (char=="]" and stack[-1]=="[") or (char=="}" and stack[-1]=="{")):
            del stack[-1]
        else:
            print "NO"
            flag = 0
            break
    #print stack
    if flag and not stack:
        print "YES"
    elif flag:
        print "NO"
            
main = []
maxim = 0
for i in range(input()):
    temp = raw_input()
    if temp[0]=="1":
        temp = map(int,temp.split())
        main.append(temp[1])
        if main[-1]>maxim:
            maxim = main[-1]
    elif temp[0]=="2":
        if main[-1]==maxim:
            del main[-1]
            if main:
                maxim = max(main)
            else:
                maxim = 0
        else:
            del main[-1]
    else:
        print maxim
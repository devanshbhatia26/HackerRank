class stack:
    
    def __init__(self):
        self.top = -1
        self.st = []
    
    def push(self,n):
        self.st.append(n)
        self.top+=1
    
    def pop(self):
        if self.top==-1:
            return
        self.top-=1
        return self.st.pop()
    
    def peek(self):
        return self.st[self.top]
    
    def isEmpty(self):
        if self.top==-1:
            return True
        return False


st = stack()
n = input()
arr = map(int,raw_input().strip().split())
ans = 0
st.push(arr[0])
for i in range(1,n):
    ans = max(ans,st.peek()^arr[i])
    while (not st.isEmpty()) and arr[i] < st.peek():
        ans = max(ans,st.pop()^arr[i])
    if not st.isEmpty():
        ans = max(ans,st.peek()^arr[i])
    st.push(arr[i])
print ans

n=5
for i in range(1,n+1):
    s=0
    for j in range(1,1+i):
        print(j,end="")
        s+=j
    for j in range(0,n-i):
        print(" ",end="")
        
    print(s)
"""
1    1
12   3
123  6
1234 10
1234515
"""

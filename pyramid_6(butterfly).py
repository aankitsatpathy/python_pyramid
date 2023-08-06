for i in range(0,6):
    for j in range(0,i+1):
        print(i+1,end="")
    for j in range(0,5-i):
        print(" ",end="")
    for j in range(0,5-i):
        print(" ",end="")
    for j in range(0,i+1):
        print(i+1,end="")
    print("")
for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end="")
    for j in  range(0,6-i):
        print(" ",end="")
    for j in range(0,6-i):
        print(" ",end="")
    for j in range(0,i):
        print(i,end="")
    print("")
  """
1          1
22        22
333      333
4444    4444
55555  55555
666666666666
55555  55555
4444    4444
333      333
22        22
1          1
  """

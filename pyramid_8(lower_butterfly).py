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
55555  55555
4444    4444
333      333
22        22
1          1
"""

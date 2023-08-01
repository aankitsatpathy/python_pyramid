n=9
for i in range(0,n,2):
    for j in range(0,int((n-i)/2)):
        print(" ",end="")
    for j in range(0,i+1):
        print(i,end="")
    print("")
/*
    0
   222
  44444
 6666666
888888888
*/

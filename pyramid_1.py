n=9
for i in range(0,n):
    for j in range(0,n-i+1):
        print(" ",end="")
    for j in range(0,i+1):
        print(i,end="")
    print("")
/*
          0
         11
        222
       3333
      44444
     555555
    6666666
   77777777
  888888888
*/

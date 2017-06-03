import math

print("Enter number of variables: ")
n = int(input())

a = int(math.sqrt(n))+1
while(a >= 1):
    if(n%a==0):
        b = n//a
        print("Optimal Matrix Dimensions are: ",a," X ",b)
        break
    else:
        a -= 1

# PYTHON PROGRAM TO FIND FACTORIAL OF ANY ENTERED NUMBER 
num = int(input("Enter any number whose factorial your want: "));
fact = 1;
for x in range(1,num+1):
    fact *= x;

print(f"factorial of {num} is {fact}");
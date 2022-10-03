# PYTHON PROGRAM TO FIND THAT ENTERED NUMBER IS A ARMSTRONG OR NOT 
num = int(input("Enter any number to find that it is a armstrong or not: "));
leng = len(str(num));
sum = 0;
num1 = str(num)
for x in num1:
    y = int(x)**leng;
    sum = sum + y;
if sum == num:
    print(f"{num} is an armstrong number:");
else:
    print(f"{num} is not an armstrong number:");

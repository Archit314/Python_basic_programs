# PYTHON PROGRAM TO FIND FABONICAI SERIES TILL nth NUMBER: 
num = int(input("Enter any number till where you want fabonicai series: "));
a =0;
b= 1;
print(a,"\n",b)
fab =0;
for x in range(1,num):
    fab = a + b;
    a = b;
    b = fab;
    print(fab)

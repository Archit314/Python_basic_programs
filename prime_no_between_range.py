# PYTHON PROGRAM TO FIND PRIME NUMBER BETWEEN THE ENTERED RANGE: 
start = int(input("Enter the starting number from where you want to find prime number: "));
end = int(input("Enter the second number till where you want to find prime number: "));
f = 0;
total = 0;
for x in range(start, end+1):
    j = x;
    for y in range(1,j+1):
        if x % y == 0:
            f+=1;
    if f==2:
        print(f"{x} prime")
        total += 1;
    else:      
        print(f"{x} is not prime")
    f=0;
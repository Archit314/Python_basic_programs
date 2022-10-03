# PYTHON PROGRAM FOR SUM OF SQUARE OF FIRST N NATURAL NUMBERA:
num = int(input("Enter a number till where you want sum of square of natural number: "));
sum = 0;
for x in range(1, num+1):
    x = x**2;
    sum += x;
print(f"Sum of entered n natural numbers is = {sum}");
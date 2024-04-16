n = 4
a = int(input("Enter the first digit: "))
b = int(input("Enter the second digit: "))
c = int(input("Enter the third digit: "))
d = int(input("Enter the fourth digit: "))
pow_sum =pow(a, n) + pow(b, n) + pow(c, n) + pow(d, n)

if pow_sum == (a**n + b**n + c**n + d**n):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")




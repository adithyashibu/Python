
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a = num1
b = num2
while a != b:
    if a > b:
        a=a-b
    else:
        b=b-a
gcd = a 
lcm = (num1 * num2) // gcd

print(f"The GCD of {num1} and {num2} is: {gcd}")
print(f"The LCM of {num1} and {num2} is: {lcm}")

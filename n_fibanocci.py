n = int(input("Enter N: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
a = list()
ab_a = list()
number1 = int(input("how many numbers for list 1 : "))

for ele in range(0, number1):
    a.append(int(input("Enter a number in list 1 : ")))
    if a[ele] >= 0:
        ab_a.append(a[ele])
print(f'Input: {a}   Output:{ab_a}')

b = list()
ab_b = list()
number2 = int(input("how many numbers for list 2 : "))

for ele in range(0, number2):
    b.append(int(input("Enter a number in list 2 : ")))
    if a[ele] >= 0:
        ab_b.append(b[ele])
print(f'Input: {b}   Output:{ab_b}')
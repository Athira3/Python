import math

n1 = int(input('Enter first number(four digit):'))
n2 = int(input('Enter last four number(four digit):'))
list = []
while n1 <= n2:
    if n1 % 2 == 0 and math.sqrt(n1) == int(math.sqrt(n1)):
        list.append(n1)
    n1 = n1 + 1
print(list)

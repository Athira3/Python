def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


n1 = abs(int(input('Enter a number:')))
n2 = abs(int(input('Enter a number:')))
print('G.C.D = ', gcd(n1, n2))
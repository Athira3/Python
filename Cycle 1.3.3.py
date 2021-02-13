n1 = float(input('Enter a number:'))
n2 = float(input('Enter a number:'))
n3 = float(input('Enter a number:'))
big = 0
if (n1 > n2) and (n1 > n3):
    big = n1
elif (n2 > n1) and (n2 > n3):
    big = n2
else:
    big = n3
print('Biggest number is:', big)
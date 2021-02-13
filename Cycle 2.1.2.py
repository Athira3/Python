n1 = 0
n2 = 1
count = 0
num = int(input('Number of terms in the series:'))
if num <= 0:
    print('Enter a positive number:')
elif num == 1:
    print('fibonacci series upto', num)
    print(n1)
else:
    print('fibonacci series upto', num)
    while count < num:
        print(n1, end=" ")
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count = count + 1

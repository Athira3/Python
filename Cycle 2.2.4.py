def factor(num):
    print('Factors are:')
    for i in range(1,num+1):
        if num % i == 0:
            print(i)


n = int(input('Enter a number:'))
factor(n)
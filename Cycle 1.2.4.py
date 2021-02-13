list1 = []
list2 = []
n1 = int(input('Enter the elements of 1st list:'))
n2 = int(input('Enter the elements of 2st list:'))
print('Enter %d integers:' % n1)
for i in range(0, n1):
    n = int(input())
    list1.append(n)
print('Enter %d integers:' % n2)
for i in range(0, n2):
    n = int(input())
    list2.append(n)
if len(list1) == len(list2):
    print("list are of same length.")
else:
    print('list are of different length.')
if sum(list1) == sum(list2):
    print('list sum are same.')
else:
    print('list sum are not same.')
N = (set(list1)).intersection(set(list2))
if len(N)!=0:
    print('list has common values')
else:
    print('list has no common values')
List = []
n = int(input("Enter the number of elements:"))
print("Enter %d integers:" % n)
for i in range(0, n):
    value = int(input())
    if value > 100:
        List.append('Over')
    else:
        List.append(value)
print(List)
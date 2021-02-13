List = []
n = int(input("Enter the number of elements:"))
print("Enter %d integers:" % n)
for i in range(0, n):
    List.append(int(input()))
print("Squares are:")
for i in List:
    print(i*i)
List = []
n = int(input("Enter the number of elements:"))
print("Enter %d integers:" % n)
for i in range(0, n):
    List.append(int(input()))
print("Positive integers are:")
for i in List:
    if i > 0:
        print(i )
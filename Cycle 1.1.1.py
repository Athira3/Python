current_year = int(input("Enter current year:"))
year = int(input("Enter the year upto which leap year are to be displayed:"))
print("The Leap years are:")
for i in range(current_year, year+1):
    if i % 4 == 0:
        print(i)
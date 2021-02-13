list = ['Anu', 'Jacob', 'Vidhya', 'Rahul']
count = 0
for word in list:
    word = word.lower()
    for i in word:
        if i == 'a':
            count = count + 1
print('List is:', list)
print("Occurrence of 'a' in list:", count)
def occurrence(string):
    word = string.split()
    count = dict()
    for i in word:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1
    return count

line = input('Enter a sentence:')
print(occurrence(line))
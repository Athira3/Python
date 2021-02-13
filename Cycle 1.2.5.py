string = input('Enter a string:')
letter = list(string)
char = letter[0]
n = len(letter)
for i in range(1, n):
    if letter[i] == char:
        letter[i] = '$'
print(''.join(letter))
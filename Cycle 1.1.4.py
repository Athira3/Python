list = []
vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter any word:')
word = word.lower()
for i in word:
    if (i in vowels) and (i not in list):
        list.append(i)
print('Vowels present are:', *list)
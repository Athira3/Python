d = {'manu': 10, 'ammu': 5, 'haritha': 15}
print('The dictionary is:', d)
list = list(d.items())
list.sort()
print('Ascending order:', list)
list.sort(reverse=True)
print('Descending order:', list)

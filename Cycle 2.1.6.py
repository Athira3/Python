dict={}
string=input('Enter a string:')
for i in string:
    keys=dict.keys()
    if i in keys:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print('Character frequency of the string is', dict)
def ing(str):
    if (len(str) >= 3 and str[-3:] == 'ing'):
        str = str + 'ly'
    else:
        str = str + 'ing'
    print('modified string is ', str)


string = input('Enter a string:')
ing(string)
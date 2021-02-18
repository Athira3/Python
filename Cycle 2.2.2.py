def long(list2):
    maxi=len(list2[0])
    temp=list2[0]
    for i in list2:
        if(len(i)>maxi):
            maxi=len(i)
            temp=i
    print('Longest word is ', temp)


list1=['python','java','c','php','c++']
long(list1)
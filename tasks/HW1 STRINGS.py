"""
def is_palind(string):
    l = len(string)
    for idx in range(l//2):    # 5/2 = 2.5 = 2 which is int and removing 0.5 that is it
        if(string[idx] != string[l-idx-1]):
            return False
    return True

print(is_palind('madam'))
"""
"""
def group(string):
    temp_lst = ''
    string = string.lower()
    for idx,item in enumerate(string):
        if(idx != 0 and temp_lst[len(temp_lst)-1] != item ): #temp_lst has another index other than string
           temp_lst += ','
        temp_lst += item

    return temp_lst

print(group('abcdDdDdeEfa'))


def group(string):
    string = string.lower()
    sep = ''
    l = len(string)
    for idx,item in enumerate(string):
            sep = ',' if string[idx - 1] != item and idx != l  else ''
            print(end=sep)
            print(item,end = '')
    print()



print(group('abcdDdDdeEfa'))
"""
'''
def conc_string(string1,string2):
    #temp_lst = [string1,string2]   #instead of this use zip function
    print(list(zip(string1,string2)))
    for s1,s2 in zip(string1,string2):
       print(s1 + s2,end='')

    if(len(string1) < len(string2)):     # canonicalisation method 
        string1,string2 = string2,string1
    if(len(string1) > len(string2)):
        print(string1[len(string2):],end='')
    print()

print(conc_string('abc','defeee'))
'''
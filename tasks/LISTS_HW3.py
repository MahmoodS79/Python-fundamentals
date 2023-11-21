"""def find_smallest_of_givenType(list1,_type):
    #LIMITED SOL TO STR , FLOAT AND INTS
    _min = list1[0]
    for i in list1:
        if(type(i) == _type and type(i) == str):
            _min = i
        if(type(i) == _type and _min > i):
            _min = i
    return _min

list1=[10,-2.5,20,5,'mostafa',5.2,'Ziad']
print(find_smallest_of_givenType(list1,type(0)))
print(find_smallest_of_givenType(list1,type(0.0)))
print(find_smallest_of_givenType(list1,type('')))

def _find_smallest_of_givenType(list1,_type):
    #General
    temp_list=[]
    '''for i in list1:
        if(type(i) is _type):
            temp_list.append(i)
    '''
    temp_list=[i for i in list1 if(type(i)is _type)] # same as above
    if(len(temp_list) == 0):
        return None
    return min(temp_list)

print(_find_smallest_of_givenType(list1,type(0)))
print(_find_smallest_of_givenType(list1,type(0.0)))
print(_find_smallest_of_givenType(list1,type('')))
"""
"""def sublist(list1,list2):
    pre_index=0
    index=0
    for i in range(len(list1)):
        if(len(list2) == 0):
            break
        if(list1[i] == list2[0]):
            pre_index = index
            index = i
            list2.pop(0)

    return (len(list2)==0 and (index-pre_index == 1))
print(sublist([10,-10,20,25,2,7,2,3],[20,25,3]))
"""
'''def sliding_window(list1,num):  #check video 0028
    l=len(list1)
    max_sum=0
    

    for i in range(l):
        sum = 0
        for j in range(num):
            sum += list1[i+j]
        if(max_sum < sum):
            max_sum = sum
            idx=i
        if ( i + num == l ):
             return 'starts at '+str(idx)+' and its sum is '+str(max_sum)

print(sliding_window([1,0,3,-4,2,-6,9],3))
print(sliding_window([30,-6,-8,10,2],4))
'''

#there is a code wasn't done about >>>>>>>>> growing up sublists
#there is a code wasn't done about >>>>>>>>> circle and exclution
'''
def longest_subarray(lst):
    best_len = 0
    l=len(lst)
    temp_list = []
    z_c = 0
    o_c = 0
    for i in range(l):
        for j in range(i+1,l):
            temp_list = lst[i : j+1]
            z_c = temp_list.count(0)
            o_c = len(temp_list) - z_c
            if(o_c == z_c):
                if(best_len < len(temp_list)):
                    print(temp_list)
                    best_len = len(temp_list)

    return best_len

print(longest_subarray([1, 1, 1, 0, 0, 1, 0 ,1 ,0]))
'''

lst = ("pyton","is","cool"), ("ay","as","kool")
lst1 = (1,2,3), (4,5,6),(3,3,3)
print(lst)
if(__name__ == '__main__'):
    print("olaal",__name__)
'''
def neg_most_freq(list1): # more general for +ve and -ve values
    _min = min(list1)
    _max = max(list1)
    temp_list=[0]*(_max - _min + 1) #you will shift the freq_array if there is negative items , the shift is equal to _min (you will add to the length of the array)
    #the length of the list1 is not important
    for i in list1:
        temp_list[i-_min] += 1   #ex: the value -10 i will add to it the minimum value of list1

    __max=max(temp_list)
    return temp_list.index(__max)+_min,__max# you need to return the value that is most freq from the list1

print(neg_most_freq([-1,2,-1,3,-1,5,5,5,5]))
'''
"""
def digits_freq(list1):      #you need to count the most freq digits in all numbers in the list1
    temp_list=[0]*10
    for i in list1:
        if(i<0):
            i = -i
        if(i == 0 ):
            temp_list[0] += 1
        while(i!=0):
            digit=i%10
            i=i//10   # you can midify i no problem as it will start from were it entered the loop
            temp_list[digit] += 1

    return temp_list
def _digits_freq(list1):      #you need to count the most freq digits in all numbers in the list1
    #more efficient
    temp_list=[0]*10
    for i in list1:
        i=str(abs(i))
        for j in (i):
            temp_list[int(j)] += 1

    return temp_list


temp_list=_digits_freq([78307, 3, 3, 3,30])
for i in range(10):
    print(i,temp_list[i])
"""



'''
def sub_seq(list2,list1):
    """
    1==1(list2) then 1 is removed from list2,
    2!=4
    3!=4
    4==4 then 4 is removed from list2
    """
    for i in list1:
        if(i == list2[0]):
            list2.pop(0)
    return len(list2) == 0

#print(sub_seq([-10,2,2,2,3],[10,-10,20,25,2,7,2,3]))
print(sub_seq([1,4],[1,2,3,4]))
'''
"""
def rechaman(num):
    #using nested loops
    temp_list=[0]
    pre_value = 0
    count=0
    for i in range(num):
        seq = pre_value-i-1
        if(seq <0 or seq in temp_list):
            seq = pre_value + i + 1
        count += 1   # you need to count till last index
        temp_list.append(seq)
        pre_value = seq
        if(count == num):
            return seq
    return 0    # if num == 0



def _rechaman(num):
    #without nested loops
    if (num == 0):
        return 0
    occurence_list=[0]*num*10   # how many times the values has occures
    pre_value,occurence_list[pre_value] = 0 ,1
    for i in range(1,num+1):  # you must iterate until reaching the index of the value specified
        last_idx_of_prevalue=i-1
        seq = pre_value-last_idx_of_prevalue-1
        if(seq<0 or occurence_list[seq]):
            seq = pre_value + last_idx_of_prevalue + 1
        occurence_list[seq] = 1   # the seq will be corrected
        pre_value=seq               # the seq will be corrected
        if(i==num):
            return seq

    return 0    # if num == 0
print(_rechaman(5))
"""
"""
# how to deal with varaibles inside the loop,IS TO START FROM REVERS
def remove_evenVal_in_list(list1):
    l=len(list1) # must be const as idx and item are constants
    for idx,item in enumerate(reversed(list1)): #NO MEMORY IS CREATED HERE  #if idx=0 is executed then it won't be reused again so using del with lists is not OK
        if(item%2 ==0):
            del list1[l-idx-1]  #delete in the revers order ==== enumertae()

def _remove_evenVal_in_list(list1):
    l=len(list1) # must be const as idx and item are constants
    for idx in range(l):
        if(list1[l-idx-1]%2 == 0):
            del list1[l-idx-1]
def __remove_evenVal_in_list(list1):
    l=len(list1) # must be const as idx and item are constants
    for idx in range(l-1,-1,-1):#stop at 0
        if(list1[idx]%2 == 0):
            del list1[idx]

#list1=[1,2,3,4,5,6]
#list1=[-6,6]
list1=[-111,91,-6,6,2,2,10,3,3,2,99]
__remove_evenVal_in_list(list1)
print(list1)
"""

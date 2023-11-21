"""def mx_sum_pair(list1):
    '''
    more efficient way depending assumption before looping
    '''
    if(len(list1)==0 or len(list1)==1):
        return (0,0)
    max=list1[0]
    max_idx=0
    sec_max=list1[1]
    sec_max_idx=1
    for i in range(1,len(list1)):
        if(list1[i]>max):
            sec_max = max
            sec_max_idx=max_idx
            max=list1[i]
            max_idx=i
    return (max_idx,sec_max_idx)

list1=[1]
idx1,idx2=mx_sum_pair(list1)
print("("+str(idx1)+','+str(list1[idx1])+")","("+str(idx2)+','+str(list1[idx2])+")")


def argmax(list1):
    '''
    very slow approach , many iterations
    '''
    max_idx=list1.index(max(list1))
    _max=max(list1)
    list1[max_idx]=min(list1)-1
    sec_max_idx=list1.index(max(list1))
    sec_max=max(list1)
    list1[max_idx]=_max #because there is an item that's already has been updated
    return (max_idx, sec_max_idx)

list1=[1,2,3]
idx1,idx2=argmax(list1)
print("("+str(idx1)+','+str(list1[idx1])+")","("+str(idx2)+','+str(list1[idx2])+")")
"""
"""def most_freq(list1):
    max_count=0
    max_count_value=None
    l=len(list1)
    for i in range(l):
        var_count = 0
        for j in range(l):
            if(list1[i]==list1[j]):
                var_count += 1
                if(var_count >max_count):
                    max_count=var_count
                    max_count_value=list1[i]
                if(max_count_value>list1[i] and var_count==max_count):
                    max_count_value=list1[i]
    return (max_count_value,max_count)

def most_freq(list1):
    '''
    more efficient but limited values range from 0 to 1000000
    '''
    temp_list=[0]*(max(list1)+1)  # the index of temp_list will be the values of list1 and the values will be the counts
    for i in list1:
        temp_list[i] += 1
    most_count_value=temp_list.index(max(temp_list)) # the 1st index(value) with maximim counts will be returned
    return most_count_value,temp_list[most_count_value]

if(__name__=='__main__'):
    list1=list(map(int,input("enter numbers").split()))
    max_count_val,max_count=most_freq(list1)
    print(max_count_val,max_count)
"""
"""
def min_max_list(list1):
    l=len(list1)
    _max=max(list1)
    _min=min(list1)
    for i in range(l):
        if(_max == list1[i]):
            list1[i]=_min
        elif(_min == list1[i]): #only one and one item must be replaced in the iteration
            list1[i]=_max

list1=[1,2,3,4,4,4,4,1,1,1,1,4333]
min_max_list(list1)
print(list1)
"""

"""
def find_with_last_idx(list2):
    '''
    very un efficient 
    '''
    l=len(list2) # you don't need a list larger than the list2 lenghth
    temp_list=[0]*l
    for i in range(l):
        for j in range(len(list1)):
             if(list2[i] == list1[j]):
                 temp_list[i]=j
        if(temp_list[i]==0):
            temp_list[i]=-1
    for i in range(l):
        print("query "+str(list2[i])+" answer "+str(temp_list[i]))
        
def find_with_last_idx(list1,list2):
   #optimum solution
    m1=max(list1)
    m2=max(list2)
    temp_list=[-1]*(m1+1)
    count=0
    for i in list1:
        temp_list[i]=count
        count += 1
    for i in list2: #loop for just printing the queries
        if(m2 != m1 and m2==i and i not in list1): #the m2 doesn't exist in the list1 and to avoid putting the max as index to the list2(index isn't in range)
            print("query " + str(i) + " answer " + str(-1))
            continue
        if(temp_list[i] == -1):
            print("query " + str(i) + " answer " + str(-1))
            continue
        print("query " + str(i) + " answer " + str(temp_list[i]))

list1=[1 ,3,3,33,3,3]
list2=[7,2,1,100]
#list1=list(map(int,input("Put Nums : ").split()))
#list2=list(map(int,input("what numbers you want to find ").split()))
find_with_last_idx(list1,list2)
"""
'''
def unique_unordered_nums(list1):
        l = len(list1)
        temp_list = []
        for i in range(l):
            count=0
            for j in range(l):
                if(list1[i] in temp_list):   #may be list1[i] == temp_list[j] but an error because of index pit of range
                    count += 1 #YOU DON'T NEED TO COOUNT JUST DETECT ANY EXISTENCE
                    break
            if(count == 0):
                temp_list.append(list1[i])

        return temp_list


def eff_unique_unordered_nums(list1):
    #more efficient
    temp_list = []
    for idx,item in enumerate(list1):
        if(idx==0 or temp_list[idx] != temp_list[idx-1]):
            temp_list.append(item)
    return temp_list


def unique_ordered_nums(list1):
    l = len(list1)
    temp_list = []  # the index of temp_list will be the values of list1 and the values will be the counts
    for i in range(l):
        count = 0
        for j in range(l):
            if (list1[i] in temp_list):
                count += 1
                break
        if (count == 0):
            temp_list.append(list1[i])

    temp_list.sort()

    return temp_list



print(unique_unordered_nums([1,22,22,4,5,6,6]))

'''
"""
def smallest_result(list1):
    l=len(list1)
    _min=None #None is a special object
    for i in range(l):
        for j in range(i+1,l):
            cur=list1[i]+list1[j]+j-i
            if(i==0 or cur < _min):
                _min=cur  
    return _min
print(smallest_result([20,1,9,4]))
"""

def three_min(list1):
    #very efficient code
    l=len(list1)
    temp_list=[]
    for i in range(l):
        temp_list.append(list1[i])
        if(len(temp_list)>3):
            temp_list.sort()
            temp_list.pop()
    temp_list.sort()
    return temp_list
print(three_min([1,2,0,342,342234]))

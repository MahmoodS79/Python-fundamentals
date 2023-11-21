


'''
lst=[[1,2,3],
     [4,5,4],
     [12,3,10]]
i = 0
if(len(lst[0]) != len(lst) and len(lst[0]) > len(lst)):
    i=1

left_d=sum([lst[col][col] for col in range(len(lst[0])-i)])
temp_lst = []
row = 0
for col in range(len(lst[0])-1,i-1,-1):  # in case len(lst)>len(lst[0]) or len(lst)=len(lst[0])  i-1=-1 but col=0 in last
    temp_lst.append(lst[row][col])
    row += 1

print(left_d)
print(sum(temp_lst))

'''


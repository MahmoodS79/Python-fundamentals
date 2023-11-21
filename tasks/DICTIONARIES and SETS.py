# dict1={12:[1,2,('a7a','mah')],'mostafa':20}
# dict1[12].append('mahmood')
# print(dict1)
# list1=[1,2,3,112,321321]
# list3=[2,2,3,4,5444]
# list2 = [item for item in zip(list3,list1)]
# # print(list2)
# # print(*list2)

def printing_last_occurence(list1,values):
    dict1={}
    for i in range(len(list1)):
        dict1.update({list1[i]:i})
    for i in range(len(values)):
        if(values[i] in dict1):
            print("query "+str(values[i])+' answer '+str(dict1[values[i]]))
        else:
            print("query " + str(values[i]) + ' answer ' +'a7a')


if(__name__ == '__main__'):
    list1 = input("enter the list"+'\n').split()
    list_of_values = input("enter the values"+'\n').split()
    printing_last_occurence(list1,list_of_values)

#-1000 500 -1000 70 2 2 70 3 20 20
#2 3 20 70 500 -1000 999
def repeat(sentence):
    for idx,val in enumerate(sentence):
        print(val*(idx+1),end='')
    print()

repeat('mahmood')




'''
def nth_feb(seq_num):
    count = 0   # represents the index of chars in the sequence ex:  1 2 3 4 5      ->>>>>> 5 has count = 5
    before_prev = 0
    prev = 1

    if(seq_num == 1):
        return 0
    elif(seq_num == 2):
        return 1
    else:
        #this block should print all fib seq starting from 0 1
        for i in range(0,100000):
            if(count == seq_num):
                return now
            elif(count >= 2):
                now = prev + before_prev
                #print(str(now)+ ",", end='')
            else:   #a case for printing 0 and 1 first
                #print(str(0)+','+str(1)+',',end='')    #at first you need to print 2 numbers then increase your count
                count += 1    #it represents your index
            count += 1
            if(i != 0):  # i=1  represents count = 3
                before_prev = prev
                prev = now

for i in range(1,100):
    print(i , nth_feb(i))

nth_feb(10)
'''


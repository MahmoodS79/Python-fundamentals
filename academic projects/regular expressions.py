def stateA(n):
    l = len(n)

    if (l == 0): #empty string
        stateD(n)

    elif(l >= 2):   #    the last 'a' must be marked
        if (l==3 and n[0] == 'a'  and n[1] == 'b' and n[2] == 'b'  ): # 'a' is the last
            stateB(n[1:])

        elif (n[0] == 'a'  and n[1] == 'b' ):   #a and b cocatenated any number of times the last 'a' wasn't yet occured
            stateA(n[1:])


        elif (n[0] == 'a' and n[1] == 'a'):     #a and a cocatenated any number of times the last 'a' wasn't yet occured
            stateA(n[1:])

        elif (n[0] == 'b'  ):
            stateA(n[1:])

        else: #'           ':8 and '  ':2 AND ANY WRONG characters
            print("string not accepted")
    else:      #for strings length less than 2  ex: '\n'
            if(n == 'a' or n == 'b'):
                print("string accepted")
            else:
                print("string not accepted")

def stateB(n):
     stateC(n[1:])



def stateC(n):
        stateD(n)


def stateD(n):
    print("string accepted")


if(__name__ == '__main__'):
    n = input()
    '''
    test_cases : 'aaaaaaaaaaaaaaaabbbbbbbbbbbbabb'
                 'aaaaaaaaaaaaaaaabb'
                 'aaaaabac'
                 'aaaaabacabb'
                 'aaaaabaaabb'
                 'aaaaaaaaaaaaaaaab'
    '''
    stateA(n)

""" Question asked in Mathworks interview : Minimum operation of  1. Add by 1 or 2. Multiply by 2
    to get to the target number k """


# Iterative approach

def minOps(k):
    count = 0
    while(k>0):

        if k%2 == 0:
            count +=1
            k=k//2

        else:
            count+=1
            k-=1


    return count


# Recursive approach




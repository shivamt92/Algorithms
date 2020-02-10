import random
import math

def Merge(Left,Right):
    i,j,k = 0,0,0
    Output = [0]*(len(Left) + len(Right))
    while(i<len(Left) and j<len(Right)):
        if Left[i]< Right[j]:
            Output[k] = Left[i]
            i+=1
            k+=1

        else:
            Output[k] = Right[j]
            j+=1
            k+=1

    if i<len(Left):
        Output[k:] = Left[i:]
    else:
        Output[k:] = Right[j:]

    return Output


def MergeSort(arr):

    if len(arr)<2:
        return arr

    half = math.floor(len(arr)/2)

    left = MergeSort(arr[0:half])
    right = MergeSort(arr[half:])
    output = Merge(left,right)
    return output

'''
    if arr[0]>arr[1]:
        temp = arr[0]
        arr[0]= arr[1]
        arr[1] = temp
        print(arr)

'''
# Merge and Finish bismillah
random.seed(3)
arr1 =[]
for i in range(12):
    arr1.append(random.randint(1,10))

print(arr1)

print(MergeSort(arr1))
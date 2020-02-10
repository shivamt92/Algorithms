import random


def partition(arr,start,end):

    max_piv = start

    piv = arr[end]
    #print('new loop')
    for i in range(start,end):
        if arr[i] <= piv and i>=max_piv:

            arr[i],arr[max_piv] = arr[max_piv],arr[i]
            max_piv +=1


    arr[max_piv],arr[end] = arr[end],arr[max_piv]

    return max_piv



def QuickSort(arr,start,end):

    if start == end:
        return arr

    if start < end:

        piv = partition(arr,start,end)
        #print(piv)

        QuickSort(arr,start,piv-1)
        QuickSort(arr,piv+1,end)


    return arr

random.seed(3)
arr1 =[]
for i in range(50):
    arr1.append(random.randint(1,40))

print(arr1)

print(QuickSort(arr1,0,len(arr1)-1))

# print(QuickSort([1,4,6,5,3],0,4))
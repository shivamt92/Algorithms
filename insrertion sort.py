import random

def InsertionSort(arr):

    for i in range(len(arr)):
        #print('value of i is ',i)
        temp = arr[i]
        k=0

        for j in range(i-1,-1,-1):
            #print(j)

            if temp < arr[j]:
                arr[j+1] =arr[j]
                k = k+1

        arr[i-k] = temp
        #print(arr)

    return arr


random.seed(3)
arr1 =[]
for i in range(10):
    arr1.append(random.randint(1,10))

print(arr1)

print(InsertionSort(arr1))

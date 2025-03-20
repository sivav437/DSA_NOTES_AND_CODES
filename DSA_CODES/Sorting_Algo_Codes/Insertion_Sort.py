# InsertionSort
# take elements and place it in right order.
# [1,2,3,4,5] => [1] => [1,2] and checks 1 < 2 or not. and continues till reaches to end

arr=[5,2,4,1,3]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if(arr[j]<arr[j-1]):
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
            #print(arr,"at if")
print(arr)
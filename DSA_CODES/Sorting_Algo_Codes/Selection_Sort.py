arr=[2,5,8,1,4,3] #unsorted array
length=len(arr)
for i in range(length): # 0 1 2 3 4
        smallest=arr[i] # assume first element is smallest
        idx=i # consider idx is first element of unsorted portion
        for j in range(i,length):# 1 2 3 4
            if(arr[j]<smallest):
                smallest=arr[j]
                idx=j
        temp=arr[i]
        arr[i]=smallest
        arr[idx]=temp

print(arr)
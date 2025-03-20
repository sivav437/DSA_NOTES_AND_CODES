## SELECTION SORT :

>> Aim : Finding smallest or largest element from an unsorted portion and swap element with first element in unsorted portion , repeat it until unsorted portion becomes zero.

>> STEPS :
    step-1: assume given array is an unsorted array , so intially sorted portion is empty and unsorted portion is 0 to length-1.
    step-2: iterate over an unsorted portion and find the smallest / largest element.
    step-3: once smallest or largest element is found , swap it with first element of unsorted portion.
    step-4: repeat this process till the unsorted portion becomes empty.

>> SUDO_CODE :
    eg: [ele1,ele2,ele3,ele4,ele5]
    arr=Array(Elements) #unsorted array
    for(int i=0;i<arr.Length-1;i++){ # 0 1 2 3
        smallest=arr[i];
        idx=i
        for(int j=i+1;j<arr.Length;j++){# 1 2 3 4
            if(arr[j]<smallest){
                smallest=arr[j];
                idx=j
            }
        }
        temp=arr[i]
        arr[i]=smallest
        arr[idx]=temp
    }

>> TIME_COMPLEXITY: B-c => O(N2) , W-C => O(N2) , A-C => O(N2) 
>> SPACE_COMPLEXITY: O(1) { extra memory is for temporary and smallest variable}

>> THEORY: Selection Sort is a comparison-based sorting algorithm.list is divided into two parts, the sorted part at the left end and the unsorted part at the right end.Initially, the sorted part is empty and the unsorted part is the entire list.
The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array. 

>> ADV :
    - Requires only a constant O(1) extra memory space.
    - It requires less number of swaps compared to other standard algo

>> DIS :
    - O(N2) in all cases of T.C.
    - does not maintain the relative order of equal elements

>> Q & A :

    Is Selection Sort a stable sorting algorithm?
    -No, Selection Sort is not stable as it may change the relative order of equal elements.

    Does Selection Sort require extra memory?
    - Selection Sort is an in-place sorting algorithm and requires only O(1) additional space.

    When is it best to use Selection Sort?
    - Selection Sort is best used for small datasets, educational purposes, or when memory usage needs to be minimal.
    
    How does Selection Sort differ from Bubble Sort?
    - Selection Sort selects the minimum element and places it in the correct position with fewer swaps, while Bubble Sort repeatedly swaps adjacent elements to sort the array.
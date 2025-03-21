#m-1 O(n),O(1)

def arraymax_min(arr):
    max_value =arr[0]
    min_value = arr[0]

    for i in range(len(arr)-1):
        if arr[i]>max_value:
            max_value = arr[i]
        
        if(arr[i]<min_value):
            min_value =arr[i]

    print(min_value)
    print(max_value)

#other sortcut

# min = min(arr)
# max= max(arr)


#m-3 using lambda
from functools import reduce

def arraymax_min(arr):
    max_value = reduce(lambda a,b:a if a>b else b,arr)
    min_value  = reduce(lambda a,b :a if a<b else b,arr)


#m-4 using heaphq
def arraymax_min_heap(arr):
    min_value = heapq.nsmallest(1,arr)[0]
    max_value = heapq.nlargest(1,arr)[0]
import heapq



if __name__ =="__main__":
    arr = [2,34,5,6,8]
    arraymax_min(arr)
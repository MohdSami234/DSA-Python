# def kthsmallest(arr,k):
#     arr.sort()
#     return arr[k-1]

# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# print(kthsmallest(arr, k))  # Output: 7



# import heapq

# def kth_smallest(arr, k):
#     return heapq.nsmallest(k, arr)[-1]

# arr = [3,4,5,6,7,7]
# k=3

# # print(kth_smallest(arr, k))



# #o(n)+ klogn
# def kth_small_by_heap(arr,k):
#     heapq.heapify(arr)
#     for _ in range(k-1):
#         heapq.heappop(arr)
    
#     return heapq.heappop(arr)
# # print(kth_small_by_heap([7, 10, 4, 3, 20, 15], 3))  # Output: 7


# #max_heap

# def kth_smallest(arr, k):
#     max_heap =[]

#     for num in arr:

#         heapq.heappush(max_heap,-num)

#         if len(max_heap)>k:
#             heapq.heappop(max_heap)

#     return -heapq.heappop(max_heap)


# # by QuikSort with O(n)

# import random

# def partition(arr,left,right):

#     pivot = arr[right]

#     i=left
#     for j in range(left,right):
#         if arr[j]<=pivot:
#             arr[i],arr[j] =arr[j],arr[i]
#             i+=1

#     arr[i],arr[right]  = arr[right], arr[i]

#     return i


# def quik_select(arr, left,right,k):

#     if left ==right:
#         return arr[left]
       
#     pivot_index = partition(arr, left,right)

#     if pivot_index == k:

#         return arr[pivot_index]
    
#     elif pivot_index>k:

#         return quik_select(arr,left,pivot_index-1,k)
#     else:
#         return quik_select(arr,pivot_index+1,right,k)
# def kth_smallest_new(arr, k):
#     return quik_select(arr, 0, len(arr) - 1, k - 1)

# print(kth_smallest_new([7, 10, 4, 3, 20, 15], 3))  # Output: 7



#quik sort implementation

def partition(arr,low,high):
       pivot = arr[high]
       i  = low

       for j in range(low,high):
           if arr[j]<=pivot:
               arr[i],arr[j] =arr[j],arr[i]
               i+=1

       arr[i],arr[high] = arr[high],arr[i]

       return i

 

# def quick_sort(arr,low,high):
#     if low<high:
#         pivot_index = partition(arr,low,high)
#         quick_sort(arr,low,pivot_index-1)
#         quick_sort(arr,pivot_index+1,high)

             
# arr = [8, 3, 5, 2, 7, 6]
# quick_sort(arr, 0, len(arr) - 1)
# print(arr)  # Output: [2, 3, 5, 6, 7, 8]


#finding Kth Smallest in array


# def quick_sort_for_smallest(arr,low,high,k):
#      if low==high:
#           return arr[low]
#      pivot_index = partition(arr,low,high)
#      if pivot_index==k:
#           return arr[pivot_index]

#      elif pivot_index<=k:
#          return quick_sort_for_smallest(arr,low,pivot_index-1,k)
#      else:
#          return quick_sort_for_smallest(arr,pivot_index+1,high,k)
     
# print('end')
# print(quick_sort_for_smallest([3,5,6,7,8,8,6],0,len([3,5,6,7,8,8,6])-1,2))


def partition_asc(arr,low,high):
       pivot = arr[high]
       i  = low

       for j in range(low,high):
           if arr[j]>=pivot:
               arr[i],arr[j] =arr[j],arr[i]
               i+=1

       arr[i],arr[high] = arr[high],arr[i]

       return i



def quick_sort_for_largest(arr,low,high,k):
     if low>=high:
          return arr[low]
     pivot_index = partition_asc(arr,low,high)
     if pivot_index==k:
          return arr[pivot_index]

     elif pivot_index>k:
         return quick_sort_for_largest(arr,low,pivot_index-1,k)
     else:
         return quick_sort_for_largest(arr,pivot_index+1,high,k)
     
def kth_largest(arr, k):
    return quick_sort_for_largest(arr, 0, len(arr) - 1, k-1 )

# ✅ Test
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_largest(arr, k))  
    



   
def sort012(arr):
    low,mid,high = 0,0,len(arr)-1
    while mid<=high:

        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            # mid+=1
            high-=1


arr = [2, 0, 1, 2, 1, 0, 0, 2, 1]
sort012(arr)
print(arr)  # Output: [0, 0, 0, 1, 1, 1, 2, 2, 2]
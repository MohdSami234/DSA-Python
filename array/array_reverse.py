#question - Reverse An Array-

#m-1, By using another array of same length with time complexity o(n) and o(n)

def reversearraym1(arr):
    n = len(arr)
    temp  = [0]*n
    for i in  range(n):
        temp[i] = arr[n-i-1]

    for i in range(n):
        arr[i] = temp[i]

 

#m-2, By swapping, time complexity o(n)  and o(1)

def reverarrayswap(err):
    n = len(arr)-1
    l=0
    while l<n:
        arr[l],arr[n]=arr[n],arr[l]
        l+=1
        n-=1


#m-3 By Recursion  - O(n) , O(n)

def reversearraybyrec(arr,l,r):
    if l>r:
        return
    arr[l],arr[r] =arr[r],arr[l]

    reversearraybyrec(arr,l+1,r-1)

def reversefinal(arr):
    n = len(arr)-1
    reversearraybyrec(arr,0,n)




if __name__ =="__main__":
    arr=[1,4,5,6,6,2]
   # reversearraym1(arr)
   # reverarrayswap(arr)
    reversefinal(arr)
    for i in range(len(arr)):
        print(arr[i])


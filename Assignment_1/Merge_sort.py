def Merge_sort(arr,front,back):
    if front < back:
        mid = (front+back) // 2
        print(mid)
        Merge_sort(arr,front,mid)
        Merge_sort(arr,mid+1,back)
        merge(arr,front,mid,back)


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()   
        
        
def merge(arr,front,mid,back):
    i = front
    j = mid + 1
    k = 0
    temp = [0,] * (back - front + 1)
    while i <= mid  and j <= back:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j += 1
        k+=1
      
    while(i <= mid) :
        temp[k] = arr[i]
        k += 1; i += 1

    while(j <= back) :
        temp[k] = arr[j]
        k += 1; j += 1

    for i in range (front, back+1) :
        arr[i] = temp[i - front]
            


if __name__ == "__main__":
                
    arr = [10,2,5,44]
    Merge_sort(arr,0,3)
    printList(arr)
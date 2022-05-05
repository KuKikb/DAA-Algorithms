def BS(list,n,l,h):
    if h >= l:

        mid = (h+l) // 2

        if list[mid] == n:
            print(mid)
            return 

        elif list[mid] > n:
            return BS(list,n,l,mid-1)

        elif list[mid] < n:
            return BS(list,n,mid+1,h)

    else:
        print("element not found")
        return 



list = [1,2,3,4,5,6,7,8]
b = int(input("The Element "))

BS(list,b,0,len(list)-1)

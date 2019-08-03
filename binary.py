p =-1
def bsa(lst, n):
    a = 0
    l = len(lst)-1

    while a <= l:
        mid = (a+l)//2
        if lst[mid] == n:
            p = mid
            return True
        
        else:
            if lst[mid] < n:
                a = mid+1
            else:
                l = mid-1
        
    return False
lst = list(map(int, input().split()))
n = int(input())
if bsa(lst, n):
    print("found a", p+1)
else:
    print("na")

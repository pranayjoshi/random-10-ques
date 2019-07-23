a = int(input())
c = a
b= 0
while c > 0:
    r = c%10
    b +=r**3
    c //= 10
if a==b:
    print("yes")
else:
    print("no")

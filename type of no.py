a = int(input())
l = []
l.append("integer")
if a % 2 == 0:
    l.append("even")
else:
    l.append("odd")
if a >= 0:
    l.append("whole number")
else:
    pass
if a > 1:
    for _ in range(2, a):
        if (a & i) == 0:
            break
    else:
        l.append("prime")
else:
    pass
print(l)

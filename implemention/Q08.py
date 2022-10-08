S = input()
sum = 0
L = []
for i in sorted(S):
    if i.isdigit():
        sum += int(i)
    else:
        L.append(i)
if sum != 0:
    L.append(str(sum))
str = "".join(L)

print(str)

S = input()
sorted_S = sorted(S)
sum = 0
index=0
for i in sorted_S:
    if i.isdigit() == True:
        sum += int(i)
        index+=1

print(''.join(sorted_S[index:])+str(sum))
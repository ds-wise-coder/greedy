#문자열 뒤집기
S = input()
result = S[0]
x  = []
count = 0
same = 0
for i in range(1,len(S)):
    if S[0] != S[i]:
        x.append(i)
        print(x)
        
for i in range(0,len(x)-1):
    if x[i]+1 == x[i+1]:
        same += 1
    else:
        count += 1
        if same != 0:
            count +=1
        same = 0
if same != 0:
    count +=1
print(x)
print(count)
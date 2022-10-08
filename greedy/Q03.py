#문자열 뒤집기
#아주 좋은 아이디어 => 0을 1로 바꿀 때와 1 =>0 로 바꿀 때 의 값을 구해서 min을 이용하여 최솟값을 
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

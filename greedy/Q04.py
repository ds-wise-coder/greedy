#만들 수 없는 금액(노답)
N = int(input())
S=list(map(int,input().split()))
S.sort()
x = 1
for i in S:
    if x < i:
        break
    x += i
print(x) 


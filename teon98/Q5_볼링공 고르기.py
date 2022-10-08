N, M = map(int,input().split())
bowling = list(map(int, input().split()))

count = 0
for i in range(1,N+1):
    if bowling.count(i) >= 2:
        a = bowling.count(i)
        count += (a*(a-1))/2

print(((N*(N-1))/2)-count)
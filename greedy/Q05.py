#볼링공 고르기
N,M = (int(), input().split())
x=list(map(int, input().split()))
count = 0

# for i in range(0,len(x)):
#     for j in range(0,len(x)):
#         if x[i] != x[j]:
#             count += 1

# count=count/2 
#i = 1, j=2 / i =2, j = 1 중복으로 계산되기 때문 

for i in range(0,len(x)-1):
    for j in range(1+i,len(x)):
        if x[i]!=x[j]:
            count += 1
print(count)

# 0 # 1234
# 1 #234
# 2 #34
# 3 #4

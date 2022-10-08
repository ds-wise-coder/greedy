#럭키스트레이드 
N = list(input())
mid=(len(N)//2)-1
sum1, sum2 = 0,0
for i in range(0,mid+1):
    sum1 += int(N[i])
    sum2 += int(N[mid+i+1])
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")

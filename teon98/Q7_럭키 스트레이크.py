N = input()

#홀수는 입력으로 들어오지 않는다.
left = 0
right = 0

for i in range(int(len(N)/2)):
    left += int(N[i])
    right += int(N[i+int(len(N)/2)])

if left == right:
    print("LUCKY")
else:
    print("READY")
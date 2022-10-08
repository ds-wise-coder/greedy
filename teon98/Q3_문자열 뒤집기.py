S = input()

action0 = 0 # 모두 0으로 바꾸는 경우
action1 = 0 # 모두 1로 바꾸는 경우

# 첫 번째 원소에 대해 처리
if S[0] == '1':
    action0 += 1
else:
    action1 += 1

# 두 번째 원소부터 검사!
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            action0 += 1
        else:
            action1 += 1

print(min(action0, action1))
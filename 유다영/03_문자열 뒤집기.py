'''
0->1
1->0
뒤집는 최소 횟수?
'''

data = input()

cnt0 = 0
cnt1 = 0

for i in range(len(data)):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1
print(min(cnt0, cnt1))

'''
0001100
'''
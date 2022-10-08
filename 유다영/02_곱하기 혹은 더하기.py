'''
곱하기 혹은 더하기를 넣어 가장 큰 수 만들기
'''

s = input()
# s_list = list(s)

# s_list.sort(reverse=True)
# print(s_list)

ans = 0
for i in s:
    if int(i) <= 1 or ans <= 1: # 값이 1보다 작거나 같거나 가장 큰 수가 1보다 작거나 같다면
        ans += int(i)
    else:
        ans *= int(i)

print(ans)

'''
02984
567
'''

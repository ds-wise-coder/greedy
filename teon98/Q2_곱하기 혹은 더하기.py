"""
아이디어 
주어진 문자열 앞에서부터 +와 x연산을 한후 더 큰 값이 나온걸 통과시킨다.
"""

S_input = input()
#문자를 입력받아 char하나를 int형으로 변환해 리스트에 넣어준다.
S = [int(i) for i in S_input]

result = S[0] #첫 비교대상은 첫번째 인자
for i in range(1,len(S)):
    if(result + S[i] <= result * S[i]):
        result *= S[i]
    else:
        result += S[i]

print(result)
'''
캐릭터 점수: N
럭키 스트레이트 사용 가능인지 아닌지 알려주는 프로그램
'''
num = input()

n = len(num) // 2
a = 0
b = 0
for i in num[:n]:
    a += int(i)
for i in num[n:]:
    b += int(i)
if a == b:
    print("LUCKY")
else:
    print("READEY")

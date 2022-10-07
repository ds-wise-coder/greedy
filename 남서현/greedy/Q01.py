#모험가 길드 문제
N  = int(input(""))
x = input().split()

x.sort()

count = 0
num = 0

for i in x:
    count += 1
    if count >= int(i):
        num +=1
        count = 0

print(num)

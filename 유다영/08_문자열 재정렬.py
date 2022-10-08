s = input()
length = len(s)
s_num = 0
result = ""
ascii_result = []

for i in range(length):
    # 숫자인 경우
    if str.isdigit(s[i]):
        s_num += int(s[i])  # 숫자 합
    # 알파벳인 경우
    else:
        ascii_result.append(ord(s[i]))  # 아스키코드 값으로 변환 후 저장

ascii_result.sort()  # 아스키코드 값 기준 오름차순 정렬

for i in ascii_result:
    result += chr(i)  # 아스크코드 값을 문자로 변경 후 문자열 합치기

if s_num != 0:  # 문자열에 숫자가 하나라도 존재하는 경우
    result += str(s_num)  # 문자열 끝에 숫자 결과값 합치기
print(result)

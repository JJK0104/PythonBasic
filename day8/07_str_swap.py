
'''
* 문자열 형태 변경 메서드

1. lower(): 영문 알파벳을 모두 소문자로 변환
2. upper(): 영문 알파벳을 모두 대문자로 변환
3. swapcase(): 영문 대소문자를 반대로 뒤집음
4. capitalize(): 문장의 시작문자만 대문자로 나머지는 소문자로 변경
5. title(): 단어의 각 첫글자만 대문자로 나머지는 소문자로 변경
'''
s = "GOOD Evening!! my name is HONG!"

print(s.lower()) # good Evening!! my name is hong!
print(s.upper()) # GOOD EVENING!! MY NAME IS HONG!
print(s.swapcase()) # good eVENING!! MY NAME IS hong!
print(s.capitalize()) # Good evening!! my name is hong!
print(s.title()) # Good Evening!! My Name Is Hong!

print("-" * 40)

answer = input("사과의 영문 철자를 쓰세요: ")

if answer.upper() == "APPLE":
    print("정답!!")
else:
    print("오답!!")








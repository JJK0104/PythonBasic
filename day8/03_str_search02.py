'''
in, startswith(), endswith(), isalpha(), islower(), isupper(), isdecimal() 
int에는 isdecimal() 못 쓴다. 문자열에 쓰는 거다.
'''









'''
- 특정 문자가 있는 인덱스 번호는 관심이 없고 단순히 포함여부만 확인하고
  싶다면 in 키워드를 사용합니다.

- in 키워드는 문자열 내부에 찾는 단어가 포함되어 있다면 True를
  포함되어 있지 않다면 False를 반환합니다.
'''
s = "python programming"

print("a" in s) #True
print("q" in s) #False
print("pro" in s) #True
print("z" not in s) #True

'''
- startswith() 메서드는 문자열이 특정 단어,문자열로 시작하는지의 여부를
  검사하여 True, False를 반환합니다.

- endswith() 메서드는 반대로 특정 단어,문자열로 끝나는지의 여부를 검사합니다.
'''
name = "홍길동"

if name.startswith("고"):
    print("성이 고씨입니다.")
else:
    print("성이 고씨가 아닙니다.")

if name.startswith("홍길"):
    print("성이 홍길씨입니다.")
else:
    print("성이 홍길씨가 아닙니다.")

file = "야옹이.png"

if file.endswith("jpg"):
    print("확장자명이 jpg입니다.")
else:
    print("확장자명이 jpg가 아닙니다.")


'''
- 사용자에게 데이터를 입력받을 때 입력값의
  형태를 검사할 수 있습니다.

1. isalpha() - 모든 문자가 알파벳형태인지를 조사하여 True, False를 반환합니다.
2. islower() - 모든 문자가 소문자인지를 조사하여 True, False를 반환합니다.
3. isupper() - 모든 문자가 대문자인지를 조사하여 True, False를 반환합니다.
4. isdecimal() - 모든 '문자'가 숫자인지를 조사하여 True, False를 반환합니다.
                 int에는 isdecimal() 못 쓴다. 문자열에 쓰는 거다.

'''
print("-" * 40)

while True:
    point = input("점수: ") #  point = int(input("점수: ")) 라고 쓰면 '90점'이라고 입력하면 오류 발생
    
    if point.isdecimal():
        print(type(point)) # <class 'str'>
        point = int(point)
        print(type(point)) # <class 'int'>
        print("당신의 점수는", point, "점입니다.")
        break
    else:
        print("점수는 숫자로만 입력하세요!")


#내가 한번 만들어 본거 
print("-" * 40)

while True:
    point = input("점수(숫자 또는 숫자점으로 입력해주세요): ")
    
    if point.isdecimal():
        point = int(point)
        print(type(point))
        print("당신의 점수는", point, "점입니다.")
        break
    elif not point.isdecimal(): # elif point.endswith('점')
        point = point[:-1]
        
        point = int(point)
        print(type(point))
        print("당신의 점수는",point,"점입니다")
        break
    else: 
      print("점수는 숫자 또는 숫자점으로 입력해주세요")




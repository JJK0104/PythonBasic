
'''
* 파이썬의 블록구조 표현

- 파이썬은 타 언어와 달리 문장의 종속구조를 나타낼 때
  블록({})을 사용하지 않습니다.
- 그 대신 들여쓰기를 통해 블록구조를 표현합니다.
- if문 뿐만 아니라 코드의 종속구조를 나타내는 모든 곳에서
  들여쓰기를 사용합니다.
'''
point = int(input("점수: "))

if point >= 60:
    print("60점 이상의 점수를 획득했습니다.")
    print("시험에 합격했습니다.")

if point < 60:
    print("60점 미만의 점수를 획득했습니다.")
    print("시험에 불합격했습니다.")

# 들여쓰기를 안할 경우 if의 종속문으로 보지 않음.
print("수고하셨습니다!")
#    print("메롱")





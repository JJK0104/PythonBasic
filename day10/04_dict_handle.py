
'''
* 사전 내부 데이터 관리

- 사전은 변경 가능한 자료형이어서 실행 중에 데이터의 삽입, 삭제, 수정 등의
  편집을 자유롭게 할 수 있습니다.

- key 수정은 못하고 value 수정만 가능

- 존재하지 않는 key를 사용하여 데이터를 대입시키면 append 개념이 됩니다.

- del() , clear(), keys(), values()
'''
eng_kor = {'student':'학생', 'girl':'소녀', 'book':'책'}
print(eng_kor) # {'student':'학생', 'girl':'소녀', 'book':'책'}

# 사전에 데이터 추가하기
# 사전은 위치의 개념이 필요없다, 찾는데 우리가 번호 찾는 게 아니니까, 특정 키로 찾으니까
# 그래서 중간 삽입기능은 없다
# 존재하지 않는 key를 사용하여 데이터를 대입시키면 append 개념이 됩니다.

# 없는 key를 R value로 사용하면 에러가 난다
# 근데 L value로 사용하고 값을 저장하면 append 개념
eng_kor['boy'] = '소년' # append
print(eng_kor) # {'student':'학생', 'girl':'소녀', 'book':'책', 'boy':'소년'}

# 사전에 데이터 수정하기
# 존재하는 key를 사용하여 데이터를 대입하면 수정의 개념이 됩니다.
eng_kor['book'] = "서적" # update
print(eng_kor) # {'student':'학생', 'girl':'소녀', 'book':'서적', 'boy':'소년'}

# 사전 데이터 삭제하기
del(eng_kor['student']) #대괄호 안에 들어가는 건 key. Key를 통해 삭제하면 key,value 다 삭제된다
print(eng_kor) # # {'girl':'소녀', 'book':'책', 'boy':'소년'}

# 전체 삭제 
eng_kor.clear() 
print(eng_kor) # {}
'''
- 사전의 key목록과 value목록만 따로 추출하고 싶다면
  keys()메서드와 values()메서드를 사용합니다.

- 위 메서드들은 각각의 목록을 고정형 리스트형태, 편집 불가능한 리스트 형태로 반환합니다.
'''
print("-" * 40)
eng_kor = {'student':'학생', 'girl':'소녀', 'book':'책'}
print(eng_kor.keys()) # dict_keys(['student', 'girl', 'book'])
print(eng_kor.values()) # dict_values(['학생', '소녀', '책'])

# for ~ in 뒤에 사전을 적으면 key만 반복 순회합니다.
print("-" * 40)
for k in eng_kor:
    print(k, ":", eng_kor[k])

# 빈 사전 만들기
d = {}
print(d) # {}

d = dict()
print(d) # {}

print("-" * 40)

eng_kor = {}

print("[영어 단어장 만들기]")
print("- 종료하시려면 영단어에 0을 입력하세요.")

while True:
    eng = input("영단어: ")
    if eng == '0': 
        print("종료합니다.")
        break
    kor = input("뜻: ")
    
    if eng not in eng_kor:
        eng_kor[eng] = kor
    else:
        print("이미 등록한 단어입니다.")
        
    print("\n *** 단어장 ***")
    print("-" * 40)
    for k in eng_kor:
        print(k, ":", eng_kor[k])
    print("-" * 40)






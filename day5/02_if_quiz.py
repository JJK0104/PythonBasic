


'''
* 퀴즈
1. 놀이기구에 키가 140cm이상이고, 
  나이가 8세 이상인 사람만 탑승한다고 가정합니다.
2. 먼저 키(height)와 나이(age)를 입력받으세요.
3. 조건문 if~else를 사용하여 2개의 조건이 모두 
    참일 경우  "놀이기구에 탑승할 수 있습니다."
    를 출력하세요.
4. 위 조건이 거짓일 경우 
  "놀이기구에 탑승할 수 없습니다."를 출력하세요.  
5. 조건식과는 별개로 "오늘 하루 즐거운 시간되세요!"
   를 출력하세요.    
'''


height = int(input("키: "))
age = int(input("나이: "))

if (height >= 140) and (age >= 8):
    print("놀이기구에 탑승할 수 있습니다.")
else :
    print("놀이기구에 탑승할 수 없습니다.")     
print("오늘 하루 즐거운 시간 되세요!")



'''
C언어에서 연산자 우선순위
1순위) () , [] , -> , . (왼쪽부터 차례대로 우선순위 높다... ()가 1짱)
2순위) 연산자 항의 개수가 적을수록 먼저 실행 ex) !1||0 여기서 !은 단항연산자, ||은 2항연산자
따라서 단항연산자 먼저 실행돼서 !1||0 => 0||0 => 0
3순위) 산술 > 관계 > 논리 > 대입
'''
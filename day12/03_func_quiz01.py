'''
리스트나 튜플을 우측에 배치하면 순서대로 담아준다. 개수 다르면 오류

내장함수 map()
'''

# 2개의 숫자 중 최대값을 판별하여 반환하는 함수를 정의
def max_of_two(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

'''
* 문자열 분할 메서드 split()

- split메서드는 구분자를 기준으로 문자열을 분할하여 리스트[]에
 저장한 뒤 반환합니다.
- 구분자를 지정할 때는 문자열로 지정해야 합니다.
'''


n = input("정수들을 입력하세요 : ").split() # 15 16 17으로 입력하면 공백을 기준으로 분할하여 n = ['15','16','17']
print(type(n)) # <class 'list'>
print(n) # ['15', '16', '17']

li = [1,2,3]
n1 = li[0]
n2 = li[1]
n3 = li[2]
print(n1,n2,n3) # 1 2 3

n1,n2,n3 = li # 리스트나 튜플을 우측에 배치하면 순서대로 담아준다. 개수 다르면 오류
print(n1,n2,n3) # 1 2 3 


'''
* 내장함수 map()
- map은 첫번째 인수로 타입을 적어주고, 두번째 인수로 문자열을
  리스트를 적으면 해당 리스트 내부에 값을 일괄적으로 첫번째 인수의
  타입으로 변환한 map구조의 데이터를 리턴합니다.
''' 
n1 , n2 = input("정수 2개를 입력하세요 : ").split() # 이때 정수 2개는 공백을 기준으로 분리해서 써야됨
# 만약 좌변에 변수가 한개 있었으면 그건 리스트가 된다. 위 예제 n = input("정수들을 입력하세요 : ").split() 처럼
# 리스트나 튜플을 우측에 배치하면 순서대로 담아준다. 개수 다르면 오류
# day 12-5 예제도 보기
print(type(n1)) #str
print(type(n2)) #str
print(n1,n2) # 5 4


n1, n2 = map(int, input('정수 2개를 입력하세요 : ').split()) # 정수를 g h로 입력하면 오류
                                                            # int 적어야 하는듯, 소수 적어도 오류뜸
print(type(n1)) #int
print(type(n2)) #int
print(n1,n2) # 5 4


# map 함수 쓰려면 좌측에 변수 개수 맞춰서 써야겠네...
n =  map(int, input('정수 2개를 입력하세요 : ').split())
print(type(n)) # <class 'map'>
print(n) # <map object at 0x00000226012BD070>

'''
1. 3개의 정수를 입력받으세요
2. 3개의 정수 중 가장 큰값을 반환하는 
    함수 max_of_three를 정의하세요.
3. 3개의 정수 중 가장 작은값을 반환하는 
    함수 min_of_three를 정의하세요.
4. 반환값을 통해 출력하세요.
출력예시: "n1, n2, n3중 최대값: ??"
'''   
def max_of_three(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    else:
        if n2 > n3:
            return n2
        else:             
            return n3
        
        
        
def min_of_three(n1, n2, n3):
    if n1 < n2:
        if n1 < n3:
            return n1
        else:
            return n3
    else:
        if n2 < n3:
            return n2
        else: 
            return n3


   
     
n1, n2, n3 = map(int, input('정수 3개를 입력하세요: ').split())

print('%d, %d, %d 중 최대값: %d' 
      % (n1, n2, n3, max_of_three(n1, n2, n3)))
print('%d, %d, %d 중 최대값: %d' 
      % (n1, n2, n3, min_of_three(n1, n2, n3)))






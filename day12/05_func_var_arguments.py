
def add(li):
    sum = 0
    for n in li:
        sum += n
    return sum

print(add([10, 20, 30])) # 60



'''
* 위치 가변 인수

- 함수를 호출할 때는 함수 정의시에 지정한 인수의 개수만큼
  값을 전달해줘야 합니다. 

- 하지만 위치 가변인수를 사용하면 하나의 인수로 여러 개의
  데이터를 받아서 처리할 수 있습니다.

- 위치 가변인수는 함수 정의부에서 인수를 선언할 때 인수 앞에
 * 기호를 붙여 선언하며 이런 경우에 여러 개의 데이터를 튜플로
  묶어서 함수 내부로 전달합니다.
'''
def add(*nums):
    sum = 0
    for n in nums: # nums를 내부에서 사용할 때는 * 안 붙이고 사용
        sum += n
    return sum

print(add(1,2,7,15,10,20)) # 55

print("-" * 40)
'''
def calc_points(*points, name):
    print('%s 학생의 성적 계산...' % name)
    sum = 0
    for n in points:
        sum += n
    return sum

result = calc_points(66, 77, 89, 90, '이순신')
print('총점:', result)

#이렇게 하면 name 왜 안 주냐고 오류뜬다
'''

def calc_points(name, *points):
    print('%s 학생의 성적 계산...' % name)
    sum = 0
    for n in points:
        sum += n
    return sum

result = calc_points('이순신', 66, 77, 89, 90) # 이순신 학생의 성적 계산...

print('총점:', result) # 총점: 322

'''
- 위치 가변인수는 콤마 이후의 인수를 모두 다 튜플로 묶어서 처리하기
  때문에 일반 인수와 함께 사용할 때는 항상 마지막에 위치해야 합니다.

- 그 이유는 가변 인수뒤에 일반인수가 있으면 전체를 모두 튜플로
  묶어서 처리하기 때문입니다.

- 마찬가지로 하나의 함수에서 가변인수를 2개 이상 선언할 수 없습니다.
ex) def function(*abc, *def)  (X)
'''
def function(tu1, tu2):
    print(tu1)
    print(tu2)

print("-" * 40)
t1 = (1,2,3)
t2 = (4,5,6,7,8,9,10)
function(t1, t2) # (1,2,3)
                 # (4,5,6,7,8,9,10)


'''
연습1 - n개의 정수를 전달받아 평균값을 구하여 
      리턴하는 함수를 작성하세요. (get_avg)
'''
# 가변인수 안 쓰는 case
print("-" * 40)
def get_avg(nums): 
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)
'''
#방법1
n_list = []

while True:
    n = int(input('정수(종료시 0입력): '))
    if n == 0: break
    n_list.append(n)
'''

'''
day 12-3)

* 내장함수 map()
- map은 첫번째 인수로 타입을 적어주고, 두번째 인수로 문자열을
  리스트를 적으면 해당 리스트 내부에 값을 일괄적으로 첫번째 인수의
  타입으로 변환한 map구조의 데이터를 리턴합니다.
''' 
n_map = map(int, input('정수: ').split())
print(n_map) # <map object at 0x000001C8B3265AF0> -> at 뒤의 문자,숫자는 실행할때마다 달라짐... C언어 주소 같은건가?
# n_list = list(n_map)

# day 12-3 에서는 n1, n2 = map(int,input("정수 2개 입력 : ").split())으로 하면 n1, n2에 정수 각각 int 형태로 들어갔음
# 여기는 list형태로 만드네 
n_list = list(map(int, input('정수들을 띄어쓰기로 구분하여 입력 : ').split())) 
print(n_list) # [ 14, 15, 16, 17]
print('평균: %.2f점' % get_avg(n_list))


'''
연습2 - n개의 정수를 전달받아 가장 큰 숫자를 찾아 
      리턴하는 함수를 작성하세요. (get_max)
'''
def get_max(*nums):
    max = nums[0] # - 위치 가변인수는 함수 정의부에서 인수를 선언할 때 인수 앞에
                  # * 기호를 붙여 선언하며 이런 경우에 여러 개의 데이터를 튜플로
                  # 묶어서 함수 내부로 전달합니다.
                  # 따라서 인덱싱 가능.
    print(type(nums))
    print(nums)
    for n in nums:
        if n > max:
            max = n
    return max  
'''

nmap = map(int,input("정수들 입력 : ").split())
print(nmap) 
n_list = list(nmap)
print(n_list)
a = get_max(n_list)
print(a)

이러면 지금 get_max의 인수로 n_list, 즉, 리스트 '1'개를 넣었다
그럼 max = 리스트 그 자체가 된다
'''
print('\n')
max_num = get_max(1,2,3,4,5,6,8,7) # <class 'tuple'>
                                   # (1,2,3,4,5,6,8,7)
print('\n')
print(max_num)

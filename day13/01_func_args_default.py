'''
* 인수의 기본값

- 파이썬에서는 인수의 기본값을 설정하여 자주 바뀌지 않는 데이터는
  기본값을 통해 처리할 수 있게 합니다.
'''
def calc_stepsum(begin, end, step=1):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print(calc_stepsum(1, 10, 2)) # step에는 원래 1이 저장돼 있는데 값을 적어주면 2로 변경되다
print(calc_stepsum(1, 10)) # step에 아무것도 안 적으면 미리 저장해 놓은 1사용

'''
- 인수의 기본값을 지정할 때는 항상 '맨 뒷부분'에 
  기본값이 지정된 인수들을 '모아서 나열'해야 합니다.

ex) def calc_sum(begin, end=5, step)  (X)
    def calc_sum(begin, end=5, step=1) (O)
'''
def calc_sum(begin, end=5, step=1):
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print(calc_sum(1, 5)) # 위치 인수(positional args), 얘네는 위치를 찾아간다. 
                      # 그래서 1은 begin으로 가고 5는 end로, 
                      # step은 이미 저장된 1 사용
print(calc_sum(3)) # 12 -> 왜냐면 3 + 4 + 5
print(calc_sum(1, 11, 3)) # 22 -> 왜냐면 1 + 4 + 7 + 10








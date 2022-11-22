
'''
* docstring

- 함수의 재활용성을 높이려면 함수의 사용법(인수의 의미, 사용시 
  주의사항 등)을 문서로 남기는 것이 좋습니다.

- docstring은 함수를 사용하는 사람들을 위한 설명서 역할을 하며
  주석과 마찬가지로 코드 실행에는 영향을 주지 않습니다.

- 작성된 docstring을 열람하는 함수는 내장함수 help()입니다.
'''

# help(print)
# help(len)
# help([].append)
# help([].insert)
# help({}.keys)

def calc_sum(begin, end):
    
    #함수의 정의부 바로 아래에다 멀티스트링 기호를 주고 주석처럼 작성하면 된다
    
    
    """
    # calc_sum 설명서!!
    * 1. 이 함수는 특정 범위의 누적합계를 계산합니다.
    * 2. begin값에 시작값을 넣어주세요!
    * 3. end값에 끝값을 넣어주세요!
    * 4. 결과값으로 범위의 누적합을 반환합니다. 
    """
    sum = 0
    for n in range(begin, end+1):
        sum += n
    return sum

help(calc_sum)







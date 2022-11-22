

'''
* 리스트 관리 함수, 메서드

- 리스트는 문자열과는 달리 내부 요소데이터의 자유로운 편집이 가능합니다.


* 리스트에 데이터를 추가하는 메서드
1. append(추가하고 싶은 요소): 요소를 리스트의 맨 마지막에 추가.
2. insert(들어갈 자리(index), 들어갈 값): 요소를 리스트의 특정 위치에 삽입.
3. list2.extend(list1): 리스트에 또 다른 리스트를 병합.
                        list2 뒤에 list1 요소를 추가시켜 
                        list2 영구적으로 변화
'''
a = [1,2,3]
print([1,2,3].append(2)) # None
b=[1,2,3].append(2)
print(b) # None
c=a.append(2)  # 여기서 a에 2 한번 추가
print(c) # None
print(a) # [1 ,2, 3, 2]
print(a.append(2)) # None ,  여기서 a에 2 한번 추가
print(a) # [1, 2, 3, 2, 2]
a.append(2) # 여기서 a에 2 한번 추가
print(a) # [1, 2, 3, 2, 2, 2]


print("-"*40)
nums = [1, 3, 5, 7]
print(nums)

# nums[4] = 9 이러면 에러뜬다
nums.append(9)
print(nums)

nums.append("안녕")
print(nums)

# insert(index, value) : index는 들어갈 자리, value는 들어갈 값
nums.insert(2, 4)
print(nums)

nums.insert(100,2) # 이러면 그냥 마지막에 2 추가되네
print(nums)

nums.insert(4, "메롱")
print(nums)


name = "홍길동"
nums.append(name)
print(nums)

print("-" * 40)

nums = [2,4,6,8]
print(nums)

'''
# nums의 2번인덱스에 새로운 리스트 [9,10,11]을 저장!
nums[2] = [9, 10, 11]
print(nums) #[2,[9,10,11],6,8] 로 된다
'''

# nums의 2번인덱스 이상 3번인덱스 미만 영역에 들어있는 = 2번 인덱스
# 값을 '삭제하고' 요소 9, 10, 11을 추가한다. => [2,4,6,8] 에서 [2,4,9,10,11,8]이 된다
nums[2:3] = [9, 10, 11] #그냥 nums[2] = [9,10,11] 라고 하면 [9,10,11] 리스트가 통째로 요소로 들어간다
print(nums)

nums[1:5] = [15]
print(nums) # [2, 15, 8]

# 2번 인덱스 영역에 요소 99, 100, '안녕'을 삽입.
nums[2:2] = [99, 100, '안녕']
print(nums)


list1 = [5,4,3,2,1]
list2 = [9,8,7,6]
print(list2 + list1)

print(list2)
print(list1)
'''
- 리스트의 + 연산은 원본 리스트는 변화하지 않고 연산이 완료된
  새로운 리스트를 생성합니다.
- extend는 기존의 리스트에 새로운 리스트를 병합시켜 원본의
  구조를 변경시킵니다.
'''
list2.extend(list1) #list2에다 list1을 병합하세요
print(list2)






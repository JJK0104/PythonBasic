
'''
* 리스트 내부 요소 삭제
* 따로 내장함수라고 말 안 하는 건 메서드 

1. remove(): 삭제할 값을 직접 지정하여 삭제합니다. 몇번 인덱스에 있든 간에 삭제
             2개 이상이면 가장 앞에 거만 삭제

2. 내장함수 del(): 삭제할 요소의 인덱스 번호를 통해 삭제합니다.

3. 리스트 슬라이싱을 통해 빈 리스트 대입.

4. clear(): 리스트 내부 요소 전체 삭제.
'''
points = [88, 99, 56, 92, 78, 100, 44, 52]
print(points) # [88, 99, 56, 92, 78, 100, 44, 52]

points[0:3]=[0,1] # 0,1,2 번째 인덱스가 0, 1로 변한다. 즉 2번째 인덱스는 삭제됨->[0, 1, 92, 78, 100, 44, 52]
print(points)

points.remove(92) #만약 92가 2개 이상이면 가장 앞에 거만 삭제 
print(points)

del(points[0])
print(points)

del points[2] #괄호 안 써도 된다
print(points)

points[1:4] = [] #1번 이상 4번 미만의 값을 삭제하고 []의 요소를 추가해라. 
print(points)


#전체 삭제 방법1
points.clear()
print(points)

nums = [1,2,3,4,5]
print(nums)

'''
이렇게 하면 마지막 요소는 남는다
nums[0:4]=[]
print(nums)
'''


#전체 삭제 방법2
nums[:] = [] #전체를 다 삭제하고 []의 요소를 추가해라 = 전체 삭제 
print(nums)




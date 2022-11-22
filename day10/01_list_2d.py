

'''
* 2차원 리스트 - 리스트 내부 요소가 또 다시 리스트인 형태
'''
li = [ [1,2,3], [4,5,6], [7,8,9] ]

print(type(li)) # <class 'list'>
print(len(li)) # 3
print(li[1]) # [4,5,6]
print(type(li[1])) # <class 'list'>
print(li[2][0]) # 7
print(type(li[2][0])) # <class 'int'>

# 2차원 리스트를 반복문 처리하여 모든 요소를 사용하려면
# 반복문도 2중루프로 구성해야 합니다.
print("-" * 40)

for ele in li:
    for n in ele:
        print(n, end=" ")
    print()

'''
[1,2,3] : 1, 2, 3
[4,5,6] : 4, 5, 6
[7,8,9] : 7, 8, 9
for p in li:
    print(p,end=' : ')
    for q in p:
        print(q,end=', ')
    print('\b\b ')
'''

# 2차원 리스트로 학생들의 성적 처리하기
# (한 학급 학생 4명의 4과목 점수 처리하기)

students = [
        [88, 76, 92, 98],
        [65, 70, 58, 99],
        [83, 80, 88, 100],
        [100, 99, 100, 99]
    ]

print("-" * 40)
stu_num = 1 # 학생들의 출석번호를 저장할 변수
total_avgsum = 0.0 # 학생들의 평균의 총합을 저장할 변수
kor_sum = 0 # 우리 반 국어점수의 총합을 저장할 변수

for student in students:
    
    each_sum = 0 # 1명의 총점을 저장할 변수
    for score in student:
        each_sum += score # 1명의 4과목 총점을 누적
    each_avg = each_sum / len(student) #과목 수로 나눠 평균 구하기
    print("%d번 학생: 총점- %d점, 평균- %.2f점"
          % (stu_num, each_sum, each_avg))
    stu_num += 1
    
    total_avgsum += each_avg
    
    kor_sum += student[0]

total_avg = total_avgsum / len(students)
print("-" * 40)
print("학급 전체 평균: %.2f점" % total_avg)
print("국어점수 평균: %.2f점" % (kor_sum / len(students)))

print("-" * 40)


#3차원 리스트
list_3d = [
        [ [1,2], [3,4], [5,6] ],
        [ [7,8], [9,10], [11,12] ],
        [ [13,14], [15,16], [17,18] ]    
    ]

print(list_3d[1][2][0])






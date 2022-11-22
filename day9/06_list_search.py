

'''
* 리스트 탐색

- 리스트 탐색 메서드는 문자열과 거의 유사합니다.
- index(), count(), in 키워드 등을 지원합니다.
- max(), min()
'''
points = [99, 14, 87, 100, 55, 100, 87, 99, 100, 22]

perfect = points.count(100) #100이 몇개 있냐
print("만점자의 수는 %d명입니다." % perfect)

idx = points.index(87)
print("87이 저장된 위치는 %d번입니다." % idx) # 2개 이상이면 가장 앞에 거 알려줌

# 내장함수 len(), max(), min()
print("학생수는 %d명입니다." % len(points))
print("최고점수는 %d점입니다." % max(points))
print("최저점수는 %d점입니다." % min(points))

print("-" * 40)

# 리스트 내의 요소의 유무를 검사하려면 in 키워드를 사용합니다.
li = ["안녕", "헬로", "니하오"]

print("헬로" in li) #True
print("곤니치와" in li) #False
print("메롱" not in li) #True

ok_sign = ["ok", "yes", "응", "그래", "ㅇㅇ", "ㅇㅋ"]
answer = input("밥 먹을러 갈래?? ")

if answer in ok_sign:
    print("좋아!! 치킨먹으러 가자!")
else:
    print("ㅇㅋ 수고링~")







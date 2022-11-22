

'''
* 중첩 if문

- 중첩 if문은 if블록 내부에 새로운 if문이 있는 형태입니다.
- 바깥쪽 if문의 조건을 검사한 후 True가 나올 경우 다시 내부의
  if문을 검사하는 형태로 조건판단을 합니다.
'''
height = float(input("키: "))

if height >= 140:
    age = int(input("나이: "))
    if age >= 8:
        print("놀이기구를 탈 수 있습니다.")
    else:
        print("나이가 8세미만입니다.")
        print("놀이기구를 탈 수 없습니다.")        
else:
    print("키가 140cm 미만입니다.")
    print("놀이기구를 탈 수 없습니다.")









# 구구단 8단 출력하기
# 1. 구구단 8단을 for문을 사용하여 출력하세요.
# 2. 구구단 단수를 입력받아 입력받은 단수의 
# 구구단이 출력되게 하세요.
dan = int(input("구구단 단수: "))

print("구구단", dan, "단")
print("=" * 40)

for hang in range(1, 10): 
    print(dan,"x",hang,"=",dan * hang)
    
    
    
for dan in range(2,10):
    for hang in range(1,10):
        print(dan,"X",hang,"=",dan*hang)
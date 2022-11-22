

'''
때로는 에러 발생 여부와 관계없이 항상 실행해야 될 코드가 있다

* finally

- finally는 예외 발생 여부와 관계없이 항상 실행해야 할 코드를
  작성하는 예외처리의 키워드입니다.
'''
pets = ['거북이', '타란튤라', '전갈']

for i in range(4):
    try:
        print(pets[i], "키울래용!")
    except:
        print("애완동물의 정보가 없습니다.")
    finally: # 예외처리 여부와 관계없이 항상 실행됨
        print("\n\n애완동물 넘 조아~~")

print("프로그램 정상 종료!")







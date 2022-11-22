

'''
 사용자의 입력을 파일(xxx.txt)에 저장하는 프로그램을 작성하시오. 
(단, 프로그램을 다시 실행하더라도 파일명이 동일하다면
  기존 작성한 내용을 유지하고 
새로 입력한 내용이 추가되어야 한다. 또한 파일명도 입력받아 저장)

다음은 실행 예제이다.
출력 예시: "저장할 내용을 입력: "

실행 할 때마다 사용자가 입력한 내용이 xxx.txt파일에 추가되어야 한다.
'''
f_name = input("파일명을 입력: ")
user_input = input("저장할 내용을 입력: ")
f_path = "c:/py1530/%s.txt" % f_name # 파이썬에서는 파일경로 / 으로 써도 된다

try:
    f = open(f_path, "a")  # 내용을 추가하기 위해서 'a'를 사용
    f.write(user_input + "\n") # 입력된 내용을 줄단위로 구분하기 위해 줄바꿈 문자 삽입
    print("파일 저장 성공!")
except:
    pass
finally:
    f.close()



'''
* 문자열 대체 메서드

- replace(): 특정 단어를 '모두' 찾아 새로운 단어로 일괄 대체합니다.
  print(s2.replace("커피", "우유", 2)) #3번쨰 값을 주지 않으면 일괄대체, 3번쨰 값을 주면 앞에서부터 해당개수만 바꿈
'''

# 문자열 내부에 \: line continue. 이때 \ 뒤에 공백이나 다른 거 있으면 안된다.
s = "파이썬 프로그래밍!! 파이썬은 문자열을 다루는 수많은 함수들을 \
제공합니다."
print(s)
print()
s2 = '''파이썬 프로그래밍!! 파이썬은 문자열을 다루는 수많은 함수들을 
제공합니다.'''
print(s2) # 위에처럼 하면 '제공합니다'가 다른 줄로 나온다.
print()

print(s.replace("파이썬", "python")) #주의 : 문자열 s 자체는 안 변했다.
print(s.replace( "파이썬",  "")) #일괄 삭제
print(s)
print()
s = s.replace("파이썬",'python') # 이러면 s가 영구저긍로 변함
print(s)
print()
s2 = "아침부터 '커피'를 마셨는데 점심먹고도 또 커피를 마셨어 \
그런데 저녁에 또 커피를 마시라고?"

print(s2.replace("커피", "우유", 2))#3번쨰 값을 주지 않으면 일괄대체, 3번쨰 값을 주면 앞에서부터 해당개수만 바꿈
print(s2.replace("커피", "우유", 1))

print()
print("="*40)
while_sen = '''n=1
while n<2 :
    if n = 1 :
        print(hello)
    n = n + 1'''
print(while_sen) 
print("제어변수 n을 s로 바꾸면")
print()
print(while_sen.replace("n","s"))






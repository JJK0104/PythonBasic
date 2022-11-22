

'''
* 표준 모듈 codecs

- 웹이나 다른 프로그램의 텍스트 데이터와 파이썬 내부의 텍스트 데이터의
  인코딩 방식이 다를 경우 내장함수 open()은 제대로 인코딩을 할 수 없어
  예외가 발생합니다.
- 이런 인코딩 문제를 해결할 때 사용하는 모듈이 codecs입니다.
'''
import codecs

file_path = "C:/py1530/codec_test.txt"

# codecs 모듈에서 제공하는 open 사용
f = codecs.open(file_path, mode="w", encoding="utf-8")
# open과 차이점이 있다면 모듈을 지정할 때 위치인수로 지정하는 게 아니라 키워드 인수로 mode="w"
# 세번째 인수로 인코딩은 한글인코딩 "utf-8"
# 인코딩을 해석을 utf-8로 해주세요

# codecs.open write 할때 줄바꿈할때 \n만 쓰면 안되고 
# 사실 enter 키는 \r\n 같이 들어감
f.write("안녕안녕~~\r\n")
f.write("잘가잘가~~\r\n")
f.write("메롱메롱~~\r\n")

f.close()
print("파일 저장 완료!")







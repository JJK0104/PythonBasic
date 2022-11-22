

'''
* 파일 읽기 기능 (read)

- 파일에서 데이터를 읽어올 때는 분량에 따라 적당한 메서드를
  사용합니다.

1. read(): 파일 전체 데이터를 한번에 읽어서 리턴.
2. readline(): 파일 데이터를 한줄씩 읽어서 리턴.
3. readlines(): 파일 전체를 읽어 한줄씩 분리하여
  리스트에 담아서 리턴.
'''
file_path = "C:/py1530/ringdingdong.txt"

# read는 파일경로 파일이 반드시 미리 존재해야 한다
# write, append 같은 경우 파일경로에 파일이 없으면 생성한다. 상위 폴더만 미리 존재하면 된다

try:
    f = open(file_path, "r")
    text = f.read() # f.write는 변수에 대입 안 한다
                    # f.read()는 반환값이 있어서 변수에 대입
    print(text)
except:
    pass
finally:
    f.close()


'''
- read() 메서드는 파일을 한번에 읽을 수 있어 편리하지만
  파일 용량이 크면 메모리 소모가 심해지는 단점이 있습니다.

- 따라서 큰 파일을 읽을 때는 read()의 인수로 읽을 양을 지정하여
  조금씩 반복해서 읽어들이는 것이 좋습니다.
'''
print("-" * 40)

try:
    f = open(file_path, "r")
    while True:
        text = f.read(10) # 10개씩 잘라서 읽는다. 우리 눈에 보이지 않는 \n도 한글자로 읽는다
                          # 링딩동 링딩동 링디 = 10글자
                          # 기링디기 링딩동~~ = 10글자
                          # /n링딩동 링딩동 링 = 10글자
        if len(text) == 0: break
        print(text, end="") # print 자체에도 \n 이 있으니까 
                            # 만약 10개씩 어떻게 쪼개지는지 보고 싶으면 end="" 지우고 실행시켜봐

    print()
except:
    pass
finally:
    f.close()
    
'''
- readline()은 데이터를 자동으로 \n을 기준으로 한 줄씩 
  읽어들이기 때문에 텍스트를 줄 단위로 관리하기 좋습니다.

  \n까지 포함해서 한줄이다 
  ex) 링딩동 링딩동 링디기링디기 링딩동~~\n -> 이게 한줄
'''   
print("-" * 40)

try:
    f = open(file_path, "r")
    while True:
        text = f.readline()
        if not text: break # not text 는 len(text) == 0 이랑 같다
                           # not 0 = True
        print(text, end='') # print 자체에도 \n 이 있으니까 
    print()
except:
    pass
finally:
    f.close()


'''
- readlines()는 파일 데이터를 한줄씩 문자열로 만들어
  리스트 형태로 리턴하기 때문에 데이터를 리스트의 인덱싱이나
  for문을 통해 관리하기 좋습니다.
'''
print("-" * 40)

try:
    f = open(file_path, "r")
    rows = f.readlines() # rows의 타입은 list, 5줄이니까 요소가 5개다
#    print(rows) # '링딩동 링딩동 링디기링디기 링딩동~~\n' 이게 첫번째 요소
    for r in rows:
        print(r, end="")
    
except:
    pass
finally:
    f.close()







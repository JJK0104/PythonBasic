

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


try:
    f = open(file_path, "r")
    while True:
        text = f.read(10)
        if len(text) == 0: break
        print(text, end="")
    print()
except:
    pass
finally:
    f.close()
    

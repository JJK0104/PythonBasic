



'''
* points.txt 파일의 숫자값을 모두 읽어 
  총합과 평균값을 구한 후 
  총점, 평균값을 result.txt라는 파일에 
  쓰는 프로그램을 작성해 보세요.
'''
try:
    f = open("C:/py1530/points.txt", "r")
    numlist = f.readlines()
    f.close()
    
    sum = 0
    for num in numlist:
        # num의 type은 str
        score = int(num)
        sum += score
    avg = sum / len(numlist)
    
    f = open("C:/py1530/result.txt", "w")
    data = "총점: %d, 평균: %.2f" % (sum, avg)
    f.write(data)
    print("파일 저장이 완료되었습니다.")
except:
    pass
finally:
    f.close()
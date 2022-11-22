'''
1. 실수형태로 입력받은 키(cm)와 몸무게(kg)을 
   인수로 전달받아 
2. bmi지수를 계산하여 반환함과 동시에 
3. bmi가 25.0이상이면 "당신은 과체중입니다." 
   18.5이하면 "당신은 저체중입니다." 
   나머지는 "당신은 정상체중입니다."를 출력하는 
   Calc_BMI라는 함수를 정의하고 호출하세요. 
# bmi 계산식 : 몸무게(kg) / (키(m) * 키(m)) 
# 출력 예시: 
"키 -> 178.4cm, 체중-> 78.2kg의 체질량지수는: 24.57입니다"
'''
def Calc_BMI(cm, kg):    
    m = float(cm) / 100
    kg = float(kg)
    
    bmi = kg / (m * m)
    
    if bmi >= 25.0:
        print("당신은 과체중입니다.")
    elif bmi <= 18.5:
        print("당신은 저체중입니다.")
    else:
        print("당신은 정상체중입니다.")    
    return bmi


height = input("신장(cm): ")
weight = input("체중(kg): ")

bmi = Calc_BMI(height, weight)
print("키 -> %scm, 체중-> %skg의 체질량지수는: %.2f입니다." 
      % (height, weight, bmi))










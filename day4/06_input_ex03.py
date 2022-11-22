

'''
- 처음부터 입력한 값을 정수나 실수형태로 사용할 것으로 판단된다면
  입력받을 때부터 정수나 실수형태로 입력받을 수 있습니다.
'''
price = int(input("가격: ")) #순수한 정수가 아닐 경우 오류. 5000'원'이라 쓰면 안된다
sale_rate = float(input("할인율: "))

print("price의 타입:", type(price))
print("sale_rate의 타입:", type(sale_rate))








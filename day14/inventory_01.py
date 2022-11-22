


# 제품 1개당 필요한 정보
# [제품번호, 제품명, 단가, 수량, 제품총액]
# 이런 비정형적 데이터는 리스트보다 사전이 편리하다 

# 사전 -> day 10-3 ,10-4

inventory = []

for x in range(2): # 0,1 -> 2번 반복
    product = {}
    
    print("# 제품 등록을 시작합니다.")
    product['제품번호'] = input("제품번호: ")
    product['제품명'] = input("제품명: ")
    product['단가'] = int(input("단가: "))
    product['수량'] = int(input("수량: "))
    product['제품총액'] = product['단가'] * product['수량']
    
    inventory.append(product)
    print("\n제품 등록이 정상적으로 처리되었습니다.")
    

print("\n           *** 창고 재고 정보 ***")
print("=============================================")
print("제품번호        제품명         수량          단가         제품총액")
print("=============================================")
'''
#방법 1
for product in inventory: # [{'제품번호':14, '제품명':'냉장고','수량':4,'단가':5}, {'제품번호':4, '제품명':'TV','수량':4,'단가':5}]
    print("%4s      %4s       %4d     %7d %10d" % 
          (product['제품번호'], product['제품명'],
           product['수량'], product['단가'], 
           product['제품총액']))
'''

# inventory =[{'제품번호':1234, '제품명':'냉장고','수량':44,'단가':55},{}]
for idx in range(len(inventory)):  # len(inventory) == 2   
    print("%4s      %4s       %4d     %7d %10d" % 
          (inventory[idx]['제품번호'], 
           inventory[idx]['제품명'],
           inventory[idx]['수량'], 
           inventory[idx]['단가'], 
           inventory[idx]['제품총액']))


print("=============================================")









'''
# 실수값을 입력하면 다시 정수값을 입력하라는 문구가 뜨게 하는 코드
while True : 
    num_str = input("정수 값을 입력하세요 : ")


'''




# print("5 + 12 =",17,"\n")

n=1
while n <=9 : 
    print("구구단 {}단".format(n))
    print("="*40)
    s=1
    while s <= 9 : 
        print("{}X{}={}".format(n,s,n*s))
        
        s = s + 1

    n = n + 1

'''
    *
   **
  ***
 ****
*****
'''


'''
0 : 0 0 0 0 
1 : 1 2 3 4
2 : 2 4 6 8
3 : 3 6 9 12
4 : 4 8 12 16
'''
'''
# 방법 2 : 0 0+0 0+0+0 0+0+0+0 으로 해석한 경우
print("방법 2 : 0 0+0 0+0+0 0+0+0+0 으로 해석한 경우")
for x in range(0,5):    
    print(x,":",end = " ")
    for y in range(1,5):
        print(y)
    print()
0
0+0
0+0+0
0+0+0+0

n = 4
print(n, end = " ")
print(n+n, end = " ")
print(n+n+n, end = " ")
print(n+n+n+n, end = " ")

for x in range(0,5):
    a = 0
    for y in range(1,5):
        a = a + x
        print(a,end=" ")
'''

'''
abcde
FGHIJ
klmno
PQRST
uvwxy
z
'''
print()
print()
a=0
b=4
print("%d위 : " %(a+b) +"asdf" )
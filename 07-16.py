print("hello world")

# 문제.1 (반복문 복습)

#구구단 3단을 출력하라. 출력할 때, 3 * 3 = 9와 같이 어떤 값을 곱하였는지도 함께 출력하여라.

for a in range(1, 100):
    print("3 *", a,"=" ,3 * a) #"문자열" 주의, 3은 고정값이니 문자열로

#교수님 풀이
for index in range(1, 10):
    print("3 x", index,"=" , 3 * index)


# 문제.2
#for 반복문을 두 번 사용해서 2차원 리스트의 요소를 모두 출력하시오.
# - num_list = [(10, 50), (20, 40),(30, 60)(40,70)]
num_list = [(10, 50), (20, 40),(30, 60), (40,70)]
for i in num_list:
    for j in i:
        print(j)


# 문제.3
# 다음 이중 리스트의 평균값을 아래 출력 결과와 같이 각각 구하여라.
# - my_list = [[100,200],[400,800],[1000,1400]]
# 출력결과
# 150
# 600
# 1200

my_list = [[100, 200], [400, 800], [1000, 1400]]
for a in my_list:
    b = (a[0] + a[1]) / 2
    print(b)

my_list = [[100, 200], [400, 800], [1000, 1400]]
for a in my_list:
    for j in a:
        print(j)



#교수님 풀이
my_list = [[100,200],[400,800],[1000,1400]]
for i in my_list:
        print("반복이 몇번 되는가?")
        for j in i :
            print(j)


my_list = [[10, 20], [30, 40], [50, 60], [70, 80]]
for i in my_list:
    var = 0
    for j in i:
        var = var + j
    print(var / len(i))



# 문제4. '10번 찍어 안 넘어가는 나무 없다' 속담을 while 문을 사용하여 구현하시오. 아래처럼 출력되도록

# 나무를 1번 찍었습니다.
# 나무를 2번 찍었습니다.
# 나무를 3번 찍었습니다.
# 나무를 4번 찍었습니다.
# 나무를 5번 찍었습니다.
# 나무를 6번 찍었습니다.
# 나무를 7번 찍었습니다.
# 나무를 8번 찍었습니다.
# 나무를 9번 찍었습니다.
# 나무를 10번 찍었습니다.
# 나무가 넘어갑니다!

count = 0
while count < 10:
    count += 1 # 자기 자신에 계속 +1 을 한다는것
    print("나무를", str(count) + "번 찍었습니다.")

else :
    print("나무가 넘어갑니다!")
#(함수)
# 문제5. 네 개의 덧셈 함수, 곱셈 함수코드를 작성하시오.
def numbers(a, b, c, d):
    result = a + b + c + d
    return result
sum_result = numbers(a, b, c, d)
print("합계:", sum_result)

def numbers(a, b, c, d):
    result = a * b * c * d
    return result


#교수님 풀이
#덧셈
def add_vars(num1, num2, num3, num4):
    result = num1 + num2 + num3 + num4
    return result
result_add = add_vars(num1:3, num2:4, num3:5, num4:8)
print(result_add)

#곱셈
def mul_vars(num1, num2, num3, num4) :
    result = num1 * num2 * num3 * num4
    return result
result_mul = mul_vars(num1:3, num2:4, num3:5, num4:8)
print(result_add)


# 문제6. 별 피라미드 찍기. 출력 결과가 아래와 같이 나오도록, 코드를 작성하시오.
# *
# **
# ***
# ****
# *****


for i in range(1, 11):
    print("*" * i)
 #1부터 10까지 출력되는 값

#  #문제7. 1부터 100까지 수를 2의 배수, 3의 배수, 5의 배수로 분류하려고 한다.
# 2의 배수는 numbers_1의 리스트에,
# 5의 배수는 numbers_2의 리스트에,
# 7의 배수는 numbers_3의 리스트에 저장하는 코드를 작성하시오.

numbers_1 = []  # 2의 배수를 저장할 리스트
numbers_2 = []  # 5의 배수를 저장할 리스트
numbers_3 = []  # 7의 배수를 저장할 리스트

for num in range(1, 101):

    if num % 2 == 0:
        numbers_1.append(num)
    if num % 5 == 0:
        numbers_2.append(num)
    if num % 7 == 0:
        numbers_3.append(num)

print("2의 배수:", numbers_1)
print("5의 배수:", numbers_2)
print("7의 배수:", numbers_3)

# #문제8. while 문을 사용하여 1부터 45사이의 중복이 없는 랜덤한 수 6개를 생성하고, 이를 result 리스트 변수에 추가하는 코드를 작성하라.
# - 랜덤한 수 생성방법
# - import random
# - random.randunt(1,45)
# -if A in B
#    print("A에 값이 있습니다.")

import random
result = []
i = 0
while i < 6:
    i = i + 1
    new_num = random.randit(a:1, b: 45)
    if new_num in result :
        print("값이 기존에 있습니다. 새롭게 추가하지 않습니다.")
    else:
   print(result)
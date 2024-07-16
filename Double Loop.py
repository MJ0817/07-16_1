# 이중 반복문(Double loop)
# - 하나의 반복문 안에 또 다른 반복문을 중첩하여 사용하는 방식
# for 변수1 in 범위1:
#     for 변수2 in 범위2:
for i in range(1, 10):
    for k in range(11, 20):
        print(1, k)


m = [1, 2, 3], [4, 5, 6], [7 ,8 ,9]
for i in m:
    for k in i:
        print(i)

#디버깅(Debugging)
# - 버그를 찾아내고 해결하는 과정






#함수 - 프로그램에서 재사용 가는한 코드 블록
string = "매개변수를 입력하면, 입력한 매개변수가 화면에 출력됩니다."
print(string)
len(string)

def print_list(var):
    print(var)

var = [1,2,3,4,5]
sum(var)

# print 변수할당 불가, 값을 출력만,

var = [1,2 ,3, 4, 5]
b = sum(var)
print(b)

def 안녕하세요():
    print("안녕하세요. 만나서 반갑습니다.")
    안녕하세요()
    안녕하세요()
    안녕하세요()
    안녕하세요()
# 괄호안에 저 문자를 집어넣는 함수

def add_numbers (number_1, number_2): #첫번째 들어오는 수를 남바원 두번째를 넘버투로 한다.
    result = number_1 + number_2
    print(result)
    return result


c = add numbers(number_1:3, numbers_2:5)
d = add_numbers(number_1:50, numbers_2:30)

#두 수를 더하는 함수
def add_numbers(a, b):
    result = a + b
    return result

#함수 호출 및 반환값 사용
sum_result = add_numbers(5, 3)
print("합계", sum_result)

# 문제5. 네 개의 덧셈 함수, 곱셈 함수코드를 작성하시오.
def numbers(a, b, c, d):
    result = a + b + c + d
    return result

def numbers(a, b, c, d):
    return a * b * c * d
PI = 3.14

def number_input():
    output = input("숫자 입력 : ")
    return float(output)

def get_circumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

# print("모듈의 __name__을 출력하기")
# print(__name__)
# print()

if __name__ == "__main__":
# test_module 모듈 활용 가이드
    print("get_circumference(10) : ", get_circumference(10))
    print("get_circle_area(10)", get_circle_area(10))
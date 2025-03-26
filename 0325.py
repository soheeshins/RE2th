# 데이터 타입 (Data Type)
# 1. 숫자

# 정수 (integer) - 소수점이 없는 숫자
from sys import getsizeof
a = 10


# 실수 (float) - 소수점이 있는 숫자
b = 3.14

# 복소수 (Complex) = 실수부와 허수부로 구성된 숫자
c = 3 + 4j

print(a, type(a))
print(b, type(b))
print(c, type(c))

# 문자열 (string)
name = "에단"
print(name, type(name))

#  3. 불리언(Boolean)
참 = True
거짓 = False

print(참, type(참))
print(거짓, type(거짓))

# 비교 연산의 결과로 불리언 값을 얻을 수 있습니다.
print('bool', 10 > 5, type(10 > 5))
print('bool', 10 == 5, type(10 == 5))
print('bool', 10 <= 5, type(10 <= 5))

# None 타입
# 아직 값이 할당되지 않았음을 표시
result = None
print(result)

# str = '문자열입니다.'
# print(getsizeof(1))
# print(getsizeof("문자열"))
# print(getsizeof(str))

# num = input("숫자를 입력하세요 :")
# print(num, type(num))
# a = int(num) / 2
# print(a)
# num = input("숫자를 입력하세요 :")
# print(num, type(num))
# a = float(num) / 2
# print(a)


# 비교연산자

x = 5
y = 10

age = 15
print(x < age < y)  # age가 x보다 크고 y보다 작다

# 논리 연산자
p = True
q = False

print(p and q)  # False 논리곱 둘다 True여야 True
print(p or q)  # True 논리합(OR) 하나라도 True면 True
print(not q)  # False 논리부정 True -> False False-> True

a = 10
b = 20
c = 30

print((a < b) and (b > c))  # False
print((a < c) or (b > c))  # True

# 할당 연산자

x = 10

x += 10
print(x)  # 20
x -= 15
print(x)  # 5
x *= 3
print(x)  # 15

# 멤버십 연산자

fruits = ["사과", "바나나", "체리"]

print("사과" in fruits)  # True
print("수박" in fruits)  # False

name = "안녕 \n 하세요"
print(name)

print("안녕\n하세요")
print("안녕\t하세요")
print("안녕\\하세요")
print("안녕\'하세요")
print("안녕\"하세요")


print("올해는 %d년 %s의 해이다" % (2024, "용띠"))

year = "올해는 %d년 %s의 해이다" % (2024, "용띠")
print(year)

number = "저는 올해 %d살 입니다." % 20
print(number)

clac = "10나눈기 3는  %.3f입니다." % 3.33333  # 소수점 3자리까지 나타냄
print(clac)

text = "저는 %5s에서 살고 있습니다." % "은평구"  # 최소의 기준 안쓴 만큼 공백으로 채워짐
print(text)


country = "대한민국"
city = "서울"
people = "한국인"

text = "저는 올해 {0}살 입니다." .format(20)
print(text)
text = "저는 {0}사람이며 {1}에 살고있습니다." .format(country, city)
print(text)
text = "제가 사는 {0}은 {country}에 있습니다" .format(city, country="한국")
print(text)

text = "나는 {1}이다.{{ 그리고 }} {0}에 산다" .format(city, people)
print(text)
text = "{}점수: {}점, {}점수: {}점" .format("영어", 100, "수학", 90)


text = "[{0:<10}]".format("hey")
print(text)  # hey+7개의 공백 10자리


print("|\_/|")
print("|q p|\t/}")
print("( 0 )\"\"\"\\")
print("|\"^\"\t|")
print("|_/=\\\\__|")

a = "{0:=^7}".format("신소희")
print(a)

text = "문자열 실습입니다. {{중괄호}}를 출력해보세요".format()
print(text)


출력 = "{{{0:^9}}}".format("중괄호")
text = f'문자열 실습입니다. {출력}를 출력해보세요'
print(text)

# 실습
print("|\_/|\n|q p|")
print('( 0 )"""\\')
print('|"^"     |')
print('||_/=\\\\__|')


# 실습2
name = "소희"
text = f'{name:=^10}'
print(text)

print(f"문자열 실습입니다. {{ 중괄호 }}를 출력해보세요.")

# 문자열 인덱싱
print()
print("문자열 인덱싱")
print()
a = "Hello, Python"

print("a[7]", a[7])

print(a[0:4])
print(a[7:])
print("a[7:]", a[7:])


date = "20240930"
print(date[:4] + "년" + date[4:6] + "월" + date[6:] + "일")

print(len(date))
print(date.count('2'))

print(date.find('4'))
print(date.index('9'))

# replace 첫번변경하고자 하는 문자, 두번째는 변경할 문자, 갯수
print(date.replace('0', '1'))
print(date.replace('0', '1', 1))

# split
print(date.split('0'))

text = "Hello, Python"
print(text.upper())  # 대문자로
print(text.lower())  # 소문자로

text = "            Hello   World           "
print("[" + text.strip() + "]")  # 공백삭제
print("[" + text.lstrip() + "]")  # 왼쪽 공백삭제
print("[" + text.rstrip() + "]")  # 오른쪽 공백삭제

# 숫자 판별
print("123".isdigit())  # 맞으면True 아니면 False
print("123aaa".isdigit())

# 문자, 공백 판별
print("hello".isalpha())
print("hello123".isalnum())
print('\n\t'.isspace())

text = "Hello"
print(text.upper().isupper)  # 문자를 대문자로 바꾼 후 전체가 대문자가 맞는지 isupper로 검산


# # 1번
# name = input("이름을 입력하세요.")
# age = input("나이를 입력하세요.")
# print("안녕하세요!", name, "님(", age, "세)")

# # 2번
# name = input("이름을 입력하세요.")
# year = int(input("태어난 년도를 입력하세요."))  # 정수로
# yearr = int(input("올해 년도를 입력하세요."))
# print("올해는", yearr, "년,", "홍길동님의 나이는", yearr-year+1, "세 입니다")

print(f"안녕하세요")


str1, str2 = input().strip().split(' ')
print(str1.strip())
print(str2.strip())

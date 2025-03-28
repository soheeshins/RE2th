#조건문

# if 조건식:
#     조건식이 참이라면 실행

# if True:
#     print("참 입니다") # if True 일때 실행
# else:
#     print('거짓입니다') # if False 일때 실행

# if False:
#     print("참 입니다") # 실행 안됌

# age = 15

# if age >= 20:
#     print('15살 이상입니다.') # 조건문이 참이면 조건문 실행
# else:
#     print('미성년자 입니다.') # 조건문이 거짓이면 조건문 실행

# print(f'나이는 {age} 입니다') # 들여쓰기를 안했기 때문에 if와 상관없이 출력

#  0은 거짓, 문자열은 빈문자열, 리스트, 딕셔너리, 튜플 셋의 값이 비어있는 경우
# if []:
#     print("리스트 비어있습니다")

# if 0:
#     print("숫자가 0 입니다")

# #1
# pw = input("비밀번호를 입력하세요 : ")

# if pw == "abc123":
#     print("비밀번호가 맞습니다")
# else:
#     print("비밀번호가 틀렸습니다.")

# #2
# num = int(input("숫자를 입력하세요: "))

# if num % 2 == 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")

# 조건문 예제
# age = int(input("입력해주세요."))

# if age >= 40:
#     print('40대 입니다.') # 조건문이 참이면 조건문 실행
# elif age >= 30:
#     print('30대 입니다.')
# elif age >= 20:
#     print('20대 입니다.')
# else:
#     print('미성년자 입니다.') # 조건문이 거짓이면 조건문 실행

# print(f'나이는 {age} 입니다') # 들여쓰기를 안했기 때문에 if와 상관없이 출력

# # 실습. elif
# score = int(input("점수를 입력하세요: "))

# if score >= 90:
#     print("학점 : A")
# elif score >= 80:
#     print("학점 : B")
# elif score >= 70:
#     print("학점 : C")
# elif score >= 60:
#     print("학점 : D")
# else:
#     print("학점 : F")
#   

#실습 다시 해보기!!
# age = int(input("나이를 숫자로 입력해주세요: "))
# pay_method = input("결제방법을 입력해주세요 (현금 또는 카드): ")

# if age <8 and age >= 75:
#     print("요금은 무료입니다.")
# elif age < 14:
#     print("450원")
# elif age < 20:
#     if pay_method == "현금"
    
# print (f'{age}의 {pay_method} 요금은 {price} 입니다. ')


# # 중첩 조건문 실습
# age = int(input("나이를 숫자로 입력하세요: "))
# pay = input("결제 방식을 입력(현금또는카드): ")

# if age < 8:
#     print(age, "세의", pay, "요금은 무료입니다.")
# elif age < 14:
#     print(age,"세의",pay,"요금은 450원입니다.")
# elif age < 20:
#     if pay == "현금":
#         print(age, "세의", pay, "요금은 720원입니다.")
#     elif pay == "카드":
#         print(age, "세의", pay, "요금은 1000원입니다.")

# elif age < 75:
#     if pay == "카드":
#         print(age, "세의", pay, "요금은 1200원입니다.")
#     elif pay == "현금":
#         print(age, "세의", pay, "요금은 1300원입니다.")
# else:
#     print(age,"세의", pay, "요금은 무료입니다.")


#삼향연산자
# age= int(input("나이를 입력하세요: "))

# message = " 성인 입니다" if age >=20 else "미성년자입니다"
# print(message)

# if age > 20:
#     pass

# else:
#     print(message)

# fruit = input("과일을 한글로 입력하세요: ")
# if fruit in ['사과', '바나나', '복숭아']:
#     print("이 과일은 포함되어 있습니다.")
# else:
#     print("존재하지 않은 과일입니다.")

# 실습

# fruit = {
#     "apple": 95,
#     "banana": 105,
#     "cherry": 50
# }

# fruit_name = input("과일을 영문으로 입력하세요. :")

# if fruit_name in fruit:
#     print(f"{fruit_name}의 칼로리는 {fruit[fruit_name]} Kcal 입니다.")
# else:
#     print("이 과일은 포함되지 않습니다.")

# GPT
#     # 과일 칼로리 딕셔너리 생성
# fruits = {
#     "apple": 95,
#     "banana": 105,
#     "cherry": 50
# }

# # 사용자 입력 받기
# fruit_name = input("과일 이름을 입력하세요: ")

# # 딕셔너리에서 검색 후 출력
# if fruit_name in fruits:
#     print(f"{fruit_name}의 칼로리는 {fruits[fruit_name]} kcal 입니다.")
# else:
#     print("해당 과일은 목록에 포함되지 않았습니다.")

# 반복문
# while 조건이 참이면 반복, 조건이 거짓이면 조건문 종료

# i = 0

# while i < 10:
#     print(i)
#     i += 1
# print("종료")

# i = 1 
# total = 0
# while i <= 10:
#     total += i
#     i += 1

# print(f'1부터 10까지의 합은 {total}입니다')

# #초기화
# user_input = ""
# while user_input !="종료":
#     user_input = input("종료하려면 '종료'를 입력하세요: ")
#     print(f'입력한 값: {user_input} 입니다.')

# while문 사용하기 실습 - GPT
# while True:
#     num = input("양수를 입력하세요 ('종료' 입력 시 프로그램 종료)): ")

#     if num.lower() == '종료':
#         print("프로그램을 종료합니다.")
#         break 

#     if not num.isdigit():
#         print("양수만 입력하세요.")
#         continue 

#     n = int(num)

#     if n == 0:
#         pass
#         continue  

#     total = sum(range(1, n + 1))  
#     print(f"1부터 {n}까지의 합은 {total}입니다.")


# while True:
#     num = input("숫자를 입력하세요. ('종료' 입력시 프로그램이 종료)) : ")

#     if num == "종료":
#         print ("프로그램을 종료합니다.")
#         break
    
    
#     if not num.isdigit():
#         print("양수만 입력하세요")
#         continue

#     n = int(num)

#     if n < 0:
#         print("양수만 입력하세요")
#         continue
    
#     if n == 0:
#         pass
#         continue

#     total = sum(range(1, n+1))
#     print(f"1부터 {n}까지의 합은 {total}입니다.") #공부해라.

# # for 문
# for i in range(1, 10):
#     print(i)

# fruits = ['사과','바나나', '체리']

# for fruit in fruits:
#     print(fruit, end= ' ')

# numbers = [1,2,3,4,5,6,7]
# total = 0 
# for num in numbers:
#     total += num

# print(f'합계는 {total} 입니다.')

# for i in range(1,12,2):
#     if i > 5 :
#         print(i, end=' ')

# print()

# dict1 = {'name' : '홍길동', 'age' : 25, 'city' : '서울','hobby': ['캠핑', '영화보기']}
# for key in dict1:
#     print(key, end= ' ')

# for value in dict1.values():
#     print(value, end = ' ') 

# for key in dict1.keys():
#     print(f'{key} : {dict1[key]}', end = ' ')

# for key,value in dict1.items():
#     print(f'')

# print()

# 구구단 만들기
# num = int(input("몇단을 출력할까요? :"))

# for j in range(1, 10):
#     print(f'{num} x {j} = {num * j}')

# 정수 합 계산

# a = int(input("어디까지 계산할까요? :" ))
# total = 0 

# for i in range(1, a + 1) :
#     if i % 2 != 0:
#         total += i

# print(f"1부터 {a} 까지의 홀수의 합 :{total}")

#평균값 구하기 1

# students = {
#     "학생1" : {"국어": 83 , "영어": 92 , "수학": 88},
#     "학생2" : {"국어": 90 , "영어": 79 , "수학": 86},
#     "학생3" : {"국어": 88 , "영어": 86 , "수학": 94}
# }

# total_a = 0
# total_b = 0
# total_c = 0

# for student in students.values():
#     total_a += student["국어"]  
#     total_b += student["영어"]  
#     total_c += student["수학"]  

# num_students = len(students)

# average_a = total_a / num_students
# average_b = total_b / num_students
# average_c = total_c / num_students

# print(f"국어 평균 : {average_a}")
# print(f"영어 평균 : {average_b}")
# print(f"수학 평균 : {average_c}")

#평균값 구하기 2

# students = {
#     "학생1": {"국어": 83, "영어": 92, "수학": 88},
#     "학생2": {"국어": 90, "영어": 79, "수학": 86},
#     "학생3": {"국어": 88, "영어": 86, "수학": 94}
# }

# totals = {"국어": 0, "영어": 0, "수학": 0}

# for student in students.values():
#     for subject, score in student.items():
#         totals[subject] += score

# for subject, total in totals.items():
#     print(f"{subject} 평균 : {total / 3:}")

#평균값 구하기 3

# students = {
#     "학생1": {"국어": 83, "영어": 92, "수학": 88},
#     "학생2": {"국어": 90, "영어": 79, "수학": 86},
#     "학생3": {"국어": 88, "영어": 86, "수학": 94}
# }

# for key, value in students.items():
#     total = sum(value.values())
#     avg_score = total / len(value)
#     print(f'{key}의 평균은 점수 : {avg_score:.2f}') #소수점 두번째자리까지

# for i in range(1,3):
#     for j in range(4,7):
#         print(f'{i},{j}')

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in matrix:
#     for element in row:
#         print(element)


# for i in range(0,3):
#     for j in range(0,3):
#         print(matrix[i][j])

# for row in matrix:
#     for element in row:
#         total += element

#  print('total : ', total)
        

# for i in range(0,3):
#     for j in range(0,3):
#         print(matrix[i][j])

#실습

# for n in range(2,10): #2단부터 9단까지
#     print(f"[{n} 단]") # 각 단을 출력
#     for i in range(1,10): # 1부터 9까지 반복
#         print(f"{n} x {i} = {n * i}") #구구단 계산 결과 출력

# print() # 공백을 출력으로 각 단 끝난 후 한줄 띄우기

print()
print()
print()

vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
print(f'남은 음료수: {vending_machine}')

user_type = input('사용자 종류를 입력하세요\n1.소비자\n2.주인\n:')



if user_type not in ['소비자','주인']:
    print("잘못된 값.")
else:
    if user_type == "소비자":
        bev = input("마시고 싶은 음료? : ")
        if bev in vending_machine:
            print(f'{bev} 드릴게요.')
            vending_machine.remove(bev)
            vending_machine.sort()
            print(f'남은 음료수: {vending_machine}')
            
        else:
            print("없음")
    elif user_type == "주인":
        cho = input("할 일 선택\n1.추가\n2.삭제\n:")
        if cho == "추가":
            print(f'남은 음료수: {vending_machine}')
            bev_add = input("추가할 음료수: ")
            vending_machine.append(bev_add)
            vending_machine.sort() #같은 값끼리 연결 = 정렬
            print("추가 완료")
            print(f"남은 음료수: [{', '.join(vending_machine)}]")
        elif cho == "삭제":
            print(f'남은 음료수: {vending_machine}')
            bev_remove = input("삭제할 음료수: ")
        
            if bev_remove in vending_machine:
                vending_machine.remove(bev_remove)
                vending_machine.sort()
                print('삭제 완료.')
                print(f'남은 음료수: [{', '.join(vending_machine)}]')
                
            else:
                print(f"{bev_remove}는 지금 없네요")
        else:
            print("잘못된 값입니다.")

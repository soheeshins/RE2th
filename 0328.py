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



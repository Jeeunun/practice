# r = int(input("구의 반지름을 입력해주세요: "))
# print("구의 부피는 {}입니다.".format((str((4/3*3.141592)*r*r*r))))
# print("구의 겉넓이는 {}입니다.".format((str((4*3.141592)*r**25))))

# import math
# a = float(input("밑변의 길이를 입력해주세요: "))
# b = float(input("높이의 길이를 입력해주세요: "))
# c = str(math.sqrt(pow(a,2)+pow(b,2)))
# print("빗변의 길이는 {}입니다.".format(c))

# numInput = int(input("정수를 입력해주세요: "))
# for a in range(2,6):
#     if numInput % a != 0:
#         print("{}은 {}로 나누어 떨어지는 숫자가 아닙니다.".format(str(numInput),str(a)))
#     else :
#         print("{}은 {}로 나누어 떨어지는 숫자입니다.".format(str(numInput),str(a)))

# 
# import datetime
# now = datetime.datetime.now()
# while True:
#     numInput = input("입력 : ")
#     if "안녕" in numInput:
#         print("안녕하세요.")
#     elif "몇 시" in numInput :
#         print(f"지금은 {now.hour} 시 입니다.")
#     else :
#         print(numInput)

# <Q 다시 풀기 !!>
# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[],[],[]]
# for number in numbers:
#     output[].append(number)
# print(output)


# numbers = [1,2,3,4,5,6,7,8,9]
# for i in range(0,len(numbers)//2):
#     j = 1+(2*i)
#     print(f"i ={i},j={j}")
#     numbers[j] = numbers[j]**2
# print(numbers)

# p237
# # 내가 푼 것
# for a in range(1,10):
#     print('*'*a)
# # 교재 정답
# output = ""
# for i in range(1,10):
#     for j in range(0,i):
#         output +="*"
#     output += "\n"
# print(output)

# # p238 (공백.?)
# for a in range(1,15):
#     for b in range(a+1):
#         output = a + b
#         result = output*'*'
#     print(result)

# print("안녕\t")
# print("하세요")

# 리스트 

# while


# import time
# number = 0
# target_kick = time.time() + 5
# while time.time() < target_kick:
#     number += 1
# print("5초동안 {}번 반복했습니다.".format(number))

# 
# key_list = ["name","hp","mp","level"]
# value_list = ["기사",200,30,5]
# character = {}
# for a in range(0,len(key_list)):
#     character[key_list[a]] = value_list[a]
# print(character)


    
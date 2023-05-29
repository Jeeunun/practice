# lista = [100,20,30,5,90]
# print(max(lista))
# print(min(lista))

# lista = [100,20,30,5,90]
# lista.sort()
# # print(lista[-1])
# # print(lista[0])
# # lista = [100,20,30,5,90]
# # lista.sort(reverse = True)
# # print(lista[0])
# # print(lista[-1])

# # a=10
# # if a > 5 :
# #     print("참 입니다.")
# # elif a > 100 :
# #     print("참 입니다.")
# # else :
# #     print("거짓 입니다.")

# # a = 10
# # if a > 5 :
# #     print("참 입니다.")
# # if a > 100 :
# #     print("참 입니다.")
# # else :
# #     print("거짓 입니다.")

# # lista=[1,2,3,4,5,6,7,8,9,10]
# # num = int(input("숫자를 입력하세요: "))
# # if num in lista:
# #     print("값이 있습니다.")
# # else:
# #     print("값이 없습니다.")

# # lista=[1,2,3,4,5,6,7,8,9,10]
# # num = int(input("숫자를 입력하세요: "))
# # if num not in lista:
# #     print("값이 없습니다.")    #다시 입력하세요 출력후, num 다시 입력
# # else:
# #     print("값이 있습니다.")     #만약 값이 있으면 반복문 종료

# # numinput = float(input("짐의 무게를 입력하세요: "))
# # money = 10000*(numinput//10)
# # if numinput >=10:
# #     print("짐의 무게는 %f이고, 수수료는 %d 입니다." %(numinput,money))
# #     print(f"짐의 무게는 {numinput}이고 수수료는 {money}입니다.")

# # 홀수인 값에 2를 곱한 값만을 list로 만들어라
# # lista = []
# # for a in range(1,11):
# #     if a %2 != 0 :
# #         lista.append(a*2)
# # print(lista)

# # # for문을 이용해서 list 만들기
# # lista = []
# # for a in range(1,11):
# #     if a not in lista:
# #         lista.append(a)    
# # print(lista)

# # a=1
# # while a<1001:
# #     print(str(a)+'번째 반복')
# #     a+=1

# # a=1
# # lista=[]
# # while a<1001:
# #     lista.append(a)
# #     a+=1
# # print(sum(lista))
# # print(sum(lista)/len(lista))

# listsize = int(input("리스트의 크기를 입력하세요: "))
# a = 1
# lista=[]
# while a<listsize:
#     listvalue = input("리스트의 값을 입력하세요: ")
#     lista.append(listvalue)
#     a+=1
# print(lista)
# print(len(lista))

# station1 = "사당"
# station2 = "신도림"
# station3 = "인천공항"
# print (station1, "행 열차가 들어오고 있습니다.")
# print (station2, "행 열차가 들어오고 있습니다.")
# print (station3, "행 열차가 들어오고 있습니다.")
# print (station1 + "행 열차가 들어오고 있습니다.")
# print (station2 + "행 열차가 들어오고 있습니다.")
# print (station3 + "행 열차가 들어오고 있습니다.")
# print (f"{station1} 행 열차가 들어오고 있습니다")
# print (f"{station2} 행 열차가 들어오고 있습니다")
# print (f"{station3} 행 열차가 들어오고 있습니다")

# from random import *
# random()
# random.randint(x,y) -x이상 y이하
# random() * x - 0이상 x미만
# int((ranom() * x)) + 1 - 1이상 x+1미만
# randomrange(x,y) - x이상 y이하

# print(random()) #0.0~1.0 미만의 임의의 값 생성
# print(random()*10) #0.0~10.0미만의 임의의 값 생성
# print(int(random()*10)) #0~10미만의 임의의 값 생성
# print((int(random()*10)) + 1) #0~10이하의 임의의 값 생성
# print((int(random()*45)) + 1)#1~45이하의 임의의 값 생성
# print(random.randint(1,45)) #1~45이하
# print(randomrange(1,46)) #1~45까지의 임의의 값 생성
# print(random(1,45)) #1~45까지의 임의의 값 생성

import random
print(random.randint(1,45)) #print((int(random()*45) + 1)
lista=[]
listasize=1
while listasize < 7:
    randNum = random.randint(1,45)
    lista.append(randNum)
    listasize+=1
print(lista)

import random
lista = []
for num in range(0,6):   
    if num not in lista:
        num = random.randint(1,45) 
        lista.append(num)
    else:
        lista.remove(num)   #pop은 삭제할 인덱스값, remove는 삭제할 값
print(lista)


# 문제 : 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함.
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외.
# 출력문 예제 : "오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다."
import random
lista = []
listasize = 1
studyday = random.randint(4,28)
while listasize < 5:
    lista.append(studyday)
    listasize +=1
print("스터디 모임 날짜는 ''.join(lista) 로 정했습니다.")

import random
studyday = random.randint(4,28)
print("오프라인 스터디 모임 일짜는 매월",studyday,"일로 선정 되었습니다.")
print("오프라인 스터디 모임 일짜는 메월"+str(studyday)+"일로 선정 되었습니다.")
print(f"오프라인 스터디 모임 일짜는 매월 {studyday} 일로 선정되었습니다.")

juminnumber = '123456-7891234'
print(juminnumber.split('-')[0])
print("성별 : ",juminnumber.split('-')[1][0])
print("나이: ",juminnumber.split('-')[0][:2],"년생")

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)
print(python.find("n"))
print(python.find("Java")) #-1
# print(python.index("Java")) #Error

print(python.count('n'))

# 포맷팅
print("나는 {}살입니다.".format(20))
print("나는 %d살입니다." % 20)
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨강"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20,color="빨간"))
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 문제 : 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예 ) http://naver.com
# 규칙: http://부분은 제외 => naver.com
# 규칙 : 처음 만나는 점(.)이후 부분은 제외 => naver
# 규칙 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e'의 갯수 (1) + "!" (!)로 구성
# 예 ) 생성된 비빌번호 : nav51!
site = "http://naver.com"
sitename =(site.split("//")[1]).split('.')[0]
password = sitename[:3],str(len(sitename)),str(sitename.count('e')),"!"
print("생성된 비밀번호 : ",''.join(password))

url = "http://naver.com"
my_str = url.replace("http://","") 
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))


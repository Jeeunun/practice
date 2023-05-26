# <문자열 str>
# 1. 문자열 더하기 ,곱하기
#   문) a = "python" b="is fun" print(a+b)?
'python is fun' 
#   문) a = "python" b="is fun" print(a*2+b)?
'pythonpython is fun'

# 2. 문자열 인덱스
#   문)문자열의 마지막 문자를 출력해보자.
a = "python's fun python's fun python's fun"
print(a[-1])
#   문)문자열의 길이
a = "python's fun python's fun python's fun"
print(len(a))
#    문)문자열의 길이함수를 활용하여 마지막문자 출력하기
a = "python's fun python's fun python's fun"
print(a[len(a)-1]) #len는 1,2,3,4,5,,,,로 시작 <-> index는 0,1,2,3,4,,,,->그래서 -1시켜줌

# 3. 문자열 슬라이싱 : 변수[x,y,z] (x이상, y미만, z-1씩 건너뛰기)
#   문) python만 잘라내서 b에 담아 출력
a = "python is fun"
print(a[:6])
#   문) 2번째 이상 7번째 미만 문자열 중에 1개씩 건너뛰고 b에 담아 출력
a = "python is fun"
print(a[2:7:2])
#   문) day와 date 출력
a = "20220505children's_day"
print(a[:8])
print(a[8:])

#  4. 문자 포맷팅 : 문자열 중간에 특정문자(숫자) 삽입 (%s,%d,%f)
#    문) 몸무게와 나이를 input으로 받고 문자열로 출력
age = int(input("나이를 입력하세요: "))
weight = float(input("몸무게를 입력하세요: "))
answer = "나이는 %d 이고 몸무게는 %f이다." % (age,weight)
print(answer)
        # age = int(input("나이를 입력하세요: "))
        # weight = float(input("몸무게를 입력하세요: "))
        # print("나이는 {}이고 몸무게는{}이다.",format(age,weight)) 
        ###TypeError: format() argument 2 must be str, not float

# ==============================================================================
# <사칙연산>
# 1. 제곱, 제곱근 
#   문) 2의 10제곱을 출력하라: a**b or math.pow(a,b) = a의 b승
print(2**10)
print(pow(2,10))
import math
print(math.pow(2,10))
#   문) 1024의 제곱근을 구하라 :math.sqr()
#   제곱근은 math라는 라이브러리를 import해줘야 한다.
import math
print(math.sqrt(1024))
#   문) x를 input으로 하고 y = 2.5 * x^2 + 3.3 * x +6 을 구하시오.
x = (int(input("x를 입력해주세요")))
y = 2.5 * pow(x,2) + 3.3 * x +6
print(y)

# ====================================================================
# <문자열 주요 함수>
# 1. count(문자)
a = "python"
print(a.count('o'))

# 2. find(문자), index(문자)
a = "python"
print(a.find('o'))
print(a.index('o'))
#   없는 문자를 찾을 경우 -1 return
whatyouwant = input("아무런 문자나 입력해주세요")
search = input ("찾고자 하는 문자 1개만 입력해주세요")
result = whatyouwant.find(search)
if result == -1:
    print("찾고자 하는 값이 없습니다")
else:
    print("요청하신 문자는 %d 번째에 있습니다" % result)

# 문. 연습문제
# 3개의 단어를 키보드로 입력 받아 각 단어의 첫글자를 추출 후 단어의 약자를 출력하라
# <조건1> 각 단어 변수(word1,word2,word3)
# <조건2> 입력과 출력 구분선 : 문자열 연산
# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr)저장
word1 = input('첫번째 단어를 입력하세요: ')
word2 = input('두번째 단어를 입력하세요: ')
word3 = input('세번째 단어를 입력하세요: ')
print("="*10)
abbr = word1[0]+word2[0]+word3[0]
print(abbr)

# 3. upper(),lower()
a = "hello"
print(a.upper())
b = "HELLO"
print(b.lower())

# 4. strip()
a = "  hello world  "
print(a.strip())

# 5. replace(a,b)
a = 'I studied python'
b = a.replace('python', 'java')
print(b)

# 6. split()
a = "I studied python"
b = a.split()
print(b)    #['I', 'studied', 'python']
# 공백의 차이 
a = "I     studied     python"
b = a.split()
print(b)    #['I', 'studied', 'python']
a = "I     studied     python"
b = a.split(" ")
print(b)    #['I', '', '', '', '', 'studied', '', '', '', '', 'python']
# 왜 이런 결과가 나왔을까? 공백을 문자로 인식했기 때문에
a = "I:studied:python"
b = a.split(":")
print(b)    #['I', 'studied', 'python']

# ===================================================================
# <List형> list = [value1,value2,value3,,,,] 
#   1. list[0] = value1
#      - 리스트 값은 인덱스로 접근 !
#       문) list_ex1 = ['a','b','c',[1,2,3]]이라는 리스트가 있다. 
#           변수 number에 [1,2,3]을 담아 출력하라. 
#           number에 담은 값 중 1과 3을 더해 4를 출력하라. 
list_ex1 = ['a','b','c',[1,2,3]]
number = list_ex1[3]
print(number[0]+number[2])

#      - 인덱스를 활용해 리스트값 수정
list_ex1 = ['a','b','c',[1,2,3]]
list_ex1[0] = 'b'
print(list_ex1) # ['b','b','c',[1,2,3]]

#   2. list[0:4] = value1, value2, value3, value4
#       리스트의 범위는 slicing사용

#   3. 리스트의 요소 세기
lista = ["1","2","3","4","1","1","3"]
counta = lista.count("1")
print(counta)

#   4. 리스트의 요소 삭제 : del 변수[인덱스], 변수.remove(값)
#      - del 변수 [index]
lista = ["1","2","3","4","1","1","3"]
del lista[0:3]
print(lista)
lista = ["1","2","3","4","1","1","3"]
del lista[2]
print(lista)
#       - remove : 리스트.remove(값)
lista = ["1","2","3","4","1","1","3"]
lista.remove("1")
print(lista)

#   5. 리스트의 요소 추가 : 변수.append(), 변수.insert(), 변수.extend()

#   6. 리스트의 정렬 :sort() / sort(reverse = True)

#   7. 리스트 뒤집기 : reversed.()

#   8. 리스트 위치반환(index) : list.index('값')
lista = ['김돌쇠','김갑돌','김갑순','김철수']
print(lista.index('김철수'))

#   9. 리스트 마지막 요소 끄집어내기 : pop()
lastvalue = lista.pop()
print(lastvalue) #김철수

lista.pop()
lastvalue = lista.pop()
print(lastvalue) #김갑순

            #비교
            #print(lista.pop()) #김철수

#   10. 리스트형 -> 문자열 변환
lista = ["hello","world","python"]
st1 = ""
st2 = st1.join(lista)
print(st2)    #helloworldpython
        # # for문으로도 할 수 있다.
        # for a in lista:
        #         st1 = st1 + a
        # print(st1)

#   11. 문자열 -> 리스트형 변환
sta = "hello world python"
mySta1 = list(sta)
print(mySta1)   #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'p', 'y', 't', 'h', 'o', 'n']
mySta2 = sta.split()
print(mySta2)   #['hello', 'world', 'python']

#   12. 리스트 값의 최대값 구하기
lista = [100,20,30,5,90]
# 위 리스트의 최대값을 정렬함수sort() X, 최대값함수max()X 
# 방법1
max_A = lista[0]
min_A = lista[0]
for a in lista:
    if max_A < a :
        max_A = a
    if min_A > a :
        min_A = a
        print(max_A,min_A)

min_A = lista[0]
for a in lista:
    if min_A > a :
        min_A = a
        print(min_A)

# 방법2
lista = [100,20,30,5,90]
max_A = max(lista)
min_A = min(lista)

# 방법3 lista.sort()
lista = [100,20,30,5,90]
lista.sort()
minA = lista[0]
maxA = lista[len(lista)-1]
maxA = lista[-1]
print(maxA)
print(minA)


# # 모든 특정한 숫자 9값을 삭제하려면?
# # lista = [1,3,9,3,5,6,9,9]
# # for a in range(0,len(lista)) : 
# #     if lista[a] == 9:
# #         del lista[a]
# # print(a) 
# #왜 에러가 날까? 
# # lista[0] != 9 -> lista[0] = 1
# # lista[1] != 9 -> lista[1] = 3
# # lista[2] == 9 -> del lista[2] => lista = [1,3,3,5,6,9,9]
# # lista[3] != 9 -> lista[3] = 5 => index Error :  del 하면 인덱스가 삭제한 자리에 앞으로 땡겨진다. lista[2]를 해야하는데

# # 해결 [방법1]
# lista = [1,3,9,3,5,6,9,9]
# count = 0 
# for a in range(0,len(lista)) :
#     if lista[a-count] == 9: 
#         del lista[a-count]
#         count = count + 1 
#         # if lista[a]==9, del lista[a]라면 lista=[1,3,3,5,6,9,9] 
#         # -> 다음 인덱스 검사는 lista[2]를 체크해야하는데 lista[3]부터 시작함 -> a-count해야함
# print(lista)
# # lista[0-0] != 9 -> lista =[1]
# # lista[1-0] != 9 -> lista = [3]
# # lista[2-0] == 9 -> lista[2-0] 삭제 & count = 0+1
# # lista[3-1] !=3 ( )

# # 해결 [방법2]
# lista = [1,3,9,3,5,6,9,9]
# listb = []
# for a in range(0,len(lista)) :
#     if lista[a] != 9: 
#         listb = listb + [lista[a]]   #listb = 1 
#         listb.append(lista[a])
# print(listb) 
# #lista[0] != 9 -> listb = listb + lista[0] = 1 -> listb.append(lista[0]) =listb.append(1) = print(listb) =[1]
# #lista[1] != 9 -> listb = listb + lista[1] = [1] + [3] -> listb.append = print(listb) = [1,3]
# #lista[2] == 9 -> X
# #lista[3] != 9 -> listb = listb + lista[3] = [1,3] + [3] -> listb.append = print(listb) = [1,3,3]
# #lista[4] != 9 -> listb = listb + lista[4] = [1,3,3] + [5] -> listb.append = print(listb) = [1,3,3,5]
# #lista[5] != 9 -> listb = listb + lista[5] = [1,3,3,5] + [6] -> listb.append = print(listb) = [1,3,3,5,6]
# #lista[6] == 9 -> X
# #lista[7] == 9 -> X 
# # 해결 [방법3]
# lista = [1,3,9,3,5,6,9,9]
# for a in range(0,len(lista)) : 
#     if 9 in lista: 
#         lista.remove(9)
#     else:
#         break
# print(lista)
# # lista[0]=1, lista[1]=3, lista[2]=9, lista[3]=3, lista[4]=5, lista[5]=6, lista[6]=9, lista[7]=9
# # if 9 in lista -> lista.remove(9) -> remove lista[2],[6],[7]
# # print(lista) = [1,3,3,5,6]
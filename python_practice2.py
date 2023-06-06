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
    print("요청하신 문자는 %d 번째에 있습니다" % (result+1))

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

#   10. 리스트형 -> 문자열 변환 : '구분자'.join()
lista = ["hello","world","python"]
st1 = ""
st2 = st1.join(lista)
print(st2)    #helloworldpython
        # # for문으로도 할 수 있다.
        # for a in lista:
        #         st1 = st1 + a
        # print(st1)

#   11. 문자열 -> 리스트형 변환 : list(문자열) or list.split('구분자')
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

# ===================================================================
# <tuple형>

# ====================================================================
# <dictionary형> dict = {'key' : 'value', 'key2' : value2',....}
#   1. 'key'를 이용한 'value'출력
dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남'}
print(dic1['이름'])             #인덱스활용 = 홍길동
print(dic1.get('이름'))         #함수 활용 = 홍길동

#   2. 'key'를 이용한 'value'추가(재정의) / 삭제(del)
dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남'}
dic1['신분'] = '학생'
print(dic1) #{'이름': '홍길동', '나이': 25, '성별': '남', '신분': '학생'}

dic1 = {'이름' : '홍길동', '나이' : 25, '성별' : '남'}
del dic1['성별']
print(dic1) #{'이름': '홍길동', '나이': 25}

#   3. 'key'목록 출력 : dict.keys()

#   4. 'value'목록 출력 : dict.values()

#   5. dictionary의 확장 : 변수.update()   cf.list는 변수.extend()
dic1 = {"a": 1, "b":2, "c":3}
dic2 = {"a": 2, "d":4 , "f":5}
dic1.update(dic2)
print(dic1)     #{'a': 2, 'b': 2, 'c': 3, 'd': 4, 'f': 5} 

#   6. 연습문제
# 딕셔너리로 변환해서 출력해보자. 예를들어 'A':2, 'B':1, 'O':2 이렇게 출력되도록 코딩해보자. dic = {key : value}
# 방법1
lista = ['A','A','B','O','O','AB','AB']
dicta = {}

for a in lista :
    if a not in dicta.keys():
        dicta[a] = 1    
    else :
        dicta[a] = dicta[a] + 1
print(dicta)

# 방법2
for a in lista :
    if a not in dicta.keys():
        dicta[a] = lista.count(a)    
print(dicta)

# =======================================================
# <set형>
#   1. 딕셔너리와 마찬가지로, index X와 중복 X
#   - 중복제거 : 중복을 제거하기 위해 리스트를 set으로 변환 시키기도 함
#   - index 사용불가 : 왜? 순서가 없어서
#   2. 집합의 개수를 구하는 함수 : len()
#   3. 문제 : 이 반 학생들의 혈액형 종류는 총 몇 개 인가?
lista = ['A','A','B','O','AB','B']
bloodtype = set(lista)
print(len(bloodtype))

#   4. 집합
#       - 합집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8])
#       s3 = s1 | s2   #|는 or를 의미
s3 = s1.union(s2)       #s3= s1 | s2
print(s3)
#       - 교집합
#           & 는 and를 의미 (앰퍼샌드)
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)

#       - 차집합
#       s2에서 s1을 뺀 차집합을 구해보자. 
s3 = s2.difference(s1)
s3 = s2 - s1
print(s3)

#       - 집합에서 값 추가 : add
s1 = {1,2,3,4,5,6}
# 7을 추가한 다음에 s1출력
s1.add(7)
print(s1)

#   5. set의 value 추가 : update()
s1 = {1,2,3,4,5,6}
s2 = {1,2,10,11,12}
s1.update(s2)
print(s1)

#   6. set의 value 삭제 : set.remove(값), set.discard(값)
s1 = {1,2,3,4,5,6}
s1.remove(1)
s1.discard(6)
print(s1)

# ================================================================
# <제어문 - if문>
#   1. if조건문 : 실행문 else : 실행문 or if조건문: 실행문 elif조건문: 실행문, 
#   2. if조건문을 한줄로 쓸 수 있다.
#   - if 조건문: print() 
#   - 두줄 이상의 코드를 한즐로 쓸 수 있다.
#   - if 조건문:print() ; else:print()
#   3. 조건부표현식(삼항연산자)
a = 10
print('A는 10보다 큽니다.')if a > 10 else print('A는 10보다 작습니다.')
#   4. 문제 : 얼마를 가지고 있습니까?를 변수에 담고, 만약 30,000원 이상이 있으면, 택시를 타고 가시오를 출력. 그렇지 않으면, 걸어가시오를 출력.
money = int(input("얼마를 가지고 있습니까? : "))
if money >= 30000:
    print("택시를 타고 가시오.")
else :
    print("걸어가시오.")
#   5. 문제: 1~10까지 담고 있는 하나의 리스트가 있다. 키보드로 정수 하나를 입력 받아 위 리스트에 그 값이 있는지 알아내라.
lista=[1,2,3,4,5,6,7,8,9,10]
num = int(input("숫자를 입력하세요: "))
if num in lista:
    print("값이 있습니다.")
else:
    print("값이 없습니다.")
#   6. 문제 : 짐의 무게를 input으로 설정하고 수수료 설정
numinput = float(input("짐의 무게를 입력하세요: "))
money = 10000*(numinput//10)
if numinput >=10:
    print("짐의 무게는 %f이고, 수수료는 %d 입니다." %(numinput,money))
    print(f"짐의 무게는 {numinput}이고 수수료는 {money}입니다.")

# <제어문 - for문>
#   1. for 변수 in 반복가능한 자료형(list, dictionary, set)
#   2. 반복가능한 자료형 => range(a,b) a이상 b미만 숫자를 담은 객체
#   3. 문제) 홀수인 값에 2를 곱한 값만을 list로 만들어라
lista = []
for a in range(1,11):
    if a %2 != 0 :
        lista.append(a*2)
print(lista)
#   4. 문제) for문을 이용해서 list 만들기
lista = []
for a in range(1,11):
    if a not in lista:
        lista.append(a)    
print(lista)

#   5. 문제 ) 1반에 수학점수가 60점이 넘으면 합격. 60점 미만이면 불합격.
lista = [90,25,67,45,80]
# 위 리스트가 학생의 번호순서대로 있을 때, 아래와 같이 출력하도록 코딩하여라. 
# 출력 예시 : "1번학생은 합격입니다."
for a in range(len(lista)):
    if lista[a] >= 60:
        print(f"{a+1}번째 학생은 합격입니다." )
    else :
        print(f"{a+1}번째 학생은 불합격입니다.")

#   6. for문과 break 
#       문제) 혈액형이 A형인 고객 선착순 1명만 찾는 상황.
lista = ['b','b','ab','a','b','a']
# 출력 결과 : n번째 고객이 이벤트에 당첨되었습니다.
for a in range(len(lista)):
    if lista[a] == 'a':
        print(a+1,"번째 고객이 이벤트에 당첨되었습니다.")
        print(f" {a+1} 번째 고객이 이벤트에 당첨되었습니다.")
        break #하나만 출력된다.

#   7. for문을 이용한 구구단
#   문제) 구구단 5단을 출력해보자 예를 들어)
#   5단 결과 출력 : 5X1 = 5.....5X10 = 50
for a in range(1,11):
    print(f'5*{a} = {5*a}')
#   문제) 이중for문 - 구구단을 5단~9단까지 한꺼번에 출력
# 방법1
for a in range(5,10):
    for b in range(1,11):
        print(f'{a}X{b} = {a*b}')
# 방법2
a = 5
while a <10:
    for b in range(1,11):
        print(f'{a}X{b} = {a*b}')
        a+=1

#   8. for문을 이용한 정렬 알고리즘
#   1) 들어가기 앞서, 자리 바꾸기를 알아보자. 
lista = [10,20,30,40] 
temp = lista[0] #자리 바꾸기 전
lista[0] = lista[1]
lista[1] = temp #자리 바뀐 후
print(lista)
# 파이썬에서 지원하고 있는 문법
lista[0],lista[1] = lista[1],lista[0]
#   2) 정렬 알고리즘
#   -sort() 내장함수 이용하는 방법

#   -선택정렬 : 0번째 index부터 가장 작은 값을 채워나가는 방식
#               첫번째 for문은 채워나가야 할 index를 의미
#               두번째 for문은 비교의 대상이 되는 index를 의미
lista = [93,45,21,30,20,94,66,71,45]
for a in range(len(lista)-1):
    for b in range(1,len(lista)):
        if lista[a] > lista[b]:
            temp = lista[a] #자리 바뀌기 전
            lista[a] = lista[b]
            lista[b] = temp #자리 바뀐 후
print(lista)

#   -버블정렬 
def bubble_sort_ascending(data):
    ## 총 교환 횟수를 기록하는 변수 (버블 정렬 원리 4)
    n_swap = 0
 
    ## 총 비교 횟수는 데이터 길이보다 1회 작게 이루어져야 함 (버블정렬 원리1)
    for i in range(len(data) - 1):
        
        ## 정리된 데이터는 반복할 필요가 없기 때문에 i회를 제외 시킨다.
        for i2 in range(len(data) - i - 1):
 
            ## 버블 정렬을 오름차순 혹은 내림차순으로 결정할 수 있는 영역
            if data[i2] > data[i2 + 1]:
                
                ## 순서를 바꿔 준 뒤에 교환이 이뤄졌음을 알린다.
                data[i2], data[i2 + 1] = data[i2 + 1], data[i2]
                n_swap += 1

#   9. 프로그래머스 연습문제 : 행렬의 덧셈
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 
# 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 
# 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
arr1 = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = [[2,3,4],[5,6,7],[8,9,10]]
# arr1[0][0]+arr2[0][0],arr1[0][1]+arr2[0][1],arr1[0][2]+arr2[0][2]....
answer =[[]]
for a in range(len(arr1)):
    temp = []
    for b in range(len(arr2)):
        temp.append(arr1[a][b] + arr2[a][b])
        answer.append(temp)
    print(answer)




# <제어문 - while문>
#   1. while 조건식 : ~실행문 => 조건식이 참일 때 실행문 무한반복.
#   2. 문제 ) 1~1000까지만 프린트 되도록 반복
a=1
while a<1001:
    print(str(a)+'번째 반복')
    a+=1

#   3. 문제 ) 1~1000 까지 더한 값과 평균값 출력
# 내가 푼 것
a=1
lista=[]
while a<1001:
    lista.append(a)
    a+=1
print(sum(lista))
print(sum(lista)/len(lista))
#  같이 푼 것
a=1
b=0
while a <1001:
    b+=a
    a+=1
print(b)
print(b/1000)

#   4. break와 continue

#   5. 문제) 나만의 리스트 만들기
#   리스트의 크기를 키보드로 입력받아 그 크기만큼 임의 숫자를 리스트에 추가하고
#   리스트의 크기와 값 전체를 출력하라.
listsize = int(input("리스트의 크기를 입력하세요: "))
a = 1
lista=[]
while a<listsize:
    listvalue = input("리스트의 값을 입력하세요: ")
    lista.append(listvalue)
    a+=1
print(lista)
print(len(lista))

#   6. 문제) 로또 번호 생성기
#   리스트의 크기가 6개인 리스트를 만들어서, 오늘의 로또번호를 만드어보자.
#   랜덤의 값을 추출하는 파이썬 라이브러리 -> random
import random
print(random.randint(1,45)) #print((int(random()*45) + 1)
lista=[]
listasize=1
while listasize < 7:
    randNum = random.randint(1,45)
    lista.append(randNum)
    listasize+=1
print(lista) 

# =================================================
# <함수>
#   1. 기본형태
#   def 함수명(input값):
#   계산식:
#   return

#   input값이 있어도 되고, 없어도 된다.
#   return값이 있어도 되고, 없어도 된다. 

#   2. 출력
#   변수 = 함수명(input)
#   print(변수)

#   3. 문제) 함수 직접 구현해보기
#   함수명은 myPlustFunc
#   함수의 로직은 사용자의 input을 받아 input값의 누적합을 더하는 함수
#   예를 들면 100을 입력하면 1+2+3+4....+100
def myPlusFunc(numinput):
    for a in range(1,numinput+1):
        tot +=a
        return tot 
# 출력해보기
result = myPlusFunc(10)
print(result)

#   4. 문제) 함수 직접 구현해보기
# input값을 2개를 받아 2값을 더한 뒤, *2만큼 하여 return하는 함수를 만들어보자.
# 그리고, 해당 함수를 호출하여 호출된 결과값을 result에 담아 출력해보자.
def myPlusFunc(num1,num2):
    calc = (num1+num2)*2
    return calc

result = myPlusFunc(10,20)
print(result)

#   5. 문제) 함수 직접 구현해보기
# 리스트의 index함수를 쓰지 않고, for문 또는 while문을 통해 
# 숫자 9가 몇 번째 인덱스에 있는 값인지 print해보자. 
#   -1. index함수 사용한 경우
lista = [1,4,6,9,9]
print(lista.index(9))
#   -2. for를 이용한 경우
for a in range(len(lista)):
    if lista[a] == 9:
        print(a)
        break
#   -3. 함수로 구현
# 위의 for문을 활용하여 myIndex라는 이름의 함수를 만들고자 한다.
# input값이 2개 (list, 찾고자하는 값)
# print는 함수내에서 하지 않고, return에 값을 담는다. 
def myIndex(l, num):
    for a in range(len(l)):
        if l[a] == num:
            return a
# 출력해보기
result = myIndex([1,2,3,4,5,6,7,8,9],5)
print(result)

# 다른방법
lista = [1,4,6,9,9]
def myIndex(i1,i2):
    result =-1
    
#   6. 문제) 키보드로 반지름의 길이를 입력받고, 원의 넓이를 구하는 함수를 만들어 결과를 출력하라.
def width(num1):
    result = num1**2*3.14
    return result
num1 = int(input("반지름의 길이를 입력하세요: "))
a = width(num1)
print(a)

#   7. return이 필요한 경우와 아닌 경우
def hello1():
    print("hello1 python") #'식'이 없어
hello1()

def hello2():
    result = "hello2 python" #'식'을 변수로 받아.
    return result #return값이 있어야 함수식에서 떠돌지 않아.
result = hello2() 
print(result)

#   8. 입력값의 개수가 정해져있지 않고 multiple한 함수
def sum(*args):
    total = 0
    for a in args:
        total+=a
    return total

result = sum(2,5,7)
print(result)

#   9. 2개 이상의 리턴값이 있는 경우 : 튜플형태로 데이터 return
def cal(a,b):
    result1 = a+b
    result2 = a-b
    result3 = a*b
    return result1,result2,result3
calValue = cal(1,2)
for x in range(len(calValue)):
    print(f"계산한 {x+1}번째 값: {calValue[x]}")

#   10. 함수에서 default값 세팅
#   - default값 세팅하는 대표적인 예시가 print함수
print('hello',end=' ')
print('world')
# 출력 : hello world (end =''는 print의 default값 줄바꿈을 없앤다.)

#  11. 매개변수의 순서를 안맞추고도 원하는 매개변수의 자리에 값을 넣어 함수 호출
def whoAreYou(name, age, gender):
    print(f"제 이름은 {name}이고, 나이는 {age},성별은 {gender}입니다.")
whoAreYou(age=19, name='홍길동', gender='남자')

#   12. 지역변수와 전역변수
#   - 지역변수 : 함수 내에서 사용하는 변수. 함수 호출 뒤 사라진다.
#   - 전역변수 : 함수 밖에서 사용하는 변수. 
#   - 예시
a = 1   #전역변수
def Fn():
    a = 2 #지역변수
    print(a) #지역변수 2 출력
Fn() #지역변수 2 출력
print(a) #전역변수 1 출력 => 지역변수는 함수 호출 뒤 사라짐 => 전역변수만 남게 된다.

#   - 예시
a = 100 
c = 200
def sum(a,b,c): 
    result = a+b +c
    return result
result = sum(10,20,30) 
# sum함수 지역변수 a,b,c
print(result) 
# 전역변수 a=100, c=200
print(a) # 100
print(c) #200
#a,c가 각각 100,200이 나온 이유는 지역변수가 함수 실행후 종료되었기 때문에

#   - 전역변수를 지역변수로 사용하기 위해선 => global + 전역변수
a = 100 
c = 200
def sum(a,b): 
    global c
    result = a+b +c
    return result
result = sum(10,20) 
print(result) 

#   - 전역변수가 없는데 global로 전역변수를 만들 수 있다.
def Fn():
    global a
    a = 10
    print(a)
Fn()
print(a) #전역변수 10출력
    # # 비교 : 
    # def Fn():
    #     a = 10 #지역변수 
    #     print(a)
    # Fn()
    # print(a) #전역변수 a가 없으므로 출력오류

# ------------------------------------------------------
# <그 외 함수>
#   1. lambda함수 (lambda 매개변수 : 실행문)
#   - 1)함수를 간편하게 표현하기 위한 방식
def add(a,b):
    return a+b
print(add(1,2))
#   -> 람다함수로 표현하기
lambdaA = lambda a,b : a+b
print(lambdaA)
#   -> list에 lambda함수를 담아서 사용가능
cal_list = [lambda a,b : a+b, lambda a,b : a-b, lambda a,b: a*b]
print(cal_list[0](1,2))
print(cal_list[1](1,2))
print(cal_list[2](1,2))    
#   -> dictionary에 lambda함수를 담어서 사용가능
cal_list = {"plus":lambda a,b : a+b, "minus":lambda a,b : a-b, "multiply":lambda a,b: a*b}
print(cal_list["plus"])
print(cal_list["minus"])
print(cal_list["multiply"])

#   -2) 함수를 변수로 사용하기 위한 방식
#   -> lambda로 입력한 매개변수가 짝수이면 True, 홀수이면 False
# 예시 if else 쓸 수 있다.
def TrueOrNot(x):
    if x % 2 == 0:
        return True
    else:
        return False
TrueOrNot = lambda x : True if x % 2 ==0 else False

#   2. map 함수 : 특정함수와 반복가능한 자료형을 입력받아, 특정함수가 수행한 결과값을 return
#   map(함수, 리스트(또는 튜플 등등))
#   - 예시
def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4])))
#   - map함수와 lambda함수를 사용해서 입력한 list의 제곱값을 담은 리스트를 출력하도록 하자.
print(list(map((lambda x: x**2), [2,4,6,8])))

#   3. filter함수 : 대상이 되는 리스트에서 함수를 적용하여 참/거짓 조건으로 값을 걸러내는 것 -> 참인 것만 뽑음.
#   filter(함수, 리스트(또는 튜플 등등))
#   - 예시
def trueOrNot(x):
    if x>0 :
        return True
    else:
        return False
print(list(filter(trueOrNot, [-1,5,-7,-4])))
print(list(filter(True if x>0 else False, [-1,5,-7,-4])))
    # map과 비교
    # lst = list(map(lambda x : True if x > 0 else False, [-1,0,3,-2,5]))
    # print(lst)
    # [False, False, True, False, True]
    # =true false가 새로운 리스트에 담기게 된다. 
#   -문제 ) # 함수형 프로그래밍(lambda,map,filter)을 사용하여, 주어진 list에서 홀수만 추출하도록 하여라.
lista = [4,7,1,2,5,6,8]
lst = list(filter(lambda x : True if x%2 != 0 else False, lista))
print(lst)

#   4. sum() : 주어진 자료들의 총합
lista = [4,7,1,2,5,6,8]
lst = list(filter(lambda x : True if x%2 != 0 else False, lista))
sum_value = sum(lst)
print(sum_value)

#   5. ord() : 문자를 아스키코드로 변환 / chr() : 코드를 문자로 변환

#   6. abs() : 절대값 구하기
print(abs(-3)) #3
#   문) map을 사용해서 주어진 리스트를 절대값으로 변환한 리스트를 출력해보자. 
lista = [1,-5,12,-5]
lst = list(map(abs,lista))
print(lst)

    # - 함수를 안쓰고 for 반복문으로도 풀어보기
lista = [1,-5,12,-5]
for a in range(len(lista)):
    if lista[a] < 0 :
        lista[a] = abs(lista[a])
print(lista)

# ----------------------------------------------------
#  <재귀함수>
#  -전형적인 예제 :factorial
def solution(n):
    total = 1
    for a in range(1,n+1):
        total*=a
    return total
#     출력해보기
n = int(input("숫자를 입력하세요: "))
answer = solution(n)
print(answer)
#   - 재귀함수란 함수내에서 함수자기자식을 호출하는 방식
#   - 재귀함수에서는 반드시 재귀함수를 종료시키는 조건이 들어가야 한다. 

#   -재귀함수 만들어보기

# -------------------------------------------------------
#  <Class>
#   1. 사용이유 :
#   -1) 같은 기능의 함수의 집합
#   -2) 객체를 만들기 위해 사용
#   - 명명규칙 : 일반적으로 클래스는 대문자 알파벳으로 / 변수명, 함수명은 소문자로

#   2. 예시)
#   - 사칙연산 함수가 있을 때 Calculator라는 클래스에 모아둘 수 있다.
class Calculator: #class 이름 = Calculator
    def plus(a,b): #class내에 선언된 함수 = 메서드
        return a+b
    def minus(a,b):
        return a-b 
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b 
print(Calculator.plus(10,20)) 
#       -> 이 클래스의 문제점 : 누적된 값을 변수로 갖고 있지 않다.

#   3. 클래스 변수 접근 방법
#   - 클래스 변수 접근가능 방법1 : 클래스명.변수
#   - 클래스 변수 접근가능 방법2 : classmethod데코레이터 사용
#   - 예시)
class Calculator:
    result = 0 #누적값을 변수로 만든다.
    @classmethod #@classmethod선언 
                #인스턴스 메서드가 객체의 인스턴스 필드를 self를 통해 엑세스할 수 있는 반면, 
                # 정적 메서드는 이러한 self 파라미터를 갖지 않고 인스턴스 변수에 엑세스할 수 없다. 
                # 따라서, 정적 메서드는 보통 객체 필드와 독립적이지만 로직상 클래스내에 포함되는 메서드에 사용된다. 
                # 정적 메서드는 메서드 앞에 @staticmethod 라는 Decorator를 표시하여 해당 메서드가 정적 메서드임을 표시한다
    def plus(cls,a): #classmethod데코레이터 => self가 아닌 cls로
        cls.result+=a #Calculator함수에 누적변수result => result값에 계속해서 누적 가능.
    def minus(a):
        Calculator.result-=a
    def multiply(a):
        Calculator.result*=a 
    def divide(a):
        Calculator.result/=a       
print(Calculator.result)
Calculator.plus(10)
print(Calculator.result)
Calculator.minus(5)
print(Calculator.result)

#   4. 객체와 인스턴스
#   - 객체 : 클래스의 복제본 ex. 객체(aCompany)
#   - 인스턴스 : 객체와 클래스의 관계를 설명할 때 인스턴스를 사용  ex. Calculator 클래스의 인스턴스는 aCompany

#   - 객체 사용이유 - 클래스의 중복 제거 (=변수와 함수의 재활용의 어려움 해결)
#   - 객체 형식의 클래스의 기본구조 (instance method)
class Calculator:
    # 객체가 생성될때 init은 가장 먼저 실행된다.
    # 생성자는 객체생성될 때 객체변수를 초기화. 
    # result와 self.result는 다른 값이다. => result(지역변수) / self.result(객체의 변수)
    def __init__(self): # 생성자(__init__) 선언
        self.result=0   # 최초값(객체변수의 초기화)
    # 객체를 만들 때 매서드 내의 첫번째 매개변수는 객체(self)를 의미한다. 
    def plus(self,a):
        self.result+=a 
    def minus(self,a):
        self.result-=a
    def multiply(self,a):
        self.result*=a 
    def divide(self,a):
        self.result/=a    

aCompany = Calculator() #객체가 만들어짐 => Calculator의 복제본. => aCompany의 Calculator => self = aCompany
aCompany.plus(100)
bCompany = Calculator() #객체가 만들어짐 => Calculator의 복제본. => bCompany의 Calculator => self = bCompany
bCompany.plus(100) 
print(aCompany.result)
print(bCompany.result) 

#   5. 옵션주기 : 클래스생성 시 매개변수(a)를 통해 초기값 세팅가능
class Calculator:
    def __init__(self,a): 
        self.result=a   
    def plus(self,a):
        self.result+=a 
    def minus(self,a):
        self.result-=a
    def multiply(self,a):
        self.result*=a 
    def divide(self,a):
        self.result/=a    
aCompany = Calculator(1000)
print(aCompany.result)
aCompany = Calculator(2000)
print(bCompany.result) 

#   6. 문제) person이라는 클래스를 만든다. 생성자로 이름(name), 나이(age), 성별(gender), email이라는 매개변수를 받아 각각의 객체변수를 만든다. 
# register 메서드를 만들어서 해당메서드에서는 myInfo라는 객체변수에 이름, 나이, 성별, email정보를 문자열로 담는다. 
# 2명의 person을 만든다.

class Person: #person 클래스
    def __init__(self,name, age, gender, email): #self(객체)/name,age,gender,email(생성변수)
        self.name = name    #객체의 변수 = 생성변수
        self.age = age
        self.gender = gender
        self.email = email
    def register(self): # 클래스의 메서드 
       self. myInfo = "이름:{}, 나이:{}, 성별:{}, 이메일:{}.". format(self.name, self.age, self.gender, self.email)

p1 = Person('홍길동', '25','남자','1234@naver.com')
p2 = Person('손흥민', '30', '남자','5678@gmail.com')

p1.register()
p2.register()

print(p1.myInfo)
print(p2.myInfo)

#   + 회원가입일 추가하기 = datetime 이용
import datetime
register_date = str(datetime.datetime.now())
print(register_date[:11])

class Person:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.register_date = str(datetime.datetime.now())
    def register(self):
        self. myInfo = "이름:{}, 나이:{}, 성별:{}, 이메일:{}, 회원가입일:{}". format(self.name, self.age, self.gender, self.email, self.register_date)

p1 = Person('홍길동', '25','남자','1234@naver.com')
p2 = Person('손흥민', '30', '남자','5678@gmail.com')

p1.register()
p2.register()

print(p1.myInfo)
print(p2.myInfo)       

#   5. 클래스 상속
#   - 부모 클래스에서의 기능을 자식클래스에서 물려받는 것.
#   - 자식클래스 선언 형식: class 자식클래스명(부모클래스명)
# -부모클래스-
class Calculator:
    def __init__(self):
        self.result = 0
    def plus(self,a):
        self.result+=a
    def minus(self,a):
        self.result-=a
    def multiply(self,a):
        self.result*=a
# -자식클래스-
class CalculatorChild(Calculator):
        # 1) 자식클래스의 init설정할 수 있다. (=부모클래스의 init을 덮어쓰는 것.)
        # def __init__(self):
        #     self.result = 100 
    def divide(self,a):
        self.result/=a
        # 2)자식클래스만의 메서드 사용가능.
    def multiply(self,a):
        self.result*=(a+1)
        # 3) 부모클래스의 메서드를 자식클래스의 메서드로 재정의 할 수 있다. (*overriding) 
        #  = 부모에게 있는 기능을 재선언하게 되면 부모의 기능보다 자식의 기능이 우선

# ------------------------------------------------------------------------------
# <예외처리 : try except 구문>
#   1. 예외처리를 해야하는 이유는 뭘까?
#   - 프로그램 실행 중간에 예외가 발생하더라도 프로그램이 강제종료되지 않도록 하기 위해
#   -> 현실에서 빈번하게 발생할 수 있는 경우(사용자input, DB조회) 예외처리를 한다.

#   2. 예시
while True:
    try:
        first = int(input("분자를 입력하세요: "))
        second = int(input("분모를 입력하세요: "))
        print(first/second) 
    except:
        print("오류입니다.")
    finally:
        print("결과를 확인해주세요.")
        #=> except를 좀 더 명확하게 보여주기 위해
# 수정
while True:
    try:
        first = int(input("분자를 입력하세요: "))
        second = int(input("분모를 입력하세요: "))
        print(first/second) 
    except ZeroDivisionError as zd:
        print(f"{zd} 오류입니다.") 
    except ValueError as ve:
        print(f"{ve} 오류입니다.")
    except Exception:
        print(f"{Exception} 오류입니다.")
    finally:
        print("결과를 확인해주세요.")

#   3. 에러 강제 예시
#       - 방법
while True:
    raise Exception
#       - 예시
class Bird:
    def fly(self):
        raise Exception
    
class Eagle(Bird):
    pass

eagle1 = Eagle() #객체만들기
eagle1.fly() #함수적용 => 출력 : Exception => 오버라이딩 강제

# -->  자식클래스로 하여금 overriding 재정의 유도 해준다. 
class Bird:
    def fly(self):
        raise Exception
    
class Eagle(Bird):
    def fly(self):
        print("fly fly")
    pass

eagle1 = Eagle() 
eagle1.fly()

# ---------------------------------------------------
# <Module>
#   1. 방법
#   - import하고 싶은 모듈이 있으면 import구문 사용
#   - from 패키지명 import 파일명 / import 패키지명.파일명
#   - as를 사용하여 약어로도 사용가능

# ----------------------------------------------------
# <파이썬으로 file만들기>
#   1. open: file시스템 입출력 라이브러리 
#       -open함수는 mode(w,r,a)을 갖고 있다. 
#       -open을 했을 때 해당 파일명이 없으면 자동생성
f = open("test.txt","w")
f.close()

#   2. w옵션 : write
f = open("test.txt","w", encoding="UTF-8") #encoding="UTF-8" => 컴퓨터가 인식가능할 수 있는 숫자로 변환시켜주는 것.
for i in range(0,10):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)   #file에 data 덮어쓰기
f.close()   
#   3. r옵션 : read
#   1. readline = 첫번째 줄만 가져오는 함수
f = open("test.txt","r",encoding="UTF-8")
line = f.readline()
print(line)
f.close() #0번째 줄입니다. 

#   2. readlines : 데이터를 리스트형태로 라인별로 담아준다.
f = open("test.txt","w",encoding="UFT-8")
lines = f.readlines
print(lines)

#   3. read : 데이터를 한꺼번에 문자열로 담아준다.
f = open("test.txt","w",encoding="UFT-8")
lines = f.readlines
print(lines)

# read보다 readlines을 쓴다 => 데이터 parsing이 편하기 때문에


#   4.  while, if문으로 readline으로 전체 출력
# 방법1
line = f.readline
while line: #line이 없으면 False로 인식 -> 멈춤
    print(line)
    line = f.readline
f.close()

# 방법2
while True:
    line = f.readline()
    print(line)
    if not line:
        break
f.close()

#   4. a옵션 : c (추가모드)
f = open("test.txt","a",encoding="UTF-8")
# 0~9번째 줄입니다. -> 10번째~19번째 줄입니다. 
for i in range(10,20):
    data = "%d번째 줄입니다. \n" %i     
    f.write(data)
f.close()
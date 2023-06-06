# # n = 10
# # n(10)이하의 짝수를 모두 더한 값 = answer
# n = 10
# answer = 0
# for a in range(1,(n+1)):   
#     if a % 2 == 0:
#         answer+=a
# print(answer)


# def solution(n):
#     return sum([i for i in range(2, n + 1, 2)])

# ----------------
# <아이스아메리카노>
# coffee_price = 5500
# money = int(input("가진 돈이 얼마 입니까? "))
# drink = money // coffee_price
# change = money % coffee_price
# print(f"가진 돈은 {money}이고, 마실 수 있는 잔 수는 {drink}이며 잔돈은 {change}원입니다.")

# ------------
# 최댓값 만들기(1)
# numbers = [0,31,24,10,1,9]
# numbers.sort()
# print(numbers[-1]*numbers[-2])

# -------------
# <점의 위치 구하기>
# def solution(dot):
#     if dot[0] > 0 and dot[1] > 0:
#         return 1
#     elif dot[0] < 0 and dot[1] > 0:
#         return 2
#     elif dot[0] < 0 and dot[1] < 0:
#         return 3
#     elif dot[0] > 0 and dot[1] < 0:
#         return 4

# dot = [-7,9]
# result = solution(dot)
# print(result)

# --------------------
# <중복된 숫자 개수>
# array = [1,1,2,3,4,5]
# n = 1
# if n in array:
#     result = array.count(n)
#     print(result)

# def solution(array,n):
#     if n in array:
#         answer = array.count(n)
#     else:
#         answer = 0
#     return answer

# def solution(array, n):
#     return array.count(n)
# -----------------------
# <배열의 유사도>
# s1 = ["a","b","c"]
# s2 = ["com","b","d","p","c"]
# s3 = []
# for a in s1:
#     if a in s2:
#         s3.append(a)
# print(len(s3))

# s1 = ["n", "omg"]
# s2 = ["m", "dot"]
# s3 = []
# for a in s1:
#     if a in s2:
#         s3.append(a)
# print(len(s3))
# ----------------------------
# <삼각형의 완성조건(1)>
# sides = [199,72,222]
# sides.sort()
# if sides[2] < (sides[0]+sides[1]):
#     print(1)
# else : 
#     print(2)
# ----------------------------
# <중앙값 구하기>
# import math
# array = [1, 2, 7, 10, 11]
# array.sort()
# answer = array[math.ceil(len(array)/2)-1]
# print(answer) 

# def solution(array):
#     return sorted(array)[len(array) // 2]
# -------------------------
# <모음제거>
# def solution(my_string):
#     vowels = ['a','e','i','o','u']
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     return my_string

# my_string = "nice to meet you"
# remove_char = "aeiou"
# new_string = my_string.translate(my_string.maketrans("","",remove_char))
# print(new_string)
# -----------------------------
# <피자 나눠먹기(3)>
# def solution(slice, n):
#     if n % slice == 0:
#         answer = n // slice
#     else :
#         answer = (n // slice) +1
#     return answer
# ------------------------
# <특정 문자 제거하기>
# my_string = "abcdef"
# remove_str = "f"
# answer = my_string.translate(my_string.maketrans("","",remove_str))
# print(answer)

# def solution(my_string, letter):
#     answer = my_string.translate(my_string.maketrans("","",letter))
#        return answer

# --------------------------
# <옷가게 할인 받기>
# def solution(price):
#     if  100000 <= price < 300000 :
#          return int((price * 0.95))
#     elif 300000 <= price < 500000 :
#          return int((price * 0.9))
#     elif 500000 <= price :
#          return int((price * 0.8))
#     else : 
#         return price
# ----------------------------
# <머쓱이보다 키 큰 사람>
# array = [180, 120, 140]
# height = 180

# array.append(height)
# array.sort()
# print(len(array)-(array.index(height)+1))

# lista = []
# for a in array:
#     if a> height:
#         lista.append(a)
# print(len(lista))

# def solution(array, height):
#     array.append(height)
#     array.sort(reverse=True)
#     return array.index(height)
# --------------------------------
# <분수의 덧셈>
# import math
# def solution(numer1, denom1, numer2, denom2):      
#     numer = ((numer1*denom2) + (numer2*denom1)) 
#     denom = (denom1*denom2) 
#     i = math.gcd(numer,denom)
#     return [numer//i,denom//i]

# result = solution(1, 2, 3, 4)
# print(result)

# -------------------------------
# <배열 두 배 만들기>
# numbers = [1, 2, 100, -99, 1, 2, 3]
# result = list(map(lambda x: x*2, numbers))
# print(result)
# --------------------------------
# <최빈값 구하기>

# def solution(array):
array = [1,2,3,3,3,4]     
dict ={}
for i in array:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
#     answer = 0
#     if len(dict)==1 : 
#         answer = list(dict.keys())[0]
#     else:
#         first_max = sorted(dict.values())[-1]
#         second_max = sorted(dict.values())[-2]
#         if first_max == second_max:
#             return -1
#         else:
#             for key, value in dict.items():
#                 if value == first_max:
#                     answer = key
#                     return answer
# array = [1,2,3,3,3,4]                
# result = solution(array)
# print(result)
# -------------------------
# <짝수는 싫어요>
# n = 15
# result = []
# for a in range(1,n+1):
#     if  a % 2 != 0:
#         result.append(a)
# print(result)
# ---------------------------
# <최대공약수>
# # for문 이용하기 
# a=72
# b=90
# def gcd(a,b):
#     for i in range(min(a,b),0,-1): #range역순 range(72,0,-1)
#         if a%i==0 and b%i==0:
#             return i
        
# # 유클리드 호제법
# def gcd(a,b):
#     while b>0:
#         a,b = b,a % b
#     return a

# def gcd(a,b):
#     if a % b == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         return gcd(b,a%b)
    
# # math 라이브러리
# import math
# a,b = 10,15
# math.gcd(a,b)
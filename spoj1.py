# a, b, c = map(int, input("3,4,5 gurwaljnii taluud perimitriig ol").split())
# print(a + b + c)


# a, b = map(int, input("2toonii niilberoiig ol 12 23").split())
# print(a + b)


# a = int(input("cubiin gadarguu bolon ezelhuun ol 5"))
# b = a ** 3
# c = (a** 2) * 6
# print(b, c)


# a, b = map(int, input("6 4 talbai bolon perimetr ol").split())
# c = a * b
# d = (a + b) * 2
# print(c, d)


# x = int(input(1 geed bich))
# y = 3 * x - 5
# print(y)


# x = int(input(-2 geed bich))
# y = 4 * x ** 2 - 3 * x + 5
# print(y)


# a = int(input("476 suuliin tsifr"))
# b = a // 100
# c = a // 10
# d = a % 10
# print(d)


# a = int(input("423 arawtiin oroniig garga"))
# b = a //10 % 10
# print(b)


# a = int(input("27 negj arawtin ornii tsifruudin urjwer"))
# b = a // 10 % 10
# c = a % 10
# print(b * c)


# a = int(input("123 tsifruudiin niilber"))
# b = a // 100 % 10
# c = a // 10 % 10
# d = a % 10
# e = b + c + d
# print(e)


# a = int(input("200 secondiig minut second bolgo"))
# b = a // 60 % 10
# c = a % 60
# print(b, c)


# a = int(input("3612secondiig tsag min sec bolgo"))
# b = a // 3600 % 60
# c = a // 60 % 60
# d = a % 60
# print(b, c, d)


# a, b = map(int, input("3minut 4 secondiig second bolgo").split())
# c = a * 60 + b
# print(c)


# a, b, c = map(int, input("1tsag 2minut 3seciig second bolgo").split())
# d = (a * 3600) + (b * 60) + c
# print(d)


# a = int(input("44 tsagiig honog tsag bolgo"))
# b = a // 24 % 24
# c = a % 24
# print(b, c)


# a, b = map(int, input("2odor 5tsagiig tsagruu shiljuul").split())
# c = a * 24 + 5
# print(c)


# a = int(input("27 sariig jil sar bolgo"))
# b = a // 12 % 12
# c = a % 12
# print(b, c)


# a, b = map(int, input("2jil 7 sariig sar bolgo").split())
# c = a * 12 + b
# print(c)


# a, b = map(int, input("16 14 ihiig hewle").split())
# if a > b :
#     print(a)
# else:
#     print(b)


# a, b = map(int, input("9 6 bagiig ni hewle").split())
# if a > b :
#     print(b)
# else :
#     print(a)


# a, b, c = map(int, input("3toonii ihiig hewle").split())
# if a >= b and a >= c :
#     print(a)
# elif b >= a and b >= c :
#     print(b)
# else :
#     print(c)


# a, b, c, d = map(int, input("4n toonii bagiig hewle").split())
# if a <= b and a <= c and a <= d :
#     print(a)
# elif b <= c and b <= d and b <= a :
#     print(b)
# elif c <= d and c <= b and c <= a :
#         print(c)
# else :
#     print(d)


# 80s ih toonuudiin niilber
# a = [85,   75, 96, 69]
# a.sort(reverse = True)
# b = a[0] + a[1]
# print(b)

# 4toonii 5s baga toonuudiin urjwer
# a = [3, 6, 2, 4]
# a.sort()
# b = a[0] * a[1] * a[2]
# print(b)


# tegsh toonuudiin niilber
# a = list(map(int, input().split()))
# total = 0
# for i in a:
#     if i % 2 == 0:
#         total += i
# print(total)


# sondgoi toonuudiin urjwer
# a = list(map(int, input().split()))
# b = 1
# for i in a :
#     if i % 2 != 0 :
#         b *= i
# print(b)


# 5tai tentsuu toonuudiin too
# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if i == 5:
#         b += 1
# print(b)


# 3D HUWAAGDAH TOONUUD
# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if i % 3 == 0 :
#         b += 1
# print(b)


# 11d huwaagdahgui toonuud
# a = list(map(int, input().split()))
# b = 0
# for i in a:
#     if i % 11 != 0 :
#         b += 1
# print(b)


# 10aas ih
# a = int(input())
# if a < 10 :
#     print("No")
# else : 
#     print("Yes")


# 5aas baga
# a = int(input())
# if a > 5 :
#     print("No")
# else : 
#     print("Yes")


# tegsh too bol yes gej hewle
# a = list(map(int, input().split()))
# for i in a :
#     if i % 2 == 0 :
#         print("Yes")
#     else :
#         print("No")


# for i in range(1):
#     print("IOI")


# for i in range(3):
#     print("IOI")


# a = int(input())
# for i in range(a) :
#     print("IOI")


# b = 0
# a = int(input())
# for i in range(1, a+1) :
#     b += i
# print(b)


# n toonii factorialig ol
# b = 1
# a = int(input())
# for i in range(1, a+1) : 
#     b *= i
# print(b)


# a = int(input())
# b = a * 100
# print(b)


# a, b = map(int, input().split())
# c = a * b
# print(c)


# a = int(input())
# b = 2 ** a
# print(b)


# a, b = map(int, input().split())
# c = a ** b
# print(c)


# a = int(input())
# if a >= 3 :
#     print("Tentssen")
# else :
#     print("Unasan")


# a = int(input())
# if a >= 5 :
#     print("Onts")
# elif a == 4 :
#     print("Sain")
# elif a == 3 :
#     print("Dund")
# else :
#     print("Muu")


# a = int(input())
# if a >= 90 :
#     print("A")
# elif a >= 80 :
#     print("B")
# elif a >= 70 :
#     print("C")
# elif a >= 60 :
#     print("D")
# else :
#     print("F")


# a = int(input())
# if a == 1 :
#     print("Monday")
# elif a == 2 :
#     print("Tuesday")
# elif a == 3 :
#     print("Wednesday")
# elif a == 4 :
#     print("Thursday")
# elif a == 5 :
#     print("Friday")
# elif a == 6 :
#     print("Saturday")
# else : 
#     print("Sunday")


# month = int(input())
# if month in [12, 1, 2]:
#     print("Winter")
# elif month in [3, 4, 5]:
#     print("Spring")
# elif month in [6, 7, 8]:
#     print("Summer")
# elif month in [9, 10, 11]:
#     print("Autumn")
# else :
#     print("Enough")


# a, b, c = map(int, input().split())
# if a + b > c and a + c > b and b + c > a:
#     print("YES")
# else:
#     print("NO")


# a, b, c = map(int, input("2, 3, 4 toonii ilerhiileliin utga").split())
# d = a * b - c
# print(d)



# a = int(input())
# for i in range(1, 11):
#     print(f"{a}*{i}={a*i}")


# a, b = map(int, input().split())
# print(f"{a ** b}")
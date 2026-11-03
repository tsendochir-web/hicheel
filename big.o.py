# numbers = [1, 2, 3, 4, 5]

# print(numbers[0])
# O(1)




# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
    # print(number)
# O(n)


# numbers = [10, 20, 30, 40, 50]
# print(numbers[-1])
# O(1)


# n = int(input("n: "))
# for i in range(n):
    # print(i)
# O(n)


# for i in range(n):
    # print(i)
# O(n)


# for i in range(n):
    # for j in range(n):
        # print(i, j)
# O(n2)


# n = 5
# for i in range(n):
    # for j in range(n):
        # print(i, j)
# 



# for i in range(n):
    # for j in range(n):
        # print(i, j)
# 10baihoo bi oortoo itgej bna



# for i in range(n):
    # print(i)
# for j in range(n):
    # print(j)
# O(n) l baih shg bnadaaa ho



# amrhnshdee dawhar dawtalt l gej oilgoloo O(n2)



# 1000
#  ↓
# 500
#  ↓
# 250
#  ↓
# 125
#  ↓
# 62
#  ↓
# 31
# Log(n)


# tallaad shalgadag l gesenshd ho


# 
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0])
# for number in numbers:
    # print(number)
# 1l baihshg bnada



# for i in range(n):
    # print(i)
# print("Hello")
# baihguin bishu ain ain


# for i in range(n):
    # for j in range(n):
        # print(i, j)
# print("Done")
# bas baihgui l ymshg hargdaad bnadaa



# for i in range(n):
    # for j in range(n):
        # print(i, j)
# print("Done")
# O(1) Log(n) O(n) O(n2)



# # A
# print(numbers[0])

# B
# for x in numbers:
    # print(x)

# C
# for x in numbers:
    # for y in numbers:
        # print(x, y)
# D
# 1000 → 500 → 250 → 125 → ...
# a=O(1) b=O(n) c=O(n2) d=Log(n)

# 1.1
# age = int(input("Nasaa :"))
# if age >= 18 :
#     print("Orj bolnoo")
# else :
#     print("Bolohguie ho")



# 1.2
# num = int(input("Too:" ))
# if num % 2 == 0 :
#     print("Tegsh")
# else :
#     print("Sondgoi")


# 1.3
# a,b = map(int, input("2 too :").split())
# if a == b :
#     print("Tentsuu")
# elif a > b :
#     print(a)
# else :
#     print(b)




# 1.4
# day = int(input("Too :"))
# if day == 1 :
#     print("Monday")
# elif day == 2 :
#     print("Tuesday")
# elif day == 3 :
#     print("Wednesday")
# elif day == 4 :
#     print("Thursday")
# elif day == 5 :
#     print("Friday")
# elif day == 6 :
#     print("Saturday")
# elif day == 7 :
#     print("Sunday")
# else :
#     print("tiim ym baihguie")



# 1.5
# km = int(input("Km :"))
# hour = int(input("Tsagaa :"))
# if hour >= 6 and hour <= 21 :
#     if km == 2 or km == 1 :
#         une = 3000
#         print(une)
#     else :
#         une = 1500
#         print(une * km)
# else :
#     une = 1500 
#     total = km * une
#     nemegdel = total * 20 / 100
#     a = total + nemegdel
#     print(a)



# 1.6
# kwt = int(input("Toogoo"))
# if kwt <= 150 :
#     a = kwt * 100
# elif kwt <= 300 :
#     a = (150 * 100) + ((kwt * 150) * 150)
# else :
#     a = (150 * 100 + 150 * 150 + (kwt - 300) * 200)
# print(a)




# 1.7
# username = input("Username:")
# password = input("Password : ")
# is_blocked = False
# failed_attempts = 0
# if is_blocked:
#     print("Таны эрх хаагдсан байна")
# elif username == "" or password == "":
#     print("Мэдээллээ бүрэн оруулна уу")
# elif username != "admin":
#     print("Хэрэглэгч олдсонгүй")
# elif password != "1234":
#     failed_attempts += 1
#     if failed_attempts >= 2:
#         is_blocked = True
#         print("Эрх хаагдлаа")
#     else:
#         print("Нууц үг буруу")
#         password = input("Нууц үгээ дахин оруулна уу: ")
#         if password != "1234":
#             failed_attempts += 1
#             if failed_attempts >= 2:
#                 is_blocked = True
#                 print("Эрх хаагдлаа")
#             else:
#                 print("Нууц үг буруу")
#         else:
#             print("Амжилттай нэвтэрлээ")
# else:
#     print("Амжилттай нэвтэрлээ")



          

# 2.1
# n = int(input("Too :"))
# for i in range(1, n + 1):
#     print(i)



# 2.2
# n = int(input("Too :"))
# a = 0
# for i in range(1, n + 1):
#     if i % 2 == 0 :
#         a += i
# print(a)




# 2.3
# n = int(input("Too :"))
# for i in range(1, 11):
#     print(f"fsdvd{n}*{i}={n*i}")




# 2.4
# mungu=int(input("munguu oruul: "))
# jil=0
# while mungu <= 2000000:
#     mungu *= 1.12
#     jil += 1
# print(f"{jil} jil bolno")


# 2.5
# n = int(input("Too"))
# for i in range (2, n):
#     if n % i == 0 :
#         print(i)
#         break
# else :
#     print("Anhnii too")




# 2.6
# n = int(input("Too"))
# for i in range(1, n+1):
#     if i % 3 == 0 :
#         continue
#     print(i, end = " ")



# 2.7
# n = int(input("Too"))
# for i in range(1, n+1):
#     for j in range(i):
#         print(end = " * ")
#     print()





# 2.8
# secret = int(input("Nuuts too :"))
# count = 0

# for i in range(5):
#     find = int(input("Taah too :"))
#     count += 1
#     if secret < find:
#         print("Ih baina")
#     elif secret > find:
#         print("Baga baina")
#     else:
#         print(f"{count} oroldlogoor taalaa!")
#         break
# else:
#     print(f"Oroldlogo duuslaa. Nuuts too {secret} bailaa.")




# 2.9
# n = int(input())
# while n >= 10:
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     n = sum
# print(n)





# 3.1
# a = list(map(int, input("Toonuud").split()))
# total = 0
# total1 = 0
# for i in a :
#     total += i
#     total1 += 1
# print(total, (total / total1))



# 3.2
# nums = list(map(int, input("Toonuud").split()))
# high = 0
# for i in nums:
#     if i > high :
#         high = i
# b = nums.index(high)
# print(high, b)




# 3.3
# names = input().split()
# find = input()
# if find in names :
#     print(f"Oldloo, {names.index(find)}")
# else:
#     print("Baihgui")



# 3.4
# price = list(map(int, input("Unenuudee oruul :").split()))
# sales = []
# for i in price :
#     a = i * 0.9
#     b = int(a)
#     sales.append(b)
# print(f"{price}->{sales}")



# 3.5
# scores = list(map(int, input("Onoonuudaa :").split()))
# a = []
# for i in scores :
#     if i >= 60 :
#         a.append(i)
# print(f"{scores}, {a}")




# 3.6
# prices = list(map(int, input("Unenuud :").split()))
# c = []
# for i in prices :
#     if i > 5000 :
#         c.append(i)
# print(f"{prices}, Niit dun ni : {sum(c)}, hurgelt {len(c)* 2000}.")



# # 3.7
# namess = input().split()
# sub = input().split()
# scores = list(map(int, input("Onoonuudaa :").split()))




# def linear(l, t):
#     for i in enumerate(len(l)):
#         if l[i] == t :
#             return i
#     return -1
# l = list(map(int, input().split()))
# t = int(input())
# r = linear(l,t)
# print(r)


def lenear(l, t):
    for x, i in enumerate(l):
        if i == t :
            return x
    return -1
l = list(map(int, input().split()))
t = int(input())
print(lenear(l))
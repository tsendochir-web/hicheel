# 1
# for i in range(5):
#     print("Sainuu")


# 2
# for i in range(10):
#     print(i)


# 3
# for i in range(1, 11):
#     print(i)


# 4
# for i in range(10, 0, -1):
#     print(i)


# 5
# name = input("Ner")
# for i in range(5):
#     print(name)


# 6
# a = 0
# for i in range(1, 11):
#     a += i
# print(a)



# 7
# a = 0
# for i in  range(1, 101):
#     a += i
# print(a)



# 8
# a = 0
# for i in range(0, 21, 2):
#     a += i
# print(a)



# 9
# a = 0
# for i in range(0, 31, 3):
#     a += i
# print(a)



# 10
# a = int(input("5g ogno"))
# for i in range(a):
#     a += i
# print(a)



# 11
# a = 0
# for i in range(1, 21):
#     if i % 2 == 0 :
#         a += 1
# print(a)



# 12
# a = 0 
# for i in range(1, 101):
#     if i % 5 == 0 :
#         a += 1
# print(a)



# 13
# a = 0
# for i in range(1, 51):
#     if i % 3 == 0 :
#         a += 1
# print(a)



# 14
# a = 0
# b = 0
# for i in range(1, 21):
#     if i % 2 == 0 :
#         a += 1
#     if i % 2 != 0 :
#         b += 1
# print(a, b)



# 15
# b = 0
# a = int(input("ogogdson too 50"))
# for i in range(1, a):
#     if i % 7 == 0 :
#         b += 1
# print(b)



# 16
# a = 0
# b = 0
# for i in range(1, 101):
#     if i % 2 == 0 :
#         a += i
#         b += 1
# print(a, b)



# 17
# a = 0
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0 :
#         a += 1
# print(a)



# 18
# a = 0
# for i in range(1, 101):
#     if i % 3 == 0 :
#         a += i
# print(a)




# 19


# total = 0
# a = 0
# n = int(input("Heden suragchiin dun oroh we? : "))
# for i in range(n):
#     score = int(input("Dun : "))
#     total += score
#     if score >= 80:
#         a += 1
# dundaj = total / n
# print(f"Niilber : {total}\nDundaj : {dundaj}\n80-aas deesh : {a}")




# 20
# high = 0
# n = int(input("Heden suragchiin dun oroh we? : "))
# for i in range(n):
#     scores = int(input("Dun :"))
#     if  high < scores :
#         high = scores
# print(high)


# 21

# n = int(input("Heden too oroh we? : "))
# low = int(input("Too: "))
# for i in range(n - 1):
#     scores = int(input("Too: "))
#     if scores < low:
#         low = scores
# print(low)




# 22
# total = 0
# num = int(input("Too :"))
# for i in range(10):
#     digit = num % 10
#     total += digit
#     num //= 10
# print(total)



# 23
# total = 1
# n = int(input("Too :"))
# for i in range(1, n + 1):
#     total *= i
# print(total)



# 24
# total = 0
# n = int(input("Too :"))
# for i in range(1, n):
#     if n % i == 0:
#         total += i
# if total == n :
#     print("yes")
# else :
#     print("no")
    


# 25

# n = int(input("Too: "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("YES")
# else:
#     print("NO")




# 26
# total1 = 0
# total2 = 0
# total3 = 0
# for i in range (1, 101):
#     if i % 2 == 0 :
#         total1 +=1
#     elif i % 3 == 0:
#         total2 +=1
#     elif i % 5 == 0 :
#         total3 += 1
# print(f"2d huwaagdah ni : {total1}\n3d huwaagdah ni : {total2}\n5d huwaagdah ni : {total3}")




# 27
# for i in range(1, 31):
#     if i % 2 == 0 :    
#         print("2d huwaagdana", i)
#     else :
#         print("2d huwaagdahgui", i)




# 28
# total = 0
# count = 0
# for i in range(1, 101):
#     if i % 5 == 0 :
#         total += i
#         count += 1
# print(f"Too : {count}\nNiilber : {total}")




# 29
# n = int(input("Heden too :"))
# total = 0
# count = 0
# ave = 0
# for i in range(n):
#     num = int(input("Too :"))
#     total += num
#     count += 1
#     ave = total / n
# print(f"Niilber : {total}\nShirheg : {count}\nDundaj : {ave}")




# 30
# n = int(input("Too :"))
# even = 0
# even_total = 0
# odd = 0 
# odd_total = 0
# high = 1
# low = 1
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even += 1
#         even_total +=i
#     else :
#         odd += 1
#         odd_total +=i
#     if i > high :
#         high = i
#     if i < low:
#         low = i
# print(f"Tegsh toonuud : {even}\nTegsh toonuudiin niilber : {even_total}\nSondgoi toonuud : {odd}\nSondgoi toonuudiin niilber : {odd_total}\nHamgiin ih : {high}\nHamgiin baga ni : {low}")
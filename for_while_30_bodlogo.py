# 1
# for i in range(1, 11):
#     print(i)




# 2
# for i in range(1, 21):
#     if i % 2 == 0 :
#         print(i)



# 3
# for i in range(1, 21):
#     if i % 2 == 1 :
#         print(i)




# 4
# for i in range(1, 11):
#     print("5 x", i, "=", 5 * i)



# 5
# n = int(input("Too :")) 
# for i in range(1, n + 1):
#     print(i)



# 6
# n = int(input("Too : "))
# for i in range(n, 0, -1):
#     print(i)



# 7
# for i in range(1, 51):
#     if i % 3 == 0 :
#         print(i)



# 8
# for i in range(1, 31):
#     if i % 5 != 0 :
#         print(i)




# 9
# count = 0
# for i in range(1, 101):
#     if i % 2 == 0 :
#         count += 1
# print(count)




# 10
# count = 0 
# for i in range(1, 101):
#     if i % 7 == 0 :
#         count += 1
# print(count)




# 11
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)



# 12
# total = 0
# for i in range(1, 51):
#     if i % 2 == 0 :
#         total += i 
# print(total)





# 13
# i = 1 
# while i < 11 :
#     print(i)
#     i += 1



# 14
# i = 10
# while i > 0:
#     print(i)
#     i -= 1



# 15
# i = 2
# while i <= 20:
#     print(i)
#     i += 2



# 16
# n = int(input("Too :"))
# i = 1 
# total = 0
# while i <= n :
#     total += i
#     i +=1
# print(total)




# 17
# n = int(input("Too: "))
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1
# print(count)



# 18
# n = int(input("Too: "))
# total = 0
# while n > 0:
#     a = n % 10
#     total += a
#     n = n // 10
# print(total)




# 19
# for i in range(1, 21):
#     if i == 5:
#         break
#     print(i)




# 20
# for i in range(10, 101):
#     if i % 7 == 0:
#         print(i)
#         break





# 21
# secret = int(input("Nuuts too :"))
# while True:
#     n = int(input("Too taana uu: "))
#     if n == secret:
#         print("Zov taalaa!")
#         break




# 22
# while True:
#     n = int(input("Too oruul: "))
#     if n == 0:
#         break
# print("Zogsloo")




# 23
# total = 0
# while True:
#     n = int(input("Too oruul: "))
#     if n == 0:
#         break
#     total += n
# print(total)



# 24
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)




# 25
# for i in range(1, 21):
#     if i % 2 == 0 :
#         continue
#     print(i)



# 26
# for i in range(1, 31):
#     if i % 3 == 0 :
#         continue
#     print(i)




# 27
# total = 0
# for i in range(5):
#     n = int(input("Too oruul: "))
#     if n < 0:
#         continue
#     total += n
# print(total)



# 28
# i = 1
# count = 0
# while True:
#     if i % 7 == 0:
#         print(i)
#         count += 1

#     if count == 5:
#         break
#     i += 1




# 29
# while True:
#     n = int(input("Too oruul: "))

#     if n == 0:
#         break

#     if n < 0:
#         continue

#     if n % 2 != 0:
#         continue

#     print(n)




# 30
# secret = int(input("Nuuts too :"))
# while True:
#     n = int(input("Too taana uu : "))
#     if n < 0:
#         print("Sorog too oruulahgui")
#         continue
#     if n < secret:
#         print("Baga baina")
#     elif n > secret:
#         print("Ih baina")
#     else:
#         print("Zow taalaa!")
#         break
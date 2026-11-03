# 1
# n = int(input())
# i = 1
# while i <= n:
#     print(i)
#     i += 1


# 2
# n = int(input()) 
# i = 1
# while n >= i:
#     print(n)
#     n -= 1 



# 3
# n = int(input())
# i = 0
# while i <= n:
#     print(i)
#     i += 2




# 4
# n = int(input())
# i = 1
# while i <= n:
#     print(i)
#     i += 2




# 5
# n = int(input())
# i = 1
# a = 0
# while i <= n:
#     a += i
# print(a)




# 6
# n = int(input())
# i = 1
# a = 0
# while i <= n:
#     if i % 2 == 0:
#         a += i
#     i += 1
# print(a)





# 7
# n = int(input())
# i = 0
# while i <= n:
#     print(i)
#     i += 3




# 8
# n = int(input())
# i = 1
# eyreg = 0
# sorog = 0
# zero = 0
# while i <= n:
#     too = int(input())
#     if too > 0:
#         eyreg += 1
#     elif too < 0:
#         sorog += 1
#     else :
#         zero += 1
#     i += 1
# print("eyreg:", eyreg)
# print("sorog:", sorog)
# print("zero:", zero)







# 9
# n = int(input())
# i = 1
# eyreg = 0
# while i <= n:
#     too = int(input())
#     if too > 0:
#         eyreg += too
#     i += 1
# print(eyreg)





# 10
# n = int(input())
# i = 1
# high = 0
# while i <= n:
#     too = int(input())
#     if too > high :
#         high = too 
#     i += 1
# print(high)



# 11
# n = int(input())
# i = 1
# low = int(input())
# while i < n:
#     too = int(input())
#     if too < low:
#         low = too
#     i += 1
# print(low)




# 12
# n = int(input())
# i = 1
# while i <= n :
#     if i % 3 == 0 and i % 5 == 0 :
#         print(i)
#     else :
#         print("Baihguie")
#     i += 1




# 13
# n = int(input())
# count = 0
# while n > 0:
#     n //= 10
#     count += 1
# print(count)




# 14
# n = int(input())
# total = 0
# while n > 0:
#     a = n % 10
#     total += a
#     n //= 10
# print(total)




# 15
# n = int(input("Too oruul: "))
# a = 0
# while n > 0:
#     b = n % 10
#     a = a * 10 + b
#     n = n // 10
# print(a)




# 16
# n = int(input("Too oruul: "))
# original = n
# a = 0
# while n > 0:
#     b = n % 10
#     a = a * 10 + b
#     n = n // 10
# if original == a:
#     print("Yes")
# else:
#     print("No")




# 17
# n = int(input("Too oruul: "))
# i = 2
# count = 0
# while i < n:
#     if n % i == 0:
#         count += 1
#     i += 1
# if n > 1 and count == 0:
#     print("Anhnii too")
# else:
#     print("Anhnii too bish")



# 18
# n = int(input(" too oruul: "))
# i = 2
# while i <= n:
#     j = 2
#     count = 0
#     while j < i:
#         if i % j == 0:
#             count += 1
#         j += 1
#     if count == 0:
#         print(i)
#     i += 1




# 19
# n = int(input("Too oruul: "))
# i = 1

# while i <= 10:
#     print(n, "*", i, "=", n * i)
#     i += 1




# 20
# password = input("Nuuts ug oruul: ")
# while password != "python123":
#     print("Buruu nuuts ug!")
#     password = input("Dahin oruul: ")
# print("Amjilttai nevterlee!")
# nums = list(map(int, input().split()))
# for i in range(len(nums) -1):
#     a = i
#     for j in range(i + 1, nums):
#         if nums[j] < nums[a]:
#             a = j
#     nums[i], nums[a] = nums[a], nums[i]
# print(nums)


# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) // 2
#     left = nums[:mid]
#     right = nums[mid:]
#     left = merge_sort(left)
#     right = merge_sort(right)
#     i = 0
#     j = 0
#     result = []
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else :
#             result.append(right[j])
#             j += 1

#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result 
# nums = list(map(int, input().split()))
# print(merge_sort(nums))






# 1
# num = int(input("Too :"))
# if num > 0 and num % 2 == 0 :
#     print("Eyreg, tegsh")
# elif num > 0 and num % 2 != 0 :
#     print("Eyereg sondgoi")
# elif num < 0 and num % 2 != 0 :
#     print("Sorog, sondgoi")
# elif num < 0 and num % 2 == 0 :
#     print("Sorog, tegsh")
# else :
#     print("Teg")




# 2
# score = int(input("Onoo : "))
# while score > 100 or score < 0:
#     print("Buruu onoo")
#     score = int(input("Dahin onoo oruul: "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")





# 3

# year = int(input("Jil: "))

# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("Ondor jil")
# else:
#     print("Engiin jil")



# 4
# a, b, c = map(int, input("Taluud :").split())
# if a + b <= c or b + c <= a or a + c <= b:
#     print("Gurwaljin uusehgui")
# elif a == b == c:
#     print("Tegsh talt")
# elif a == b or b == c or a == c:
#     print("Adil hajuut")
# else:
#     print("Ymar neg gurwaljin")



# 5
# km = int(input("Km :"))
# hour = int(input("Tsag :"))




# 6
# num = int(input("Too :"))
# total = 0
# for i in range(num + 1):
#     if i % 2 == 0 :
#         total += i
# print(total)




# 7
# num = int(input("Too :"))
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
# print(total)



# 8##########################
# num = int(input("Too: "))
# urwuu = 0
# while num > 0:
#     digit = num % 10
#     urwuu = urwuu * 10 + digit
#     num //= 10
# print(urwuu)





# 9
# n = int(input("Too: "))
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizfaz", end=" ")
#     elif i % 3 == 0:
#         print("fiz", end=" ")
#     elif i % 5 == 0:
#         print("faz", end=" ")
#     else:
#         print(i, end=" ")



# 10
secret = int(input("Nuuts too: "))
count = 0
while count < 5:
    find = int(input("Taah too: "))
    count += 1

    if find > secret:
        print("Ih baina")
    elif find < secret:
        print("Baga baina")
    else:
        print(f"{count} oroldlogoor zow taalaa")
        break
else:
    print(f"Oroldlogo duuslaa. Nuuts too: {secret}")
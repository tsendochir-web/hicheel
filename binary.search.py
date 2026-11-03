# lst = [1, 2, 3, 4, 5, 6]
# target = int(input())
# left = 0
# right = len(lst)-1
# while left <= right:
#     mid = (right+left)//2
#     if lst[mid] == target :
#         print("oldsn")
#         break
#     elif lst[mid] < target :
#         left = mid + 1
#     else :
#         right = mid + 1

\


# 1
# def binary_search(lst, t):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if lst[mid] == t :
#             print("Oldson")
#             break
#         elif lst[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
#     print("BAihguieeee")
# lst = list(map(int, input("Toonuud :").split()))
# lst.sort()
# t = int(input("Too :"))
# binary_search(lst, t)


# 2
# def binary_search(lst, t):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if lst[mid] == t :
#             return mid
#         elif lst[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
#     return -1
# lst = list(map(int, input("Toonuud :").split()))
# lst.sort()
# t = int(input("Too :"))
# print(binary_search(lst, t))


# 3
# def binary_search(lst, t):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if lst[mid] == t :
#             print(mid)
#             break
#         elif lst[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
# lst = list(map(int, input("Toonuud :").split()))
# lst.sort()
# t = int(input("Too :"))
# binary_search(lst, t)



# 4
# def binary_search(lst, t):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if lst[mid] == t :
#             print(mid)
#             break
#         elif lst[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
# lst = list(map(int, input("Toonuud :").split()))
# lst.sort()
# t = int(input("Haih too :"))
# binary_search(lst, t)


# 5
# def binary_search(lst, t):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if lst[mid] == t :
#            return "oldson"
#         elif lst[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
#     return "BAihguieeee"
# lst = list(map(int, input("Toonuud :").split()))
# lst.sort()
# t = int(input("Too :"))
# print(binary_search(lst, t))




# 6
# def binary_search(lst, t):
#     count = 0
#     l = 0
#     r = len(lst) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         count += 1
#         if lst[mid] == t:
#             return count
#         elif lst[mid] < t:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return -1
# lst = list(map(int, input("Toonuud: ").split()))
# lst.sort()
# t = int(input("Too: "))
# print(binary_search(lst, t))



# 7
# def binary_search(scores, t) :
#     l = 0
#     r = len(scores)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if scores[mid] == t :
#             return mid
#         elif scores[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
#     return "Tiim onoo algaa ho"
# scores = list(map(int, input("Onoonuud :").split()))
# scores.sort()
# t = int(input("Haih onoo :"))
# print(binary_search(scores, t))



# 8
# def binary_search(codes, t):
#     l = 0
#     r = len(codes)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if codes[mid] == t:
#             return "Baraa burtgeltei"
#         elif codes[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
#     return "Baraa burtgelguie ho"
# codes = list(map(int, input("Coduudaa oruul :").split()))
# codes.sort()
# t = int(input("Code :"))
# print(binary_search(codes, t))



# 9
# def binary_search(books, t) :
#     l = 0
#     r = len(books)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if books[mid] == t :
#             return mid
#         elif books[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
#     return "Tiim dugaar algaa"
# books = list(map(int, input("Nomiin dugaaruud :").split()))
# books.sort()
# t = int(input("Haih dugaar :"))
# print(binary_search(books, t))



# 10
# def binary_search(nums, t):
#     l = 0
#     r = len(nums) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         print(l, r, mid)
#         if nums[mid] == t:
#             print(mid)
#             break
#         elif nums[mid] < t:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return "baihgui"
# nums = list(map(int, input("Toonuud: ").split()))
# nums.sort()
# t = int(input("Haih too: "))
# binary_search(nums, t)


# 11
# def binary_search(lst, t):
#     l = 0
#     r = len(lst)-1
#     while l <= r:
#         mid = (l + r) // 2
#         if lst[mid] == t :
#             return mid - 1
#         elif lst[mid] < t :
#             l = mid + 1
#         else :
#             r = mid - 1
#     return -1
# lst = list(map(int, input("Toonuud :").split()))
# lst.sort()
# t = int(input("Too :"))
# print(binary_search(lst, t))


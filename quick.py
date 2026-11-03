# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for num in arr:
#         if num < pivot:
#             left.append(num)
#         elif num == pivot:
#             middle.append(num)
#         else:
#             right.append(num)
#     return quick_sort(left) + middle + quick_sort(right)
# numbers = [8, 3, 1, 7, 0, 10, 2]
# print(quick_sort(numbers))




# 1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr)//2]
#     l = []
#     r = []
#     m = []
#     for num in arr :
#         if num < pivot :
#             l.append(num)
#         elif num == pivot :
#             m.append(num)
#         else :
#             r.append(num)
#     return quick_sort(l) + m + quick_sort(r)
# nums = list(map(int, input("Toonuud :").split()))
# print(quick_sort(nums))





# 2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     m = []
#     l = []
#     r = []
#     for num in arr :
#         if num > pivot :
#             l.append(num)
#         elif num == pivot :
#             m.append(num)
#         else :
#             r.append(num)
#     return quick_sort(l) + m + quick_sort(r)
# nums = list(map(int, input("Toonuud : ").split()))
# print(quick_sort(nums))



# 3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     m = []
#     l = []
#     r = []
#     for num in arr :
#         if num < pivot :
#             l.append(num)
#         elif num == pivot :
#             m.append(num)
#         else :
#             r.append(num)
#     return quick_sort(l) + m + quick_sort(r)
# nums = list(map(int, input("Toonuud : ").split()))
# print(quick_sort(nums))




# # 4
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     m = []
#     l = []
#     r = []
#     for num in arr :
#         if num < pivot :
#             l.append(num)
#         elif num == pivot :
#             m.append(num)
#         else :
#             r.append(num)
#     return quick_sort(l) + m + quick_sort(r)
# nums = list(map(int, input("Toonuud : ").split()))
# print(quick_sort(nums))




# 5
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     m = []
#     l = []
#     r = []
#     for num in arr:
#         if num < pivot :
#             l.append(num)
#         elif num == pivot :
#             m.append(num)
#         else :
#             r.append(num)
#     return quick_sort(l) + m + quick_sort(r)
# nums = list(map(int, input("Toonuud :").split()))
# print(quick_sort(nums)[:3])   




# 6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr 
#     pivot = arr[len(arr) // 2]
#     m = []
#     r = []
#     l = []
#     for num in arr :
#         if num < pivot :
#             l.append(num)
#         elif num == pivot :
#             m.append(num)
#         else :
#             r.append(num)
#     return quick_sort(l) + m + quick_sort(r)
# nums = list(map(int, input("Toonuud :").split()))
# print(quick_sort(nums)[-1: -3: -1 ])




# 7

# def quick_sort(stus):
#     if len(stus) <= 1:
#         return stus
#     pivot = stus[len(stus) // 2][1]
#     m = []
#     r = []
#     l = []
#     for num in stus:
#         if num[1] < pivot:
#             l.append(num)
#         elif num[1] == pivot:
#             m.append(num)
#         else:
#             r.append(num)

#     return quick_sort(l) + m + quick_sort(r)
# stus = []
# n = int(input("Heden suragch: "))
# for i in range(n):
#     name = input("Suragchiin ner: ")
#     score = int(input("Onoo: "))
#     stus.append((name, score))
# print(quick_sort(stus))




# 8
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    m = []
    r = []
    l = []
    for i in arr    :
        if i < pivot :
            l.append(i)
        elif i == pivot :
            m.append(i)
        else :
            r.append(i)
    return quick_sort(l) + m + quick_sort(r)
words = input().split()
print(quick_sort(words))
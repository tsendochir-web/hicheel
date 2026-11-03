# 1
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(nums[1][2])



# 2
# students = [["Bat", 18],
#             ["Sara", 19],
#             ["Bold", 20]
# ]
# print(students[2][0])




# 3
# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# print(nums[1])




# 4
# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# print(nums[2][0])


# 5
# nums = [
#     [5, 10],
#     [15, 20]
# ]
# print(nums[0][0])




# 6
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# print(nums[2][1])



# 7
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for i in nums:
#     print(i)
# print()



# 8
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in range(0, len(nums)) :
#     for j in nums[i]:
#         print(j)



# 9
# nums = [
#      [1, 2, 3],
#      [4, 5, 6]
# ]
# for i in range(0, len(nums)) :
#     for j in nums[i]:
#         print(j, end = " ")



# 10
# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]
# for i in range(0, len(nums)):
#     for j in nums[i] :
#         if j > 10 :
#             print(j)



# 11
# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]
# b = 0
# for i in range(0, len(nums)) :
#     for j in nums[i] :
#         b +=1
# print(b)




# 12
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# b = 0
# for i in range(0, len(nums)) :
#     for j in nums[i] :
#         b += j
# print(b)




# 13
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# b = []
# for i in range(0, len(nums)) :
#     for j in nums[i] :
#         if j % 2 == 0 :
#             print(j, end = " ")



# 14
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# b = 0
# for i in range(0, len(nums)) :
#     for j in nums[i] :
#         if j % 2 != 0 :
#             b += 1
# print(b)




# 15
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]
# b = 0
# for i in range(0, len(nums)) :
#     for j in nums[i] :
#         if j % 2 == 0 :
#             b += j
# print(b)




# 16
# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]
# b = 0
# for i in range(0, len(nums)) :
#     for j in nums[i] :
#         if j > 0 :
#             b += 1
# print(b)




# 17
# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]
# b = 0
# for i in nums :
#     for j in i :
#         if j < 0 :
#             b += j
# print(b)



# 18
# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]
# print(max(max(nums)))




# 19
# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ]
# print(min(min(nums)))




# 20
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in nums :
#     c = sum(i)
#     b = c
#     print(b)




# 21
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums:
#     c = max(i)
#     b = c
#     print(b)




# 22
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums :
#     c = min(i)
#     b = c 
#     print(b)




# 23
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# b = []
# for i in nums :
#     for j in i :
#         b.append(j)
# if 7 in b :
#     print("Yes")
# else:
#     print("No")






# 24
# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]
# target = 2
# a = 0
# for i in nums :
#     for j in i :
#         if j == target :
#             a += 1
# print(a)





# 25
# nums = [
#     [1, 7, 3],
#     [9, 2, 6],
#     [4, 8, 5]
# ]
# b = 0
# for i in nums :
#     for j in i :
#         if j > 5 :
#             b += j
# print(b)





# 26
# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ]
# print(max(nums))





# 27
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# for i in students :
#     for j in i :
#         print(j, end = " ")
#     print()





# 28
# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ]
# for i in students :
#     if int(i[1]) > 18 :
#         print(i[0])




# 29
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80]
# ]
# for ner, * onoo in students :
#     b = sum(onoo)/len(onoo)
#     print(ner, b)




# 30
# total = []
# name = []

# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80],
#     ["Anu", 90, 90, 90]
# ]
# for ner, *onoo in students:
#     b = sum(onoo) / len(onoo)
#     total.append(b)
#     name.append(ner)
# mx = max(total)
# for i in range(len(total)):
#     if total[i] == mx:
#         print(name[i], total[i])
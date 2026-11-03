# 1
# words = input().split()
# print(max(words))



# 2
# a = input()
# b = ""
# count = 1
# for i in range(1, len(a)):
#     if a[i] == a[i-1]:
#         count += 1
#     else:
#         b += a[i-1] + str(count)
#         count = 1
# b += a[-1] + str(count)
# print(b)




# 3
# a = input().split()
# b = []
# for i in a:
#     b.append(i[::-1])
# print(*b)



# 4
# a = input().split()
# v = "aeiou"
# b = 0
# result = ""
# for i in a:
#     count = 0
#     for j in i.lower():
#         if j in v:
#             count += 1
#     if count > b:
#         b = count
#         result = i
# print(result, b)




# 5
# a = input().split()
# if sorted(a[0].lower()) == sorted(a[1].lower()):
#     print("YES")
# else:
#     print("NO")





# 6
# a = input().split()
# b = []
# for i in a:
#     if i not in b and a.count(i) > 1:
#         print(i, a.count(i))
#         b.append(i)




# 7
# a = input()
# b = a.replace(" ", "").lower()
# if b == b[::-1]:
#     print("YES")
# else:
#     print("NO")




# # 8
# a = input().split()
# b = []
# for i in a:
#     for j in i:
#         if j.isdigit():
#             b.append(i)
#             break
# if len(b) > 0:
#     print(*b)
# else:
#     print("NO")





# 9
# a = input()
# upper = False
# lower = False
# digit = False
# special = False
# space = False
# for i in a:
#     if i.isupper():
#         upper = True
#     elif i.islower():
#         lower = True
#     elif i.isdigit():
#         digit = True
#     elif i in "!@#$":
#         special = True
#     elif i == " ":
#         space = True
# if len(a) >= 8 and upper and lower and digit and special and not space:
#     print("STRONG")
# else:
#     print("WEAK")




# a = input().split()
# names = []
# scores = []
# for i in a:
#     b = i.split(":")
#     names.append(b[0])
#     scores.append(int(b[1]))
# high = max(scores)
# avg = round(sum(scores) / len(scores), 1)
# highest = []
# above = []
# failed = []
# for i in range(len(scores)):
#     if scores[i] == high:
#         highest.append(names[i])

#     if scores[i] > avg:
#         above.append(names[i])
#     if scores[i] < 60:
#         failed.append(names[i])
# print("Highest:", *highest)
# print("Average:", avg)
# print("Above average:", *above)
# print("Failed:", *failed)
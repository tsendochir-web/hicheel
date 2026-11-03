1
# a = input().split()
# print(len(a))



# 2
# a = input().lower()
# b = 0
# for i in a :
#     if i == 'а' or i == 'э' or i == 'и' or i == 'о' or i == 'у' or i == 'ө' or i == 'ү':
#         b += 1
# print(b)



# 3
# a = input().split()
# b = input()
# c = 0
# for i in a :
#     if i == b :
#         c += 1
# print(c)



# 4
# a = input()
# b = a.split()
# print(max(a))



# 5
# a = input().split()
# a.sort()
# b = ' '.join(a)
# print(b)




# 6
# a = input().split()
# for i in a:
#     if i == i[::-1]:
#         print(i, end = " ")




# 7
# a = input().split()
# for a in a :
#     print(a, len(a), end = " ")




# 8
# a = input()
# b = input()
# print(a.count(b))




# 9 
# a = input().split()
# b = []
# for i in a :
#     if i not in b :
#         b.append(i)
# print(*b)



# 10
# a = input("Suragchiin ner bolon onoo : ").split()
# names = []
# scores = []
# for i in a:
#     b = i.split(":")
#     names.append(b[0])
#     scores.append(int(b[1]))
# high = max(scores)
# for i in range(len(scores)):
#     if scores[i] == high:
#         print(names[i], high, end=" ")
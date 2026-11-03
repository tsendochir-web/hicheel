# 1
# name = input()
# print("Sainuu", name)




# 2
# a = int(input("Too : "))
# b = a = int(input("Too : "))
# print(a + b)




# 3
# a = float(input("Too :"))
# print("Niit une : ", a * 2)



# 4
# a = 42
# b = "42"
# print(type(a))
# print(type(b))



# 5
# a = input()
# a.split()
# print(len(a))




# 6
# a = input("Ug : ")
# print(a [0])
# print(a [-1])





# 7
# n = int(input("Too :"))
# for i in range(1, n + 1) :
#     print(i)




# 8
# a = map(int, input("too ug").split())
# print(sum(a))




# 9
# a = list(map(int, input().split()))
# print(min(a), max(a))





# 10
# a = list(map(int, input().split()))
# b = sum(a)/len(a)
# print(round(b, 2))





# 11
# a = ["cat", "dog"]
# a.append("tiger")
# print(a)




# 12
# a = ["cat", "tiger"]
# a.insert(1, "dog")
# print(a)




# 13
# a = input().split()
# b = input()
# a.remove(b)
# print(a)




# 14
# a = input().split()
# b = int(input())
# deleted = a.pop(b)
# print(deleted)
# print(",".join(a))




# 15
# a = list(map(int, input().split()))
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)




# 16
# a = list(map(int, input().split()))
# print(a[::-1])




# 17
# a = input("Ug : ")
# print(f"[{a.strip()}]")
# print(f"[{a.lstrip()}]")
# print(f"[{a.rstrip()}]")    






# 18
# a = input().split()
# print(len(a))





# 19
# a = input().lower()
# b = input()
# print(a.count(b))





# 20
# a = input()
# b = input()
# c = a.find(b)
# print(c)
# if b in a:
#     print(a.index(b))
# else :
#     print("Oldoogui")





# 21
# a = input().split()
# for i in a :
#     if i.startswith("report") and i.endswith(".pdf") :
#         print(i)
# if i == 0 :
#     print("Oldohgui")





# 22
# a = input("Oguulber : ")
# b = input("SOlih ug :")
# c = input("Oruulah ug : ")
# print(a.replace(b,c))





# 23
# a = input().lower().split()
# b = input().lower()
# if b in a :
#     print("Yes")
# else :
#     print("No")





# 24
# a = input("Ug : ")
# print(a[:3])
# print(a[-3::])






# 25
# a = input().strip()
# b = a.lower()
# if b == b[::-1]:
#     print("Yes")
# else : 
#     print("No")






# 26
# a = list(input().split())
# b = [0]
# for i in a :
#     if len(i) > len(b) :
#         b = i
# print(b)





# 27
# a, b, c = input().split()
# a.strip()
# b.strip()
# c.strip()
# m = int(b) + 1
# print(a, "|Ireh jil : ", str(m), "|", c )    





# 28
# a = input().lower().split()
# b = []
# for a in a :
#     if a not in b :
#         b.append(a)
#         b.sort()
# print(" ".join(b))




# 29
# a = map(int, input().split())
# b = []
# for i in a :
#     if i not in b :
#         b.append(i)
# b.sort()
# print(b[-2])




# n = int(input("Heden suragch : "))
# names = []
# scores = []
# for i in range(n):
#     a = input("Ner, onoo : ").strip().split(",")
#     names.append(a[0].strip())
#     scores.append(int(a[1].strip()))
# avg = round(sum(scores) / len(scores), 2)
# high = max(scores)
# index = scores.index(high)
# high_name = names[index]
# names.sort()
# print(avg)
# print(high_name)
# print(" ".join(names))
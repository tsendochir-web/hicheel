# 1
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i == t :
#             return "Oldloo"
#     return "Oldsongui"
# l = list(map(int, input().split()))
# t = int(input())
# print(lenear(l, t))



# 2
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i == t :
#             return x
#     return -1
# l = list(map(int, input().split()))
# t = int(input())
# print(lenear(l, t))




# 3
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i == t :
#             return x
#     return -1
# l = list(map(int, input().split()))
# t = int(input())
# print(lenear(l, t))



# 4
# def linear(l, t):
#     count = 0
#     for i in l:          
#         if i == t:       
#             count += 1   
#     return count
# l = list(map(int, input().split()))
# t = int(input())
# print(linear(l, t))






# 5
# def lenear(l, t):
#     for i in range(len(l)):
#         if l[i] == t:
#             last = i
#     return last
# l = list(map(int, input().split()))
# t = int(input())
# print(lenear(l, t))
        



# 6
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i == t :
#             return x
#     return "Oldsonguie ho"
# l = input().split()
# t = input()
# print(lenear(l, t))





# 7
# def lenear(l):
#     for x, i in enumerate(l):
#         if i >= 0 :
#             return x
#     return - 1
# l = map(int, input().split())
# print(lenear(l))






# 8
# def lenear(l):
#     for x, i in enumerate(l):
#         if i > 15:
#             x = i
#             return x
#     return -1
# l = map(int,input().split())
# print(lenear(l)) 


# 9
# def lenear(stu, t):
#     for i in stu:
#         if i[0] == t:   
#             return i[1] 
#     return -1           
# stu = []
# n = int(input("Хэдэн сурагч: "))
# for i in range(n):
#     name = input("Нэр: ")
#     age = int(input("Нас: "))
#     stu.append([name, age])
# t = input("Хайх нэр: ")
# print(lenear(stu, t))





# 1
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i == t :
#             return x
#     return "Oldsongui"
# l = input().split()
# # t = input())
# print(lenear(l, t))



# 2
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i == t :
#             return "Oldloo"
#     return "Oldsongui"
# l = list(map(int, input().split()))
# t = int(input())
# print(lenear(l, t))




# 3
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i == t :
#             return x
#     return -1
# l = list(map(int, input().split()))
# t = int(input())
# print(lenear(l, t))




# 4
# def linear(l, t):
#     count = 0
#     for i in l:          
#         if i == t:       
#             count += 1   
#     return count
# l = list(map(int, input().split()))
# t = int(input())
# print(linear(l, t))




# 5
# def lenear(l, t):
#     last = -1
#     for i in range(len(l)):
#         if l[i] == t:
#             last = i
#     if last == -1 :
#         return "Oldsongui"
#     return last
# l = list(map(int, input().split()))
# t = int(input())
# print(lenear(l, t))
        


# 6
# def lenear(stu, t):
#     for i in stu:
#         if i[0] == t:   
#             return i[1] 
#     return -1           
# stu = []
# n = int(input("Хэдэн сурагч: "))
# for i in range(n):
#     name = input("Нэр: ")
#     age = int(input("Нас: "))
#     stu.append([name, age])
# t = input("Хайх нэр: ")
# print(lenear(stu, t))



# 1
# def lenear(l) :
#     for x, i in enumerate(l):
#         if i % 2 != 0 :
#             return x
# l = list(map(int, input().split()))
# print(lenear(l))




# 2
# def lenear(l):
#     for x, i in enumerate(l):
#         if i > 10 : 
#             return "Oldloo"
#     return "Oldsngui"        
# l = list(map(int,input().split()))
# print(lenear(l))



# 3
# def lenear(l):
#     for x, i in enumerate(l):
#         if i == 0 :
#             return x
#     return -1
# l = list(map(int,input().split()))
# print(lenear(l))



# 4
# def lenear(l):
#     for x, i in enumerate(l):
#         if i > 5 :
#             x = i 
#             return x
#     return -1
# l = list(map(int, input().split()))
# print(lenear(l))




# 5
# def lenear(l):
#     count = 0
#     for i in l:
#         if i < 0 :
#             count += 1
#     return count
# l = list(map(int, input().split()))
# print(lenear(l))



# 6
# def lenear(l, t):
#     for x, i in enumerate(l):
#         if i < t :
#             x = i
#             return x
#     return -1
# l = list(map(int, input("Toonuud :").split()))
# t = int(input("Too :"))
# print(lenear(l, t))




# 7
# def lenear(l):
#     for x, i in enumerate(l):
#         if i % 2 == 0:
#             x = i
#             return x 
#     return -1
# l = list(map(int, input("Toonuud :").split()))
# print(lenear(l))



# 8
# def lenear(l):
#     for x, i in enumerate(l):
#         if i > 15 :
#             if i % 2 != 0 :
#                 return x
#     return - 1
# l = list(map(int, input("Toonuud :").split()))
# print(lenear(l))



# 9
# def lenear(stu):
#     for i in stu :
#         if i[1] > 80 :
#             return i[0]
#     return -1
# n = int(input("Heden suragch :"))
# stu = []
# for i in range(n):
#     name = input("Ner :")
#     score = int(input("Onoogoo :"))
#     stu.append([name, score])
# print(lenear(stu))




# 10
# def lenear(l):
#     last = 1
#     for x, i in enumerate(l):
#         if i % 2 != 0 :
#             last = x 
#     return last
# l = list(map(int, input("Toonuudaa :").split()))
# print(lenear(l))




# 11
# def linear(l, t):
#     a = []
#     for x, i in enumerate(l):
#         if i == t :
#             a.append(x)
#     return a
# l = list(map(int, input("Toonuudaa :").split()))
# t = int(input())
# print(linear(l, t))



# 12
# def linear(stu, find):
#     for name, score in stu:
#         if name == find:
#             if score >= 60:
#                 return "Tentssen"
#             else:
#                 return "Tentseegui"
#     return "Oldsongui"
# n = int(input("Heden suragch: "))
# stu = []
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     stu.append([name, score])
# find = input("Haih ner: ")
# print(linear(stu, find))

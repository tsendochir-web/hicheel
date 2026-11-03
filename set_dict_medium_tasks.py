# 1
# user1 = set(input("Nernuud :").split())
# user2 = set(input("Nernuud :").split())
# print(user1 & user2)




# 2
# players = set(input("Nernuud :").split())
# played = set(input("Nernuud :").split())
# print(players | played)





# 3
# team_a = set(input("Nernuud :").split())
# team_b = set(input("Nernuud :").split())
# print(team_a - team_b | team_b - team_a)




# 4
# known = set(input("Helnuud :").split())
# required = set(input("Heregtei helnuud :").split())
# print(required - known)




# 5
# subjects = set()
# n = int(input("Heden hicheel :"))
# for i in range(n):
#     name = input("Hicheeliin ner :")
#     subjects.add(name)
# a = len(subjects)
# print(f"{a}\n{subjects}")




# 6
# password = input("Password: ")
# let = set()
# nums = set()
# for i in password:
#     if i.isalpha():
#         let.add(i)
#     elif i.isdigit():
#         nums.add(i)
# print(f"Useg : {len(let)}\nToo : {len(nums)}")




# 7
# n = int(input("Heden ug? :"))
# s = set()
# for i in range(n):
#     word = input("Ug :")

#     for char in word:
#         s.add(char)
# print(len(s))





# 8
# stu = {}
# n = int(input("Heden suragch? :"))
# for i in range(n):
#     name = input("Ner :")
#     score = int(input("Onoo :"))
#     stu[name] = score
# for k, v in stu.items():
#     if v >= 90:
#         print(k, "- Excellent")
#     elif v >= 60:
#         print(k, "- Pass")
#     else:
#         print(k, "- Fail")





# 9
# products = {}
# n = int(input("Heden baraa? :"))
# for i in range(n):
#     name = input("Baraanii ner : ")
#     price = int(input("Baraanii une :"))
#     products[name] = price
# a = input("Awah baraa :")
# b = int(input("Shirheg ni :"))
# for k, v in products.items():
#     if a == k:
#         total = v * b
#         print("Total:", total)
#     else :
#         print("Baraa oldsongui")





# 10
# sales = {}
# n = int(input("Heden baraa :"))
# high = 0
# for i in range(n):
#     name = input("Baraanii ner :")
#     quantity = int(input("Heden shirheg zaragdsan ni :"))
#     sales[name]=quantity
# for k,v in sales.items():
#     if v > high :
#         high = v
#         print(k, high)






# 11
# employees = {}
# n = int(input("Heden ajilchin? :"))
# for i in range(n):
#     name = input("Ajilchnii ner :")
#     salary = int(input("Tsalin :"))
#     employees[name] = salary
# for k, v in employees.items():
#     if v < 1500000:
#         v = v + (v * 10 / 100)
#     print(k, v)




#  12
# people = {}
# n = int(input("Heden hun? :"))
# for i in range(n):
#     name = input("Ner :")
#     age = int(input("Nas :"))
#     people[name]=age
# for k,v in people.items():
#     if v >= 18:
#         print(k, v)





# 13
# scores = {}
# n = int(input("Heden suragch? :"))
# for i in range(n):
#     name = input("Ner :")
#     score = int(input("Onoo :"))
#     while score > 100 or score < 0:
#         score = int(input("Onoogoo zow og :"))
#     scores[name] = score
# for k, v in scores.items():
#     v += 5
#     print(k, v)




# 14
# products = {}
# n = int(input("Heden baraa :"))
# for i in range(n):
#     name = input("Baraanii ner :")
#     price = int(input("Baraanii une :"))
#     products[name]=price
# for k,v in products.items():
#     if v >= 100000:
#         print(k)





# 15
# stus = {}
# n = int(input("Heden suragch :"))
# for i in range(n):
#     name = input("Ner :")
#     city = input("Hotiin ner :")
#     stus[name]=city
# a = set()
# city = input("Shalgah hot :")
# for k,v in stus.items():
#     if city == v :
#         a.add(k)
# print(a)






# 16
# games = {}
# n = int(input("Heden hun? :"))
# for i in range(n):
#     name = input("Ner :")
#     game = input("Togloomuudiin ner :")
#     games[name]=game
# game = input("Haih togloomiin ner :")
# a = set()
# for k,v in games.items():
#     if game in v:
#         a.add(k)
# print(a)





# 17
# games = {}
# n = int(input("Heden hun? :"))
# for i in range(n):
#     name = input("Ner :")
#     game = input("Togloomuudiin ner :").split()
#     games[name] = game
# a = set()
# for k, v in games.items():
#     for j in v:
#         a.add(j)
# print(a)





# 18
# games = {}
# n = int(input("Heden hun? :"))
# for i in range(n):
#     name = input("Ner :")
#     game = input("Togloomuudiin ner :").split()
#     games[name] = game
# game = input("Haih togloomiin ner :")
# game2 = input("2dahi togloomiin ner :")
# a = set()
# for k, v in games.items():
#     if game in v and game2 in v:
#         a.add(k)
# print(a)







# 19
# skills = {}
# n = int(input("Heden suragch :"))
# for i in range(n):
#     name = input("Ner :")
#     less = input("Hicheeliin nernuud :").split()
#     skills[name]=less
# less1 = input("Shalgah hicheeliin ner :")
# less2 = input("2 dahi shalgah hicheeliin ner :")
# a = set()
# for k,v in skills.items():
#     if less1 in v and less2 in v:
#         a.add(k)
# print(a)





# 20
# employees = {}
# n = int(input("Heden ajilchin :"))
# for i in range(n):
#     name = input("Ner :")
#     lan = input("Meddeg helnuud :").split()
#     employees[name]=lan
# lan1 = input("Shalgah hel :")
# lan2 = input("2dahi shalgah hel :")
# a = set()
# for k,v in employees.items():
#     if lan1 in v and lan2 not in v:
#         a.add(k)
# print(a)





# 21
# web_users = set()
# mobile_users = set()
# n = int(input("Web usersiin too: "))
# for i in range(n):
#     name = input("Ner: ")
#     web_users.add(name)
# m = int(input("Mobile usersiin too: "))
# for i in range(m):
#     name = input("Ner: ")
#     mobile_users.add(name)
# a = web_users & mobile_users
# print("Niit :", len(a))





# 22
# status = {}
# n = int(input("Heden hun :"))
# for i in range(n):
#     name = input("Ner :")
#     stat = input("Tolow :")
#     status[name]=stat

# a = set()
# for k, v in status.items():
#     if v == "online" :
#         a.add(k)
# name = input("Tolow shalgah ner :")
# if name in a :
#     print("Online")
# else:
#     print("Offline")





# 23
# courses = {}
# n = int(input("Heden hicheel: "))
# for i in range(n):
#     course = input("Hicheeliin ner: ")
#     name = input("Surdag suragchdiin ner: ").split()
#     courses[course] = name
# name = input("Ymar suragch shalgah: ")
# for k, v in courses.items():
#     if name in v:
#         print(k)





# 24
# courses = {}
# n = int(input("Heden hicheel: "))
# for i in range(n):
#     course = input("Hicheeliin ner: ")
#     name = input("Surdag suragchdiin ner: ").split()
#     courses[course] = name
# a = set()
# for k, v in courses.items():
#     for i in v:
#         a.add(i)
# high_course = 0
# best_student = ""
# for i in a:
#     count = 0
#     for k, v in courses.items():
#         if i in v:
#             count += 1
#     if count > high_course:
#         high_course = count
#         best_student = i
# print("Suragch:", best_student)
# print("Hicheeliin too:", high_course)
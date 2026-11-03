# 1
# a = list(map(int, input("Toonuud : ").split()))
# print(set(a), len(a))




# 2
# fruits = set(input().split())
# a = input()
# fruits.add(a)
# print(fruits)





# 3
# fruits = set(input().split())
# a = input()
# fruits.remove(a)
# print(fruits)






# 4
# nums = set(map(int, input("Toonuud : ").split()))
# a = int(input("Shalgah too : "))
# if a in nums :
#     print("Yes")
# else :
#     print("No")





# 5
# a = set(map(int, input().split()))
# print(len(a))





# 6
# names = set(input("Nernuud : ").split())
# b = set(names)
# print(len(b))







# 7
# a = set(map(int, input("Toonuud :").split()))
# b = set(map(int, input("Toonuud :").split()))
# print(a | b)






# 8
# a = set(map(int, input("Toonuud :").split()))
# b = set(map(int, input("Toonuud :").split()))
# print(a & b)







# 9
# a = set(map(int, input("Toonuud :").split()))
# b = set(map(int, input("Toonuud :").split()))
# print(a - b)







# 10
# python_students = set(input("Ner :").split())
# java_students = set(input("Ner :").split())
# print(python_students & java_students)





# 11
# python_students = set(input("Ner :").split())
# java_students = set(input("Ner :").split())
# print(python_students - java_students | java_students - python_students )






# 12
# a = input()
# b = set(a)
# print(len(b))





# 13
# n = int(input("Heden suragch : "))
# stu = {}
# for i in range(n):
#     name = input("Ner : ")
#     age = int(input("Nas : "))
#     stu[name]=age
# print(stu)





# 14
# n = int(input("Heden suragch : "))
# stu = {}
# for i in range(n):
#     name = input("Ner : ")
#     age = int(input("Nas : "))
#     score = int(input("Onoo : "))
#     stu[name] = (age, score)
# print(stu.keys())






# 15
# stu = {}
# name = input("Ner: ")
# age = int(input("Nas: "))
# score = int(input("Onoo: "))
# stu.update({"name" : name,
#             "age" : age,
#             "score" : score})
# score = int(input("Solih onoo :"))
# stu["score"] = score
# print(stu)





# 16
# stu = {}
# name = input("Ner: ")
# age = int(input("Nas: "))
# stu.update({"name" : name,
#             "age" : age})
# city = input("Nemeh hot :")
# stu["city"] = city
# print(stu)



# 17
# stu = {}
# name = input("Ner: ")
# age = int(input("Nas: "))
# score = int(input("Onoo: "))
# stu.update({"name" : name,
#             "age" : age,
#             "score" : score})
# del stu["age"]
# print(stu)




# 18
# car = {}
# brand = input("Ner : ")
# model = input("Torol : ")
# year = int(input("On : "))
# car.update({"brand" : brand,
#             "model" : model,
#             "year" : year})
# print(car.keys())




# 19
# car = {}
# brand = input("Ner : ")
# model = input("Torol : ")
# year = int(input("On : "))
# car.update({"brand" : brand,
#             "model" : model,
#             "year" : year})
# print(car.values())



# 20
# stu = {}
# name = input("Ner: ")
# age = int(input("Nas: "))
# score = int(input("Onoo: "))
# stu.update({"name" : name,
#             "age" : age,
#             "score" : score})
# print(f"Name {name}\nage {age}\nscore {score}")




# 21
# stu = {}
# name = input("Ner: ")
# age = int(input("Nas: "))
# score = int(input("Onoo: "))
# stu.update({"name" : name,
#             "age" : age,
#             "score" : score})
# if "score" in stu :
#     print("Yes")
# else :
#     print("No")




# 22
# product = {}
# name = input("Baraanii ner :")
# price = int(input("Baraanii une :"))
# stock = int(input("Shirheg :"))
# product.update({"name" : name,
#                 "price" : price,
#                 "stock" : stock})
# if product["stock"] > 0 :
#     print("Available")
# else : 
#     print("Out of stock")



# 23
# n = int(input("Heden suragch :"))
# stu = {}
# for i in range(n):
#     name = input("Ner :")
#     score = int(input("Onoo :"))
#     stu[name] = score
# for names, scores in stu.items() :
#     if scores >= 80 :
#         print(names, ":", scores)

 



# 24
# n = int(input("Heden suragch: "))
# stu = {}
# high = 0
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     stu[name] = score
# for names, scores in stu.items():
#     if scores > high:
#         high = scores
# for names, scores in stu.items():
#     if scores == high:
#         print(names, ":", high)


# 25
# sales = {}
# n = int(input("Heden garag :"))
# for i in range(n):
#     name = input("Garagiin ner :")
#     price = int(input("Hymdrah une :"))
#     sales[name] = price
# print(sum(sales.values()))




# 26
# sentence = input("Ugnuud : ").split()
# word_count = {}
# for word in sentence:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# for k, v in word_count.items():
#     print(f"{k} : {v}")



# 27
# a = {}
# n = int(input("Heden suragch"))
# for i in range(n):
#     name = input("Ner :")
#     hicheel = input("Hicheeluud :").split()
#     a[name]=hicheel
# b = set()
# for lessons in a.values():
#     b.update(lessons)
# print(b)




# 28
# stu = {}
# n = int(input("Too: "))
# for i in range(n):
#     name = input("Ner: ")
#     city = input("Hotoo: ")
#     stu[name] = city
# b = set()
# for j in stu.values():
#     b.add(j)
# c = len(b)
# print(c)




# 29
# stu = {}
# n = int(input("Too: "))
# for i in range(n):
#     name = input("Ner: ")
#     city = input("Hotoo: ")
#     stu[name] = city
# for k, v  in stu.items():
#     if v == "Ub" :
#         print(k)





# 30
# n = int(input("Heden utga: "))
# data = {}
# for i in range(n):
#     let = input("Useg: ")
#     num = int(input("Too: "))
#     data[let] = num
# a = set(data.values())
# print(a)
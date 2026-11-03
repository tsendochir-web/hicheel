# 1
# a = [1, 2, 2, 3, 4, 4, 5]
# print(set(a), len(a))



# 2
# fruits = {"apple", "banana"}
# fruits.add("orange")
# print(fruits)


# 3
# fruits = {"apple", "banana", "orange"}
# fruits.remove("banana")
# print(fruits)



# 4
# nums = {10, 20, 30, 40}
# if 20 in nums :
#     print("Yes")
# else :
#     print("No")



# 5
# a = set(map(int, input().split()))
# print(len(a))



# 6
# names = ["Bat", "Sara", "Bat", "Bold", "Sara", "Anu"]
# b = set(names)
# print(len(b))



# 7
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)



# 8
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a & b)



# 9
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a - b)



# 10
# python_students = {"Bat", "Sara", "Bold", "Anu"}
# java_students = {"Sara", "Bold", "Temuulen"}
# print(python_students & java_students)



# 11
# python_students = {"Bat", "Sara", "Bold", "Anu"}
# java_students = {"Sara", "Bold", "Temuulen"}
# print(python_students - java_students | java_students - python_students )


# 12
# a = input()
# b = set(a)
# print(len(b))



# 13
# a = {"name" : "Bat",
#     "age" : 18,
#     "score" : 95
# }
# print(a)



# 14
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
#      }
# print(student["name"])




# 15
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 85
# }
# student["score"] = 98
# print(student)





# 16
# student = {
#     "name": "Anu",
#     "age": 18
# }
# student["city"] = "Ulaanbaatar"
# print(student)



# 17
# student = {
#     "name": "Bold",
#     "age": 20,
#     "score": 88
# }
# del student["age"]
# print(student)




# 18
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# print(car.keys())




# 19
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# print(car.values())



# 20
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 95
# }
# print(student.items())




# 21
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 92
# }
# if "score" in student :
#     print("Yes")
# else :
#     print("No")




# 22
# product = {
#     "name": "Keyboard",
#     "price": 120000,
#     "stock": 5
# }
# if product["stock"] > 0 :
#     print("Available")
# else : 
#     print("Out of stock")



# 23
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# for names, scores in scores.items() :
#     if scores >= 80 :
#         print(names, scores)





# 24
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }

# for names, score in scores.items() :
#     if score <= score :

#         print(names, score)


# 25
# sales = {
#     "Monday": 10,
#     "Tuesday": 15,
#     "Wednesday": 20
# }
# print(sum(sales.values()))




# 26
# sentence = input("Өгүүлбэр оруулна уу: ")
# words = sentence.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print("Үг давталтын тоо:")
# for k, v in word_count.items():
#     print(f"{k}: {v}")



# 27
# a = {}
# n = int(input("Heden suragch"))
# for i in range(n):
#     name = input("Ner :")
#     hicheel = input("Hicheeluu :").split()
#     a[name]=hicheel
# b = set()
# for lessons in a.values():
#     b.update(lessons)
# print(b)




# 28
# stu = {}
# n = int(input("Too :"))
# for i in range(n):
#     name = input("Ner :")
#     city = input("Hotoo :")
#     stu[name]=city
# b = set()
# for j in stu.values():
#     b.update(j)
#     c = len(b)
# print(c)




# 29
lst = [1, 2, 3, 4, 5, 6]
target = int(input())
left = 0
right = len(lst)-1
while left <= right:
    mid = (right+left)//2
    if lst[mid] == target :
        print("oldsn")
        break
    elif lst[mid] < target :
        left = mid + 1
    else :
        right = mid + 1
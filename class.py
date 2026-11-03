# 2
# class player :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# player1 = player("Naraa", 17)
# player2 = player("Temuulen", 19)
# print(player1.name)
# print(player1.age)
# print(player2.name)
# print(player2.age)



# 3
# class player :
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
# player1 = player("Bat", 18, "12A")
# print(f"Ner : {player1.name}")
# print(f"Nas : {player1.age}")
# print(f"Angi : {player1.grade}")




# 4
# class player :
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# player1 = player("Bat", "85 onoo")
# player2 = player("Saraa", "95 onoo")
# print(player1.name)
# print(player1.score)
# print(player2.name)
# print(player2.score)



# 5
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
# student1 = Student("Бат", 80)
# student1.add_score()
# print(student1.score)


# 6
# class student :
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def show_info(self):
#         print(f"Ner :{student1.name}\nNas : {student1.age}\nAngi : {student1.grade}")
# student1 = student("Saraa", 19, "12B")
# student1.show_info()



# 7
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def check_result(self):
#         if self.score >= 60 :
#             print(f"{student1.name} : Tentssen")
#         else :
#             print(f"{student2.name} : Tentseegui")
# student1 = student("Bat", 75)
# student2 = student("Naraa", 45)
# student1.check_result()
# student2.check_result()






# 2
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# n = int(input("Heden suragch :"))
# students = []
# for i in range(n):
#     name = input(f"{i+1}-r Suragch ner :")
#     age = int(input(f"{i+1}-r Suragchiin nas :"))
#     students.append(student(name, age))
# for j in students :
#     print(f"{j.name}\n{j.age}")



# 3
# class student :
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade 
# n = int(input("Heden suragch :"))
# students = []
# for i in range(n):
#     name = input(f"{i+1}-r Suragchiin ner :")
#     age = int(input(f"{i+1}-r Suragchiin nas :"))
#     grade = input(f"{i+1}-r Suragchiin angi :")
#     students.append(student(name, age, grade))
# t = int(input("Heddeh suragchiin medeelel :"))
# print(students[t-1].name)
# print(students[t-1].age)
# print(students[t-1].grade)



# 4
# class student :
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# n = int(input("Heden suragch :"))
# students = []
# for i in range(n):
#     name = input(f"{i+1}-r suragchiin ner :")
#     score = int(input(f"{i+1}-r suragchiin onoo :"))
#     students.append(student(name, score))
# for j in students :
#     print(f"{j.name}\n{j.score}")




# 5

# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def add_score(self, m):
#         self.score += m
# m = int(input("Heden onoo nemeh ve: "))
# n = int(input("Heden suragch: "))
# students = []
# for i in range(n):
#     name = input(f"{i+1}-r suragchiin ner: ")
#     score = int(input(f"{i+1}-r suragchiin onoo: "))
#     s = student(name, score)
#     s.add_score(m)
#     students.append(s)
# for j in students:
#     print(f"{j.name}\n{j.score}")





# 6
# class student :
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def show_info(self):
#         print(f"Ner :{self.name}\nNas : {self.age}\nAngi : {self.grade}")
# n = int(input("Heden udaa :"))
# students = []
# for i in range(n):
#     name  = input(f"{i+1}-r suragchiin ner :")
#     age = int(input(f"{i+1}-r suragchiin nas :"))
#     grade = input(f"{i+1}-r suragchiin angi :")
#     students.append(student(name, age, grade))
# t = int(input("Heddeh suragchiin medeelel :"))
# print(F"Ner : {students[t-1].name}\nNas : {students[t-1].age}\nAngi : {students[t-1].grade}")






# 7
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def check_result(self):
#         if self.score >= 60:
#             print(f"{self.name}: tentssen")
#         else:
#             print(f"{self.name}: tentseegui")
# n = int(input("Heden suragch: "))
# students = []
# for i in range(n):
#     name = input(f"{i+1}-r suragchiin ner: ")
#     score = int(input(f"{i+1}-r suragchiin onoo: "))
#     students.append(student(name, score))
# for j in students:
#     j.check_result()



# 8
# class student :
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def  add_score(self, bonus):
#         self.score += bonus
# n = int(input("heden suragch :"))
# bonus = int(input("Heden onoo nemehiin ? :"))
# students = []
# for i in range(n):
#     name = input(f"{i+1}-r suragchiin ner :")
#     score = int(input(f"{i+1}-r suragchiin onoo : "))
#     s = student(name, score)
#     s.add_score(bonus)
#     students.append(s)
# for j in students :
#     print(f"{j.score}")




# 9
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def birthday(self):
#         self.age += 1
# name = input("Ner: ")
# age = int(input("Nas: "))
# student1 = Student(name, age)
# student1.birthday()
# student1.birthday()
# print(student1.age)





# 10

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         while self.score < 0 or self.score > 100:
#             print("Buruu dun!")
#             self.score = int(input("Dahin dungee oruulna uu: "))
#         if self.score >= 90:
#             print(f"{self.name}: A")
#         elif self.score >= 80:
#             print(f"{self.name}: B")
#         elif self.score >= 70:
#             print(f"{self.name}: C")
#         elif self.score >= 60:
#             print(f"{self.name}: D")
#         else:
#             print(f"{self.name}: F")
# n = int(input("Heden suragch: "))
# students = []
# for i in range(n):
#     name = input(f"{i+1}-r suragchiin ner: ")
#     score = int(input(f"{i+1}-r suragchiin dun: "))
#     students.append(Student(name, score))
# for s in students:
#     s.get_grade()




# 1

# class Phone:
#     def __init__(self, brand, battery):
#         self.brand = brand    
#         self.battery = battery
#     def use_phone(self):
#         self.battery -= 10
#     def charge(self):
#         self.battery += 20
#     def show_battery(self):
#         print(f"Цэнэг: {self.battery}%")
# brand = input("Утасны нэр: ")
# battery = int(input("Цэнэгийн хувь: "))
# phone1 = Phone(brand, battery)
# phone1.use_phone()
# phone1.show_battery()
# phone1.charge()
# phone1.show_battery()

# 1
# def hello():
#     print("Hello, Python")
# hello()



# 2
# def greet(name):
#     print("Sainuu", name)
# greet("Bat")



# 3
# def introduce(name, age):
#     print(name, "ni", age, "nastai")
# introduce("Bat", 18)


# 4
# def add(a, b):
#     return a + b
# a, b = map(int,input("2too og :").split())
# print(add(a, b))



# 5
# def square(num):
#     return num ** 2
# num = int(input("Too og :"))
# result = square(num)
# print(result)



# 6
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# a, b = map(int, input("2too og :").split())
# c = max(a, b)
# print(c)



# 7
# def check_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# num = int(input("Too og :"))
# c = check_even(num)
# print(c)




# 8
# def check_age(age):
#     if age >= 18:
#         return "Adult"
#     else:
#         return "Minor"
# age = int(input("Nas og :"))
# c = check_age(age)
# print(c)




# 9
# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "F"
# score = int(input("Dun og :"))
# while score > 100 or score < 0 :
#     score = int(input("100-s doosh too og :"))
# c = get_grade(score)
# print(c)




# 10
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i, end=" ")
# n = int(input("Too og :"))
# print_numbers(n)



# 11
# def sum_numbers(n):
#     a = 0 
#     for i in range(1, n + 1):
#         a += i
#     return a
# n = int(input("Too og :"))
# c = sum_numbers(n)
# print(c)



# 12
# def count_even(n):
#     a = 0
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             a += 1
#     return a 
# n = int(input("Too og :"))
# c = count_even(n)
# print(c)




# 14
# def find_max(nums):
#     return max(nums)
# nums = list(map(int, input("Too og :").split()))
# c = find_max(nums)
# print(c)




# 13
# def count_digits(num):
#     a = 0 
#     while num > 0 :
#         num //= 10
#         a += 1
#     return a
# num = int(input("Too og :"))
# c = count_digits(num)
# print(c)




# 15
# def find_min(nums):
#     return(min(nums))
# nums = list(map(int, input("Too og :").split()))
# c = find_min(nums)
# print(c)





# 17
# def list_sum(nums):
#     return sum(nums)
# nums = list(map(int, input("Too og :").split()))
# c = list_sum(nums)
# print(c)




# 16
# def count_even(nums):
#     a = 0
#     for i in nums :
#         if i % 2 == 0 :
#             a += 1
#     return a
# nums = list(map(int, input("Too og :").split()))
# c = count_even(nums)
# print(c)




# 18
# def get_age(student, name):
#     return student[name]
# student= {}
# n = int(input("Suragchiin too :"))
# for i in range(n):
#     name = input("Ner og :")
#     age = int(input("Nas og :"))
#     student[name] = age
# m = input("Nas oloh suragchiin ner :")
# print(get_age(student, m))



# 19


# def find_student(student, name):
#     if name in student:
#         return "Found"
#     else:
#         return "Not found"
# student = {}
# n = int(input("Suragchiin too :"))
# for i in range(n):
#     name = input("Ner :")
#     student[name] = True
# name = input("Oloh ner :")
# print(find_student(student, name))


# 20
# def avrg_score(students):
#     score = students.values()
#     b = sum(score)/len(score)
#     return b
# students = {}
# a = int(input("Suragchiin too :"))
# for i in range (a):
#     name = input("Suragchiin ner :")
#     score = int(input("Onoo"))
#     students[name] = score 
# print(avrg_score(students))




# 21
# def unique_count(nums):
#     b = set(nums)
#     return len(b)
# a =list(map(int, input("Toonuud og").split())) 
# print(unique_count(a))



# 22
# def unique_numers(nums):
#     b = set(nums)
#     return b
# a = list(map(int , input("Toonuud og :").split()))
# print(unique_numers(a))



# 23
# def greet(name = " Guest"):
#     return print("Hello" , name)
# greet("Bat")




# 24 ########################## hetsuuu ym bainaaaaa 
# def power(num, exponent = 2):
#     return num ** exponent
# print(power(5))
# print(power(2, 3))




# 25 
# def discount(price, percent=10):
#     if percent == 0:
#         return price 
#     else:
#         return int(price * (1 - percent/100))

# print(discount(10000))
# print(discount(10000, 20))




# 26
# def sum_all(*args):
#     b = sum(args)
#     return b
# a = list(map(int, input("Toonuud : ").split()))
# print(sum_all(*a))




# 27
# def find_max(*args):
#     a = args[0]
#     for i in args:
#         if a < i  :
#             a = i
#     return a
# print(find_max(1,2,3,4,10,6,7))




# 28
# def count_even(args) :
#     a = 0
#     for i in args :
#         if i % 2 == 0 :
#             a += 1
#     return a 
# b = map(int, input("Toonuudaa :").split())
# print(count_even(b))




# 29
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# name = input("Ner: ")
# age = int(input("Nas: "))
# city = input("Hot: ")

# show_info(name=name, age=age, city=city)



# 30
# def calculate_total(**prices):
#     total = 0
#     for k,v in prices.items():
#         total += v
#     return total
# n= int(input("Too :"))
# prices = {}
# for i in range(n):
#     fruits = input("Jims")
#     price = int(input("Une"))
#     prices[fruits]=price
# print(calculate_total(**prices))




# 31
# def analyze_numbers(nums):
#     b = 0
#     c = 0
#     for i in nums:
#         if i % 2 == 0:
#             b += 1
#         else:
#             c += 1
#     return (max(nums), min(nums), sum(nums), b, c)
# a = list(map(int, input("Toonuud: ").split()))
# print(analyze_numbers(a))
    


# 32
# def student_average(students, name):
#     sco = students[name]
#     a = sum(sco)/len(sco)
#     return a
# n = int(input("Too"))
# students = {}
# for i in range(n):
#     name = input("Ner :")
#     sco = list(map(int, input("Onoonuud").split()))
#     students[name]=sco
# name = input("Haih ner :")
# print(student_average(students, name))


        
# 33

# def best_student(students):
#     stu = {}
#     for k, v in students.items():
#         a = sum(v)/len(v)
#         stu[k]=a
#     max_too = max(stu.values())
#     for key,value in stu.items():
#         if max_too == value:
#             return key
# n = int(input("Too"))
# students = {}
# for i in range(n):
#     name = input("Ner :")
#     sco = list(map(int, input("Onoonuud").split()))
#     students[name]=sco
# print(best_student(students))





# 34
# def calculate(*args, **kwargs):
#     bonus = kwargs["bonus"]
#     tax = kwargs["tax"]
#     total = sum(args)
#     return total + bonus - tax
# a = list(map(int, input("Toonuud: ").split()))
# bonus = int(input("Bonus: "))
# tax = int(input("Tax ni: "))
# print(calculate(*a, bonus=bonus, tax=tax))
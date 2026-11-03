# 1.1
# age = int(input("Nas :"))
# if age >= 18 :
#     print("Orj bolnoo")
# else :
#     print("Oroh bolomjgui")





# 1.2
# num = int(input("Too :"))
# if num % 2 == 0 :
#     print("Tegsh")
# else :
#     print("Sondgoi")




# 1.3
# a,b = map(int, input("2 too :").split())
# if a > b :
#     print(a)
# elif b > a :
#     print(b)
# else :
#     print("Tentsuu")





# 1.4
# day = int(input("Too: "))
# while day < 1 or day > 7:
#     print("Buruu too")
#     day = int(input("Dahin too oruulna uu: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")




# 1.5
# km = int(input("Yavsan km: "))
# hour = int(input("Tsag: "))
# if km <= 2:
#     price = 3000
# else:
#     price = 3000 + (km - 2) * 1500
# if hour >= 22 or hour < 6:
#     price = price * 1.2
# print(int(price))





# 1.6
# kwh = int(input("Hereglee: "))
# if kwh <= 150:
#     price = kwh * 100
# elif kwh <= 300:
#     price = 150 * 100 + (kwh - 150) * 150
# else:
#     price = 150 * 100 + 150 * 150 + (kwh - 300) * 200
# print(price)




# 1.7
# is_blocked = input("Blocked: ")
# username = input("Username: ")
# password = input("Password: ")
# failed_attempts = int(input("Failed attempts: "))
# if is_blocked == "True":
#     print("Tanii erh haagdsan baina")
# else:
#     if username == "" or password == "":
#         print("Medeelelee buren oruulna uu")
#     else:
#         if username != "admin":
#             print("Hereglegch oldsongui")
#         else:
#             if password != "1234":
#                 if failed_attempts >= 2:
#                     print("Erh haagdlaa")
#                 else:
#                     print("Nuuts ug buruu")
#             else:
#                 print("Amjilttai nevterlee")






# 2.1
# n = int(input("too :"))
# for i in range(1, n+1):
#     print(i)




# 2.1
# n = int(input("Too :"))
# total = 0 
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total += i
# print(total)




# 2.3
# n = int(input("Too: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")




# 2.4
# money = int(input("Hadgalamjiin ehnii dun: "))
# percent = float(input("Jiliin huvi: "))
# target = int(input("Hureh dun: "))
# year = 0
# while money < target:
#     money = money * (1 + percent / 100)
#     year += 1
# print("Jil:", year)
# print("Mungu:", int(money))





# 2.5
# n = int(input("Too: "))

# if n <= 1:
#     print("Anhnii too bish")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Anhnii too bish")
#             print("Huvaagch:", i)
#             break
#     else:
#         print("Anhnii too mon")





# 2.6
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")



# 2.7
# n = int(input("N: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()




# 2.8
# secret = int(input("Nuuts too :"))

# for i in range(1, 6):
#     num = int(input(f"{i}-r oroldlogo: "))

#     if num > secret:
#         print(f"{num}: Ih baina")
#     elif num < secret:
#         print(f"{num}: Baga baina")
#     else:
#         print(f"{num}: Zuv! {i} dahi oroldlogoor taalaa")
#         break
# else:
#     print("Ylagdlaa. Nuuts too:", secret)





# 2.9
# n = int(input("Too: "))
# while n >= 10:
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit
#         n //= 10
#     n = total
# print(n)





# 3.1
# scores = list(map(int, input("Toonuud :").split()))
# total = 0
# count = 0
# for score in scores:
#     total += score
#     count += 1
# avr = total / count
# print(f"NIilber : {total}\nDundaj : {avr}")





# 3.2
# nums = list(map(int, input("Toonuud: ").split()))
# high = nums[0]
# index = 0
# for i, j in enumerate(nums):
#     if j > high:
#         high = j
#         index = i
# print(f"Hamgiin ih: {high}\nIndex : {index}")







# 3.3
# names = input("Nernuud :").split()
# search = input("Haih ner: ")
# if search in names:
#     print(names.index(search))
# else:
#     print("Oldsongui")








# 3.4
# prices = list(map(int, input().split()))
# new_prices = []
# for price in prices:
#     new_prices.append(price * 0.9)
# print(new_prices)





# 3.5
# scores = list(map(int, input("Onoonuud :").split()))
# count= 0 
# for i in scores:
#     if i >= 60 :
#         count+=1
#         print(i, end=" ")
# print("Tentssen", ":", count)






# 3.6
# orders = []
# n = int(input("Zahialgiin too: "))
# for i in range(n):
#     order = int(input("Zahialgiin dun: "))
#     orders.append(order)
# a = []
# for order in orders:
#     if order >= 5000:
#         a.append(order + 2000)
# total = sum(a)
# print("Niit orlogo:", total)






# 3.7
# names = []
# subjects = []
# scores = []
# n = int(input("Oyuutnii too: "))
# m = int(input("Hicheeliin too: "))
# for i in range(n):
#     name = input("Oyuutnii ner: ")
#     names.append(name)
# for j in range(m):
#     subject = input("Hicheeliin ner: ")
#     subjects.append(subject)
# for i in range(n):
#     row = []
#     print(names[i], "dun:")
#     for j in range(m):
#         score = int(input(subjects[j] + ": "))
#         row.append(score)
#     scores.append(row)
# for i in range(n):
#     total = 0
#     for j in range(m):
#         total += scores[i][j]
#     print(names[i], ":", total / m)
# print("\nHicheel bureer hamgiin undur:")
# for j, subject_scores in enumerate(zip(*scores)):
#     high = max(subject_scores)
#     index = subject_scores.index(high)
#     print(subjects[j], ":", names[index], "(", high, ")")





# 4.1
# word = input("Ug :")
# find = input("Useg :")
# print(len(word))





# 4.2
# word = input("Ug :")
# find = input("Useg :")
# print(word.count(find))




# 4.3
# email = input("Email: ")
# if email.count("@") == 1:
#     username, domain = email.split("@")

#     if username != "" and "." in domain and not domain.endswith("."):
#         print("Zuv email")
#         print("Username:", username)
#         print("Domain:", domain)
#     else:
#         print("Buruu email")
# else:
#     print("Buruu email")




# 4.4
# words = input("Horiotoi ugnuud: ").lower().split()
# word = input("Oguulber: ")
# result = []
# for w in word.split():
#     if w.lower() in words:
#         result.append("*" * len(w))
#     else:
#         result.append(w)
# print(" ".join(result))





# 4.5
# words = input("Ug uguulber: ").lower()
# result = ""
# for char in words:
#     if char.isalnum():
#         result += char
# if result == result[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")




# 5.1
# def any(n):
#     return n * n
# n = int(input("Too :"))
# print(any(n))





# 5.2
# def greet(name):
#     return "Sain baina uu " + name
# name = input("Ner: ")
# print(greet(name or "Zochin"))




# 5.3
# def is_adult(age):
#     if age >= 18 :
#         return True
#     else:
#         return False
# age = int(input("Nas :"))
# print(is_adult(age))





# 5.4
# def calculate_bmi(weight, height):
#     BMI = weight / (height ** 2)
#     return round(BMI, 2)
# def get_category(BMI):
#     if BMI <=18.5:
#         return "Turanhai"
#     elif BMI <= 25:
#         return "Hewiin"
#     elif BMI <= 30:
#         return "Iluudel jintei"
#     else:
#         return "Targalalttai"
# weight = float(input("Jin (kg): "))
# height = float(input("Ondor (m): "))
# bmi = calculate_bmi(weight, height)
# print("BMI:", bmi)
# print("Angilal:", get_category(bmi))





# 5.5
# def calc_insurance(gross):
#     ndsh = gross * 11.5 / 100
#     return ndsh
# def calc_tax(gross):
#     ndsh = calc_insurance(gross)
#     tax = (gross - ndsh) * 10 / 100
#     return tax

# def calc_net(gross):
#     ndsh = calc_insurance(gross)
#     tax = calc_tax(gross)
#     net = gross - ndsh - tax
#     return net
# gross = float(input("Tsalin: "))
# print("NDSh:", int(calc_insurance(gross)))
# print("Tatvar:", int(calc_tax(gross)))
# print("Gart olgoh:", int(calc_net(gross)))





# 5.6
# def make_counter():
#     count = int(input("Ehnii too: "))
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     def decrement():
#         nonlocal count
#         count -= 1
#         return count
#     def reset():
#         nonlocal count
#         count = 0
#         return count
#     return {"increment": increment, "decrement": decrement, "reset": reset}
# counter = make_counter()
# print(counter["increment"]())
# print(counter["decrement"]())
# print(counter["reset"]())






# 6.1
# info = {}
# name = input("Ner :")
# age = int(input("Nas :"))
# city = input("Hot :")
# info.update({"name" : name,
#              "age" : age,
#              "city" : city})
# mail = input("Nemeh mail :")
# info["email"]=mail
# del info["city"]
# info["age"] += 1
# print(info)






# 6.2
# prices = {}
# n = int(input("Heden baraa :"))
# for i in range(n):
#     name = input("Baraanii ner :")
#     price = int(input("Baraanii une :"))
#     prices[name]=price
# for k,v in prices.items():
#     print(k, "-", v)






# 6.3
# total = 0
# high_price = 0
# prices = {}
# n = int(input("Heden baraa :"))
# for i in range(n):
#     name = input("Baraanii ner :")
#     price = int(input("Baraanii une :"))
#     prices[name] = price
# for k, v in prices.items():
#     total += v
#     if v > high_price:
#         high_price = v
#         name = k
# print(f"Hamgiin unetei : {name} - {high_price}\nNiit : {total}")




# 6.4
# votes = {}
# n = int(input("Heden sanal: "))
# for i in range(n):
#     name = input("Ner: ")
#     votes[name] = votes.get(name, 0) + 1
# winner = ""
# high = 0
# for k, v in votes.items():
#     if v > high:
#         high = v
#         winner = k
# print(f"Sanal: {votes}\nYlagch ni: {winner}\nSanaliin too: {high}")






# 6.5
# classes = {}
# n = int(input("Heden oyutan: "))
# for i in range(n):
#     name = input("Ner: ")
#     clas = input("Angi: ")
#     if clas not in classes:
#         classes[clas] = []
#     classes[clas].append(name)
# print(classes)






# 1
# n = int(input("Suragchiin too : "))
# m = int(input("Shalgaltin too : "))
# for i in range(n):
#     total = 0
#     for j in range(m):
#         score = int(input("Dun: "))
#         total += score
#     avg = total / m
#     print("Niit onoo:", total)
#     print("Dundaj:", avg)
#     if avg >= 60:
#         print("Tentssen")
#     else:
#         print("Tentseegui")



# 2
# n = int(input("Heden hun: "))

# for i in range(n):
#     m = int(input("Heden baraa: "))
#     total = 0
#     for j in range(m):
#         une = int(input("Negj une: "))
#         a = int(input("Shirheg: "))
#         total += une * a
#     print(f"{i + 1}-r hunii tuluh dun: {total}")

#     money = int(input("Ugsun mungu: "))
#     if money >= total:
#         print("Hariult:", money - total)
#     else:
#         print("Dutuu mungu:", total - money)



# 3
# n = int(input("Ajilchdiin too: "))
# for i in range(n):
#     total = 0
#     for j in range(5):
#         hour = int(input("Ajillasan tsag: "))
#         if hour <= 8:
#             total += hour * 5000
#         else:
#             total += 8 * 5000 + (hour - 8) * 7500
#     print(f"{i + 1}-r ajilchnii niit tsalin:", total)





# 4
# n = int(input("Heden hun: "))
# m = int(input("Heden sar: "))
# for i in range(n):
#     debt = int(input(f"{i + 1}-r hunii awsan zeel : "))
#     total = 0
#     for j in range(m):
#         payment = int(input(f"{j + 1}-r sariin tulult: "))
#         debt -= payment
#         total += payment
#         print(f"{i + 1}-р хүн, {j + 1}-р сарын дараах үлдэгдэл: {debt}")
#     print("Tolson ni :", total)





# 5
# n = int(input("Udriin too: "))
# m = int(input("Udurt uildverleh udaa: "))
# for i in range(n):
#     total = 0
#     for j in range(m):
#         product = int(input(f"{j + 1}-r uildverleliin too: "))
#         total += product
#     box = total // 12
#     remainder = total % 12
#     print(f"{i + 1}-r odor: niit {total}, buten hairtsag {box}, uldegdel {remainder}")




# 6
# n = int(input("Ayallin too: "))
# m = int(input("Buudliin too: "))
# for i in range(n):
#     passenger = 0
#     total = 0
#     for j in range(m):
#         get_off = int(input("Buusan hun: "))
#         get_on = int(input("Suusan hun: "))
#         passenger -= get_off
#         passenger += get_on
#         total += get_on
#         print(f"{j + 1}-r buudliin daraa: {passenger} hun")
#     income = total * 1000
#     print(f"{i + 1}-r aylald niit suusan: {total}")
#     print("Aylaliin orlogo :", income)





# 7
# n = int(input("Too : "))

# for i in range(1, n + 1):
#     count = 0
#     total = 0

#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#             total += j

#     print(f"{i}: {count} huwaagchtai, niilber {total}")




# # 8
#     n = int(input("Too : "))
# count = 0

# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i + j == n:
#             print(f"{i} + {j} = {n}")
#             count += 1

# print("Niit:", count, "hos")





# # 9
# n = int(input("Too : "))
# count = 0

# for i in range(n // 1000 + 1):
#     for j in range(n // 2000 + 1):
#         if i * 1000 + j * 2000 == n:
#             print(f"1000₮: {i} shirheg, 2000₮: {j} shirheg")
#             count += 1

# print("Niit:", count, "huwilbar")





# 10
# n = int(input("Too : "))
# count = 0
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i * j == n:
#             print(f"{i} x {j} = {n}, ylgawar {j - i}")
#             count += 1
# print("niit:", count, "hos")
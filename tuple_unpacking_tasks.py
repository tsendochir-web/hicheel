# 1
# a = tuple(input().split())
# print(a)




# 2
# a = ('nohoi', 'muur', 'tuulai', 'mori')
# print( f"{a[0]}\n{a[2]}\n{a[-1]}" )





# 3
# a = (100,)
# print(type(a))





# task4
# a = tuple(input().split())
# print(f"{a[0]}\n{a[-2]}\n{a[-1]}")




# task5
# a = tuple(map(int, input().split()))
# print(a[:3])





# # task6
# a = tuple(map(int, input().split()))
# print(a[-3:])





# task7
# a = tuple(input().split())
# print(len(a))








# task8
# a = tuple(map(int, input().split()))
# print( f" Hamgiin ih : {max(a)} \nHamgiin baga : {min(a)}" )






# task9
# a = tuple(map(int, input().split()))
# print(f" Onoonii niilber : {sum(a)} \nOnoonnii dundaj : {sum(a)/len(a)} ")






# task10
# a = tuple(map(int, input().split()))
# b = sorted(a)
# print(b)






# task11
# a = tuple(map(int, input().split()))
# b = int(input())
# print(a.count(b))






# task12
# a = tuple(input().split())
# b = input()
# print(a.index(b))






# task13
# a = tuple(input().split())
# b = input()
# if b in a :
#     print("Bainaa")
# else :
#     print("Baihguie bro")





# task 14
# student = tuple(map(str, input().split()))
# name, age, angi = student
# print( f" Name:{name} \n Age:{age} \n Angi:{angi}" )






# task15
# a = tuple(map(int, input().split()))
# x, y = a
# print(f"x = {x} \ny = {y}")






#task16
# a = tuple(map(str, input().split()))
# nom, zohiolch, huudas = a 
# print( f"Nom : {nom} \nZohiolch : {zohiolch} \nHuudas : {huudas}")






# task17
# c = tuple(map(int, input().split()))
# a, b = c
# print(f"a = {b} \nb = {a} ")





# task18
# a = tuple(map(int, input().split()))
# b, *c = a
# print(f" first : {b}\n others : {c}")





# task19
# a = tuple(map(int, input().split()))
# b, *c, d = a
# print(f" ehniih : {b}\n dundah : {c}\n suuliinh : {d}")





# task 20
# a = tuple(input().split())
# b, *d = a
# print(f" Ner : {b}\n Hicheeluud : {d}")






# task21
# a = tuple(input().split())
# name, price, quantity = a
# b = int(price)
# c = int(quantity)
# total = b * c
# print(f"Baraa : {name}\n Une : {price}\n Shirheg : {quantity}\n Total : {total}")






# task22
# n = int(input("Heden suragch: "))
# stu = []
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     stu.append((name, score))
# for name, score in stu:
#     print(f"{name}: {score}")





# task23
# n = int(input("Heden suragch : "))
# stu = []
# for i in range(n):
#     name = input("Ner : ")
#     score = int(input("Onoo : "))
#     stu.append((name, score))
# for name, score in stu :
#     if score >= 80 :
#         print(name,":", score)




# task24
# a = tuple(input().split())
# c = input()
# b = list(a)
# b.append(c)
# tuple(b)
# print(b)
# 1 osoh daraalal
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)


# 2 buurah daraalal ni
# nums = list(map(int, input("Toonuud :")).split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] < nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)


# 3 sorog too baisan ch ihruu ni 
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)




# 4 dawhardsan too baisan ch ihruu
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)


# 5 garaas utgaa awaad ihruu eremble gnee
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)



# 6 nersiig eremble
# nums = input("Ugnuud og :").split()
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)



#7 onoonuudiig eremble
# scores = list(map(int, input("Onoonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(scores)



# 8 hamgiin toog ni l baruun zahd garga
# nums = list(map(int, input().split()))
# for i in range(len(nums) -1):
#     if nums[i] > nums[i+1]:      
#         a = nums[i]
#         nums[i] = nums[i+1]
#         nums[i+1]=a
# print(nums)




# 9 dawtalt heden udaa ajillahiig todorhoil daraa ni erembelsen jagsaalt
# nums = list(map(int, input("Toonuud :").split()))
# count = 0
# for i in range(len(nums) -1):
#     count +=1 
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(f"{nums}\n{count}")




# 10 heden udaa soligdoj baigaag ni tool
# nums = list(map(int, input("Toonuud :").split()))
# count = 0
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             count +=1 
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(f"{count}\n{nums}")



# 11buurah daraallaar erembeleed 2dahi hamgiin ih too
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] < nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums[1])




# 12 eyreg sorog toonuudiig eremble 
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)



# 13 erembelj baigaa ywts buriig hewle
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums) -1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
#             print(nums)




# 14
# nums = list(map(int, input("Toonuud: ").split()))

# for i in range(len(nums) - 1):
#     swapped = False
#     for j in range(len(nums) - 1 - i):
#         if nums[j] > nums[j + 1]:
#             a = nums[j]
#             nums[j] = nums[j + 1]
#             nums[j + 1] = a
#             swapped = True
#     if not swapped:
#         break
# print(nums)




# 15
# nums = list(map(int, input("TOonuudaa :").split()))
# count = 0
# for i in range(len(nums) - 1):
#     swapped = False
#     count += 1
#     for j in range(len(nums) - 1 - i):
#         if nums[j] > nums[j + 1]:
#             a = nums[j]
#             nums[j] = nums[j + 1]
#             nums[j + 1] = a
#             swapped = True
#     if not swapped:
#         break
# print(f"{nums}\n{count}")



# 16
# n = int(input("Heden suragch: "))
# stu = []
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     stu.append([name, score])
# for i in range(len(stu) - 1):
#     for j in range(len(stu) - 1 - i):
#         if stu[j][1] > stu[j + 1][1]:
#             a = stu[j]
#             stu[j] = stu[j + 1]
#             stu[j + 1] = a
# print(stu)



# 17

# n = int(input("Heden hun: "))
# people = []
# for i in range(n):
#     name = input("Ner: ")
#     age = int(input("Nas: "))
#     people.append([name, age])
# for i in range(len(people) - 1):
#     for j in range(len(people) - 1 - i):
#         if people[j][1] > people[j + 1][1]:
#             a = people[j]
#             people[j] = people[j + 1]
#             people[j + 1] = a
# print(f"{people}\nHamgiin zaluu: {people[0]}\nHamgiin hogshin: {people[-1]}")



# 18
# nums = list(map(int, input("Toonuud :").split()))
# find = int(input("Haih too :"))
# count = 0
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j + 1]:
#             a = nums[j]
#             nums[j] = nums[j + 1]
#             nums[j + 1] = a
# for i in nums:
#     if i == find :
#         count += 1
# print(f"{nums}\n{count}")



# 19
# n = int(input("Heden baraa: "))
# product = []
# for i in range(n):
#     name = input("Ner: ")
#     price = int(input("Onoo: "))
#     product.append([name, price])
# for i in range(len(product) - 1):
#     for j in range(len(product) - 1 - i):
#         if product[j][1] < product[j + 1][1]:
#             a = product[j]
#             product[j] = product[j + 1]
#             product[j + 1] = a
# print(f"{product}\nHamgiin unetei guraw : {product[0]}, {product[1]}, { product[2]}")



# 20
# nums = list(map(int, input("Toonuud :").split()))
# soliltsoo = 0
# gadna_toirgiin_too = 0
# haritsuulalt = 0
# for i in range(len(nums) -1):
#     gadna_toirgiin_too +=1
#     for j in range(len(nums)-1 -i):
#         haritsuulalt += 1
#         if nums[j] > nums[j+1]:
#             soliltsoo += 1
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(f"{nums}\nSoliltsoonii too ni : {soliltsoo}\nGadnah toirgiin too ni : {gadna_toirgiin_too}\nHaritsuulaltiin too : {haritsuulalt}")




# 21
# nums = list(map(int, input("Toonuudaa").split()))
# even = []
# odd = []
# for i in nums:
#     if i % 2 == 0 :
#         even.append(i)
#     if i % 2 != 0:
#         odd.append(i)
# for i in range(len(even)-1):
#     for j in range(len(even)-1 - i):
#         if even[j] > even[j + 1]:
#             a = even[j]
#             even[j] = even[j + 1]
#             even[j + 1] = a
# for i in range(len(odd)-1):
#     for j in range(len(odd)-1 - i):
#         if odd[j] > odd[j + 1]:
#             b = odd[j]
#             odd[j] = odd[j + 1]
#             odd[j + 1] = b
# print(f"Tegsh ni : {even}\nSondgoi ni : {odd}")




# 22
# words = input().split()
# n = len(words)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if len(words[j]) > len(words[j + 1]):
#             words[j], words[j + 1] = words[j + 1], words[j]
# print(*words)




# 23
# numbers = list(map(int,input().split()))
# count = 0
# for i in range(len(numbers)):
#     count +=1 
#     for j in range(len(numbers) - 1, 0, -1):
#         if numbers[j] < numbers[j - 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j - 1]
#             numbers[j - 1] = temp
#     if count == 1:
#         print(numbers)
#         break



# 24
# numbers = list(map(int,input().split())())
# for i in range(len(numbers) - 1, 0, -1):
#     if numbers[i] < numbers[i - 1]:
#         numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
# print(numbers)



# 25
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = a + b
# for i in range(len(c) - 1):
#     for j in range(len(c) - 1 - i):
#         if c[j] > c[j + 1]:
#             v = c[j]
#             c[j] = c[j + 1]
#             c[j + 1] = v
# print(c)



# 26
# nums = list(map(int,input("Toonuud :").split()))
# count = 0
# count1 = 0
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         count +=1
#         if nums[j] > nums[j + 1]:
#             count1 += 1
#             a = nums[j]
#             nums[j] = nums[j + 1]
#             nums[j + 1] = a
#             print(f"Toirog : {count} :Soliltsoo : {count1}")
# print(nums)


# 27
# nums = list(map(int, input("Toonuud :").split()))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j + 1]:
#             a = nums[j]
#             nums[j] = nums[j + 1]
#             nums[j + 1] = a
# print(nums[2])



# 28

# n = int(input("Heden suragch: "))
# stu = []
# best = []
# for i in range(n):
#     name = input("Ner: ")
#     score = int(input("Onoo: "))
#     stu.append([name, score])
#     if score >= 80:
#         best.append([name, score])
# for i in range(len(stu) - 1):
#     for j in range(len(stu) - 1 - i):
#         if stu[j][1] < stu[j + 1][1]:
#             a = stu[j]
#             stu[j] = stu[j + 1]
#             stu[j + 1] = a
# print(f"{stu}\nTentssen suragchid: {best}")




# 29
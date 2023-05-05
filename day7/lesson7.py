
# my_arr = ["banana",11,True,11.05,[1,2,3],5,10]  #კვადრატული ფრჩხილით შექმნილი კორექცია არის ლისტი

# print(my_arr[-1])
# print(my_arr[-3])
# print(my_arr[3])
# print(my_arr[1:4])
# print(my_arr[1:4:2])
# print(my_arr[:4])

# menu =["xinkali","mwvadi","lobiani","khachapuri","wyali]"]
# if "lobiani" in menu:
#     print("gvaq lobiani")

# menu[1] = "BBQ"
# print(menu) # ['xinkali', 'BBQ', 'lobiani', 'khachapuri', 'wyali]']
# menu[2:4] = ["aa","bb","cc"] 
# print(menu)#  ['xinkali', 'mwvadi', 'aa', 'bb', 'cc', 'wyali]']

# my_name = "davita"
# new_name = ""
# for i in range(len(my_name)):
#     if i == 3 or i ==4:
#         new_name += "x"
#     else:new_name += my_name[i]
#     print(new_name)

# menu =["xinkali","mwvadi","lobiani","khachapuri","wyali]"]
# menu.insert(3, "nayini")
# print(menu)       ['xinkali', 'mwvadi', 'lobiani', 'nayini', 'khachapuri', 'wyali]']]
# menu.append("cecxli")  
# menu.append("navti")
# print(menu)  ['xinkali', 'mwvadi', 'lobiani', 'khachapuri', 'wyali]', 'cecxli', 'navti']

# menu = []
# menu.append("pizza")
# print(menu)  ['pizza']

#momxmarebels shemaotaninet 5 sachmeli da siashi sheitanet isini romlebic sheicaven minimum 2 a s 
  
#ჩემი ამოხსნა

# product1 = input("name of product1: ")
# product2 = input("name of product2: ")
# product3 = input("name of product3: ")
# product4 = input("name of product4: ")
# product5 = input("name of product5: ")

# menu = []

# a_in_product1 = 0
# for char in product1:
#     if char=="a":
#         a_in_product1 += 1
#         if a_in_product1 >= 2:
#             menu.append(product1)     

# a_in_product2 = 0
# for char in product2:
#     if char == "a":
#         a_in_product2 += 1
#         if a_in_product2 >= 2:
#             menu.append(product2)     

# a_in_product3 = 0
# for char in product3:
#     if char== "a":
#         a_in_product3 += 1
#         if a_in_product3 >= 2:
#             menu.append(product3)      

# a_in_product4 = 0
# for char in product4:
#     if char == "a":
#         a_in_product4 += 1
#         if a_in_product4 >= 2:
#             menu.append(product4) 

# a_in_product5 = 0
# for char in product5:
#     if char == "a":
#         a_in_product5 += 1
#         if a_in_product5 >= 2:
#             menu.append(product5)
# print(menu)


#                               უფრო მარტივი ამოხსნა:
# menu = []
# for i in range(5):
#     food = input ("enter food here")
#     if food.count("a") >=2:
#         menu.append(food)    
#           print(menu)


 #                             თუ ქაუნთი ჯერ არ ვიცით:

        
# menu = []
# for i in range(5):
#     food = input("enter food name here")
#     count = 0
#     for char in food:
#         if char == "a":
#             count += 1
#             if count >= 2:
#                 menu.append(food)
#                 count = 0 


# menu = ["xinkali","mwvadi","lobiani","khachapuri","wyali"]
# menu.remove("wyali")
# menu.remove("mwvadi")
# print(menu)  # ['xinkali', 'lobiani', 'khachapuri']
# del menu[2]
# print(menu) #['xinkali', 'mwvadi', 'khachapuri', 'wyali']


# menu = ["xinkali","mwvadi", "qababi", "lobiani","khachapuri","wyali"]
# #წაშალეთ ელემენტები რომლებშიც მეორე ასო არის ა 

# # for food in menu:
# #     if food[1] == "a":
# #         menu.remove(food)
#         print(menu)
 # რიმუვი და ციკლი ერთად არ გამოვიყენოთ


# menu = ["xinkali","mwvadi", "nayini", "qababi", "lobiani","khachapuri","wyali"]
# new_menu = []
# for food in menu:
#     if food[1] != "a":
#         new_menu.append(food)
#         print(new_menu)

# scores=[20,43,56,73,10,6,87,45,97]
# scores.sort()
# print(scores)    #დალაგდება ზრდადობის მიხედვით

# students =["nika","ana","beqa","mamuka","dachi","iva","farna"]
# students.sort()
# print(students)   #['ana', 'beqa', 'dachi', 'farna', 'iva', 'mamuka', 'nika'] ანბანის მიხედვით

# students =["nika","ana","beqa","mamuka","dachi","iva","farna"]
# students.sort(reverse=True)
# print(students)

#1) daasortiret scores=[20,43,56,73,10,6,87,45,97] sort() gamoyenebis gareshe
#while ciklit satitaod sheamowmet elementi da mis marjvniv mdebare elementi romelic ufro mcirea marcxniv gadmoitanet

#sortis da maqs funqciis gareshe gamoitanet yvelaze didi ricxvi
#while ciklit satitaod sheamowmet elementi da mis marjvniv mdebare elementi romelic didi iqneba droebit mianichet maqsimumis mnishvneloba da shemdeg sheadaret marjvniv mdgoms

#2)students =["nika","ana","beqa","mamuka","dachi","iva","farna"] sheatrialet sort reversis gareshe



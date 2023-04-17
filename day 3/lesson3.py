
# if True:
#     print("z")

# my_name ="daviti"

# if "d" in my_name:
#     print("sheicavs d-s") 

# my_name = "daviti"
# my_surname = "avaliani"
# my_sentence = "aa {} bb {} cc {}".format(my_name, my_surname, "zz") ფორმატშის ფრჩხილებში იწერება სიმბოლოები რომელიც ცვლადის მნიშვნელობაში ფიგურული ფრჩხილებით ჩაისმება

# print(my_sentence)  დაიპრინტება(aa daviti bb avaliani cc zz)

# my_name ="daviti"
# my_surname ="avaliani"
# my_age ="23"

# my_sentence ="aa {2} bb {0} cc {1}".format(my_name,my_surname, my_age)

# print(my_sentence)  ვინაიდან ლისთში ასაკი მეორეა სახელი მენულე და გვარი 1 დაიპრინტება (aa 23 bb daviti cc avaliani)

# my_name ="daviti"
# my_surname ="avaliani"
# my_age ="23"
# my_height="180"

# my_sentence="my name is {0} my surname is {1} i am {2} years old, i am {3} cm".format(my_name,my_surname,my_age,my_height)
# print(my_sentence)  შედეგი: (my name is daviti my surname is avaliani i am 23 years old, i am 180 cm) 

# my_name ="daviti"

# if "d" in my_name:           
#     print("sheicavs d-s")      თუ დ არის სახელში დაპრინტავს შესაბამის პასუხს თუ არ იქნება დაპრინტავს რომ არ შეიცავს
# else:
#     print("ar sheicavs d-s ")

###input
####output

# my_name = input("enter your name:" ) 
# print("chemi saxelia "+ my_name)

# my_age = 22
# my_age += 3
# print(my_age)  მივიღებთ (25)ს 

       #დავალება:
#შემოვიტანოთ მომხმარებლის სახელი, გვარი, ასაკი
#დავპრინტოთ წინადადებაში ეს ცვლადები ფორმატ მეთოდის გამოყენებით
#გავიყვანოთ სამი წელი და მოვუმატოთ ასაკი , დავპრინტოთ ახალი წინადადება:
               #ამოხსნა:
#ძველი ვერსია:my_name = imput("Please enter your name") *ასაკის მიმატებისას მოგვცა ერორი
# my_name = int(input(" please enter your name" ))  #input-ით ყოველთვის შემოდის სტრინგი ამიტო მოგვიწია სტრინგის ინტეჯერად გარდაქმნა {გარდაქმნის მეორე მეთოდი განხილულია ქვემოთ}
# my_surname = input(" please enter your surname" )
# my_age = input("please enter your age" )
# print("chemi saxelia {} chemi gvaria {} chemi asakia {}".format(my_name, my_surname,my_age))
# # # "გავიდა სამი წელი და გავხდი x წლის"
# #                         #ამოხსნა:

# # ძველი ვერსია - my_age += 3 
# # erorfix-ი my_age =int(my_age) + 3 #ჩემი(განახლებული)ასაკი=გაინტეჯერებულ ჩემ სტრინგ ასაკს +3 (3 ინტეჯერია უკვე)
# new_age = int(my_age)+ 3
# print("gavida sami weli da var {} wlis".format(int(new_age)))
# print(type(my_age))

# print(2+2)
# print("2"+"2") #სტრინგებს შორის + არ არის მათემათიკური ოპერაცია ის უბრალოდ ორ სიმბოლოს დაუმატებს *22


# year = input("enter years")
# my_age =input("enter your age")
# new_age =int(my_age) + int(year) 
# print("after {} years i'll be {} years old".format(year,new_age))
        
#მომხმარებელს შემოატანინეთ ორი რიცხვი და დაპრინტეთ მათი ნამრავლი თუ ის 100ზე მეტია
#თუარადა დაპრინტეთ რომ მან წააგო
              

#ბიძისამოხსნა:


# first_number = int (input("please enter first number"))
# second_number = int (input("please enter secondnumber"))

# if first_number * second_number > 100:
#     print(first_number * second_number)
# else:
#     print("you lost")


# * / + - ის გარდა გვაქვს % პიფთონში % = ნაშთს. მაგ: print(20 % 6) 20/6=3(2) რჩება ნაშთში ამიტო დაპრინტავს 2ს

#input % if +=  ის გამოყენებით ამოვხსნათ ამოცანა

#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
#აქედან მხოლოდ კენტი შეიკრიბოს და დაიპრინტოს ჯამი
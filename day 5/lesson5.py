#ციკლები (loops)
# 1)for loop  
# 2) while loop

# #i საიტერაციო ცვლადი
# for i in range(7):  #range 7 = 0, 1, 2, 3, 4, 5, 6  #for range(7-3) 0,1,2,3
#     print("nika")

# for i in range(len("giorgi")):
#     print("mika")

# for i in range(2,6):   #2.3,4,5
#    print("nika")

# for i in range (3,6):        #i ართმევს რიცხვს ობიექტს და ინახავს საკუთარ თავში
#    print(i, "nika")   # 3 nika  4 nika 5 nika

# for i in range(3,6):
#     print(str (i) + "nika")   #iს მაგივრად შეგვიძლია ჩავწეროთ რაიმე და ის მიიღებს რიცხვის მნშვნელობას

# for i in range (5, 10 ,2):  #5 დან ათამდე ყოველი მეორე 5,7,9  # სამი რიცხვი 
#     print(str(i) + "nika") 

#range-ს შეგვიძლია გადავცეთ 1 , 2  ან 3 პარამეტრი


#i = 0
# while i < 5:
#     print("nika")  #უსასრულოდ გაეშვება nika თუ საიტერაციო ცვლადის ინკრემენტაციას არ მოვახდენთ
#     i += 1   #საიტერაციო ცვლადის ინკრემენტაცია

# i = 0
# while i < 5:
#     print("nika")
#     print(i)
#     i+=1


# full_name ="davit avaliani"

# i = 0
# while i < len(full_name):
#     print(full_name[i])   #i თუ ნოლია ანუ მენულეა მაშინ  პირვეელ ციკლში დაპრინტავს მენულე პოზიციაზე მდგომ d ს 
#     i+=1                  #მეორე ციკლში დაპრინტავს მენულეს + 1 ანუ პირველს და ეს არის a და ასე გაყვება full_name-ის სიგრძეს


# a = "qwerty"
# b = "asdfgh"

# i = 0
# while i < len(a):
#     print(a[i] + b[i])
#     i+=1

# if 10 > 1 and 3 > 1:
#     print("cool)")

# if False:
#     print("amen")
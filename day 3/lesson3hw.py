#input % if +=  ის გამოყენებით ამოვხსნათ ამოცანა

#მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
#აქედან მხოლოდ კენტი შეიკრიბოს და დაიპრინტოს ჯამი


num1 = int(input(" enter first number"))
num2 = int(input(" enter second number"))
num3 = int(input(" enter third number"))

sum = 0

if num1 % 2 ==1:
    sum+=num1

if num2 % 2==1:
    sum+=num2

if num3 % 2==1:
    sum+=num3

print ("sum of the three odd numbers is {}".format(sum))











    








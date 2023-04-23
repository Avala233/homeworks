#დავალება :
#მომხმარებელს ორი სახელი შემოვატანინოთ და დავპრინტოთ რომელში მეტი თანხმოვანია


name1 = input("enter name1 here"  )
name2 = input("enter name2 here"  )

consonants1 = 0
consonants2 = 0
for char in name1:
    if char not in "aeiou": 
        consonants1 += 1
for char in name2:
    if char not in "aeiou":
        consonants2 += 1
if consonants1 > consonants2:
    print("name1 contains more consonants and their number is {}".format(consonants1))
elif consonants2 > consonants1:
    print("name2 contains more consonants and their number is {}".format(consonants2))
else:
    print("name1 and name2 contain same number of consonants")
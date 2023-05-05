#1) daasortiret scores=[20,43,56,73,10,6,87,45,97] sort() gamoyenebis gareshe
#while ciklit satitaod sheamowmet elementi da mis marjvniv mdebare elementi romelic ufro mcirea marcxniv gadmoitanet


scores =[20,43,56,73,10,6,87,45,97]     
min_score = scores[0]
key_score = scores[2]

sorted_scores =[]

for score in scores:                              #43,56,73,87,97     45?????
    if score < min_score:                         #6,10,              20?????
        sorted_scores.insert(0,score)
   
    elif score >= min_score and score <= key_score:
        sorted_scores.insert(4,score)
    #print(sorted_scores)
    
    elif score > min_score:
        sorted_scores.append(score)
    print(sorted_scores)
    

    
                            



#sum of positives ფუნქცია:




def positive_sum(arr):
    new_arr = []                        #sum = 0
                                        #for number in arr
                                        #    if number > 0
                                        #        sum += number                              
    i=0                                 #    return sum
    while i < len(arr):
        if arr[i] > 0:
            new_arr.append(arr[i])
        i += 1
    
    
    return sum(new_arr)

# reverse string  ფუნქცია:

def solution(string):
    #return string[: :-1]       :)
   
    alpha_str = " "    
    i = len(string)                  # i = 0     
    while i > 0:                     # while i < len(string):
        alpha_str +=string(i-1)           #alpha_str +=string(-1-i)         
        i-=1                              #i+=1         
    return alpha_str                 # return alpha_str


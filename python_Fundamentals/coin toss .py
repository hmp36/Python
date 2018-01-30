#def CoinToss(x):
import random

def toss(reps):
    attempt_count=1
    head_count = 0
    tail_count = 0    
    result = "" 
    result_sting_complete = ""

    for i in range (1,reps): 
        new_toss = random.randint(0,1)  
        if new_toss == 1:
           head_count += 1
           result ="head"  
           print "Attempt #", attempt_count, ":Throwing a coin... It's a", result, "I... Got", head_count, "head(s) so far and", tail_count, "tail(s)so far"
        else: 
            tail_count += 1
            result = "tail"
            print  "Attempt #", attempt_count, ":Throwing a coin... It's a", result, "I... Got" , head_count, "head(s) so far and", tail_count, "tail(s) so far"
        attempt_count += 1 

toss(5001)
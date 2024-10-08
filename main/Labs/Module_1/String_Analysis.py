# Problem Statement:
# You are given a string that represents an email address: "My e-mail: eMail_Address321@anymail.com". 
# Your task is to analyze the composition of the characters in the string and determine the percentage of uppercase letters, lowercase letters, 
# digits, and other characters such as symbols (#$., etc).

# To accomplish this, you need to break down the string and calculate the percentage for each category. The results are as follows:
# Uppercase letters: 7.5% Lowercase letters: 65% Digits: 7.5% Other characters (symbols): 20%

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1 :
# Input :
# Support1@litwork.in

# Output :
# 5.263% 78.947% 5.263% 10.526%

# Exercise-2 :
# Input:
# Client.1234@litwork.in

# Output:
# 4.545% 63.636% 18.182% 13.636%

import sys
def doSomething(inputVal):
    tc = len(inputVal)
    uc = sum(1 for char in inputVal if char.isupper())
    lc = sum(1 for char in inputVal if char.islower())
    ds = sum(1 for char in inputVal if char.isdigit())
    os = tc - (uc + lc + ds)
    
    ucp = (uc/tc)*100
    lcp = (lc/tc)*100
    dsp = (ds/tc)*100
    osp = (os/tc)*100
    
    return ucp, lcp, dsp, osp
inputVal = input("")
uppercase,lowercase,digits,other = doSomething(inputVal)
print(f"{uppercase:.3f}%")
print(f"{lowercase:.3f}%")
print(f"{digits:.3f}%")
print(f"{other:.3f}%")
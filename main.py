import string
import random

s1 = list(string.digits)
s2 = list(string.ascii_lowercase)
s3 = list(string.ascii_uppercase)
s4 = list(string.punctuation)


while True:
    try:
        char_number = int(input("Enter number of characters: >> "))
        if char_number < 6:
            print("You need at least 6 characters")
        elif char_number > 52:
            print("Number must not exceed 52 characters")    
        else:
            break    
    except:
        print("You must enter a valid number")    
    
    
    
random.shuffle(s1)    
random.shuffle(s2)  
random.shuffle(s3)    
random.shuffle(s4)     

part1 = round(char_number * (30/100)) 
part2 = round(char_number * (20/100)) 

password = []

for i in range(part1):
    password.append(s2[i])
    password.append(s3[i])
    
for i in range(part2):
    password.append(s1[i])
    password.append(s4[i])   
    
password = "".join(password) 
print(f"Your password is ready, Here you are: {password}")
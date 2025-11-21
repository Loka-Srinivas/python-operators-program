prime_list=[]
for num in range(1,21):
    if num>1:            
        is_prime=True    
        for i in range(2, num):
            if num % i==0:   
                is_prime =False
            break
        
        if is_prime:
            prime_list=prime_list+[num]
print("prime number from 1 to 20:", prime_list)            


# Write a count the number of occurances of a character in a string
# eg: enter a character:'a'
# string='venkata Narayana'
# output: a is repeated 6 times

# text = input("Enter a string:")   
# ch = input("Enter a character:")        
# count = 0                                
# for c in text:                           
#     if c == ch:                         
#         count +=1                       

# print("The character", ch, "repeated", count, "times.")


# num = int(input("Enter a number:"))
# fact = 1
# i = 1
# found = False
# while fact <= num:
#     if fact == num:
#         print("It is factorial of", i)
#         found = True
#         break
#     i+= 1
#     fact*= i
# if not found:
#     print("It is not a factorial of any number")



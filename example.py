num=int(input("enter a number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev) 


primelist=[]
for num in range(1,100):
    if num>1:            
        isprime=True    
        for i in range(2, num):
            if num % i==0:   
                isprime =False
            break
        
        if isprime:
            primelist=primelist+[num]
print("prime number from 1 to 100:", primelist) 


         

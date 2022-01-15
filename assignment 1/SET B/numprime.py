#write a python program to check prime number
num=int(input("Enter a number=="))
if num>1:
     for i in range(2,num):
         if num%i==0:
              print("number is not prime")
              break
         else:
              print("number is prime")
              break
else:
     print("enter a positive number")  

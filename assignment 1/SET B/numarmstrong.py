#write a python program to check armstrong number
num=int(input("Emter a number::"))
sum=0
temp=num
while temp>0:
       d=temp%10
       sum+=d**3
       temp//=10
if num==sum:
       print("the number is armstrong number")       
else:
       print("the number is not armstrong number")
              

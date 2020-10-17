import math
n=int(input("Enter a Number \n"))
c=int(math.log10(num))+1
sum=0
t=n
while(c>1):
  sum=0
  while(t>0):
    sum+=t%10
    t=t/10
  t=sum
  c=int(math.log10(c)+1
if(sum==1):
  print("Magic Number")
else:
  print("Not a Magic Number")

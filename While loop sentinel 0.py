list=[]
num=1
while num != 0:
    num=int(input("Type in a number-> "))
    list.append(num)
sum=0
for element in list:
    sum=sum+element
print(sum)
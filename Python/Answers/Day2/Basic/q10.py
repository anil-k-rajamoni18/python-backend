num=int(input("enter the number to be reversed: "))
temp=num
reverse=0
while(temp!=0):
    remainder=temp%10
    temp =temp//10
    reverse=reverse*10+remainder

print(f"Reversed Number is {reverse}")

# my first calculator code basic 
n=input("Enter a number: ")
m=input("Enter another number: ")
a=input("Enter an operation : ")
if a=="+":
    print(int(n)+int(m))
elif a=="-":
 print(int(n)-int(m))
elif a=="*":
    print(int(n)*int(m))
elif a=="/":
    print(int(n)/int(m))
else:
    print("Invalid operation")



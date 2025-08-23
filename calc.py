# calculator

print ("claculator")
print ("_"*30)
print ("the choices \n1. Addition \n2.subtraction \n3.multiplication \n4.division")
choice = int(input("enter your choice : "))
a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
if choice ==1:
    print("addition is : ",a+b)
elif choice == 2:
    print("subtraction is :  ",a-b)
elif choice == 3:
    print("multiplecation is : ",a*b)
elif choice == 4:
    print(f"division is : {a/b}")


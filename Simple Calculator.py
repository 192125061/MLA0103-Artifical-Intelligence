x=int(input("X="))
n=int(input("n="))
choice=int(input("Enter the choice:"))
if(choice==1):
    print("Sum")
    print(x+n)
elif(choice==2):
    print("Subraction")
    print(x-n)
elif(choice==3):
    print("Multiplication")
    print(x*n)
elif(choice==4):
    print("Division")
    print(x/n)
elif(choice==5):
    print("Power")
    print(x**n)
else:
    print("Invalid")

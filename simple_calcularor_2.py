def addition(a,b):
    return a+b
    
def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def floordivison(a,b):
    return a//b

def remainder(a,b):
    return a%b

print("1.Additon:")
print("2.subtraction:")
print("3.multiplication:")
print("4.Normal division:")
print("5.floor division:")
print("6.Remainder:")
print("7.Exit")

choise=int(input("Enter your choise:"))

if choise in [1,2,3,4,5,6]:

 a=int(input("Enter first number:"))
 b=int(input("Enter second number:"))

if choise==1:
    print("sum is",addition(a,b))
    
elif choise==2:
    print("subtraction is:",subtraction(a,b))
    
elif choise==3:
    print("Multiplication is:",multiplication(a,b))
    
elif choise==4:
    print("Normal Division is:",division(a,b))
    
elif choise==5:
    print("floor division is:",floordivison(a,b))
    
elif choise==6:
    print("Remainder is:",remainder(a,b))
    
elif choise==7:
    print("Exit")
    
else:
    print("Invaild number:")
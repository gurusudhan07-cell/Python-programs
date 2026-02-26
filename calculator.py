x = int(input("ENTER 1st VALUE : "))
y = int(input("ENTER 2nd VALUE : "))
o = input("ENTER ONLY THE SYMBOL SPECIFIED (+,-,*,/,%,**) : ")

if(o == "+"):
    print(f"The addition of {x} and {y} is {x+y}")
elif(o == "-"):
    print(f"The subtraction of {x} and {y} is {x-y}")
elif(o == "*"):
    print(f"The multiplication of {x} and {y} is {x*y}")
elif(o == "/"):
    print(f"The Division of {x} and {y} is {x/y}")
elif(o == "%"):
    print(f"The remainder after divide {x} by {y} is {x%y}")
elif(o == "**"):
    print(f"The exponent of {x} and {y} is {x**y}")
else:
    print("Invalid Operation!")

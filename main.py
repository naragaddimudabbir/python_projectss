try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    o =input("press the operation you want to perform--->\nAddition press +\nSubtraction press -\nmultiplicaiton *\ndivision press /\nEnter the Operation : ")

    match o:
        case"+":
            print(f"the result is: {a+b}")
        case"-":
            print(f"the result is: {a-b}")        
        case"*":
            print(f"the result is: {a*b}")
        case"/":
            print(f"the result is: {a/b}")
        case default:
            print(f"there was an error")                

except Exception as e:
    print("Entered number a or b is invalid")

from art import logo

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b 

def calculator():

    print(logo)

    first_num=float(input("What's the first number?:"))

    terminate =False
    while not terminate:
        op={
            "+":add,
            "-":subtract,
            "*":multiply,
            "/":divide,
        }

        for symbol in op:
            print(symbol)

        operation_input=input("Pick one of the operations above:")
        sec_num=float(input("What is the next number?:"))

        calculation_function=op[operation_input]  

        output=calculation_function(first_num,sec_num) 

        print(f"{first_num} {operation_input} {sec_num} = {output}")


        if(input("Press y to continue with {output} or press n to end program ")=='y'):
            first_num=output 
        else:
            print("Thank you for using our calculator!!")
            terminate=True

calculator()
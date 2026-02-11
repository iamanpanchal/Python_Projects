num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
while True:
    op = (input("Enter oprator number (+,-,/,*,%) : "))
    if(op == '+' or op == '-' or op == '/' or op == '*' or op == '%'):
        break
    else:
        print("Invalid oprator! Try again!")
        continue
    
def cal(a,b,op):
    if(op == '+'):
        print(f"Addition : {a+b}")
    elif(op == '-'):
        print(f"Subtraction : {a-b}")
    elif(op == '/'):
        print(f"Division : {a/b}")
    elif(op == '*'):
        print(f"Multiplication : {a*b}")
    else:
        print(f"Modulo : {a%b}")


cal(num1,num2,op)
def sum(x , y):
  return x+y
def subtract(x , y):
  return x-y  
def multiply(x , y):
  return x*y
def divide(x , y):
  return x/y    
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
operator = input("Enter the operator +,-,*,/ :")
if (operator == '+'):
    print(sum(number1 , number2))
elif (operator == "-") :
    print(subtract(number1 , number2))
elif  (operator == "*") :
    print(multiply(number1 , number2))
elif (operator == "/") :
    print(divide(number1 , number2))
else :
    print('invalid operator') 
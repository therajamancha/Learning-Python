first = input("Enter First Number : ")
operator = input("Enter Operator ( +  -  * /  % ) : ")
second = input("Enter Second NUmber : ")

first = int(first)
second =  int(second)

if operator == "+" :
  print("The Sum is :",first + second)
elif operator == "-" :
  print("The Sum is :",first - second)
elif operator == "*" :
  print("The Sum is :",first * second)
elif operator == "/" :
  print("The Sum is :",first / second)
elif operator == "%" :
  print("The Sum is :",first % second)
else:
  print("Enter Valid Operator")
  
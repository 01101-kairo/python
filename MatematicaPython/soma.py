def minus(num1, num2):
    return num1 - num2

def sum(num1, num2):
    return num1 + num2

def multi(num1, num2):
    return num1 * num2

def division(num1, num2):
    return print(num1 // num2, "resto", num1%num2)


var1 = float(input("numero:"))
simbo = input("qual seu cauculo:")
var2 = float(input("numero:"))
if simbo == '-':
    print(minus(var1, var2))
elif simbo == '+':
    print(sum(var1, var2))
elif simbo == '*':
    print(multi(var1, var2))
elif simbo == '/':
    division(var1, var2)
else: print("wtf")

num1=int(input("Ingrese 1er valor"))
num2=int(input("Ingrese 2do valor"))
num3=int(input("Ingrese 3er valor"))
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)

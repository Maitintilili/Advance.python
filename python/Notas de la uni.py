nota1=int(input("ingrese valor:"))
nota2=int(input("ingrese valor:"))
nota3=int(input("ingrese valor:"))
prom=(nota1+nota2+nota3)/3
if prom>=70:
    print("Pasaste Felicidades")
else:
    if prom>=60:
        print("Casi lo logras")
    else:
        print("Reprobado")

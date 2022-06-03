
lista=[]
x=int(input('ingrese la cantidad de datos'))
for i in range (x):
    y=int(input("ingrese el dato"))
    lista.append(y)

lista_a=[]
for i in range(x):
    if i-1 < 0 :
         c=(0+lista[i]+lista[i+1])
         lista_a.append(c)
    elif i+1 >= x:
        c=(lista[i-1]+lista[i]+0)
        lista_a.append(c)
    else:
        c=(lista[i-1]+lista[i]+lista[i+1])
        lista_a.append(c)
    print(lista_a)

print (lista_a)





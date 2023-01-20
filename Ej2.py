a = (1,2,3)
b = (-1,0,2)
producto = 0
lista=[]
for i in a:
    producto = a[i-1]*b[i-1]
    print(f"El producto de los valores {a[i-1]} y {b[i-1]} es {producto}")
    lista.append(producto)

print(lista)

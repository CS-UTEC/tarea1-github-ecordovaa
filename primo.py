x = int(input("Ingrese un número entero: "))
if x==2:
    print("EL numero 2 es primo")
    exit()
for i in range(x//2,1,-1):
    if x%i == 0:
        print("\nEl número "+str(x)+" es primo.")
        exit()
print("\nEl némero "+str(x)+" no es primo")
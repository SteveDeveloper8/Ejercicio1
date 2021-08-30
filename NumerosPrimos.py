num = int(input("Ingrese un numero: "))
acum = 0

    cont = 0
    dato = 3;
    while acum != num:
        for i in range(2,dato):
            for j in range(0,i):
                resto = i%j;
                print("{} % {} = {}".format(num,i,resto))
                if resto == 0:
                    cont += 1


            if cont == 0:
                print ("El {} es un numero primo".format(num))
                acum++
            else:
                print("El {} no es un numero primo".format(num))




#TAREA CARLOS JOEL SÁNCHEZ GALAN SOFTWARE C1
#PARA PODER CAMBIAR LA EJECUCION DE UN EJERCICIO EN ESPECIFICO SOLO SE NECESITA CAMBIAR EL NOMBRE DEL EJERCICIO AL QUE QUEREMOS EJECUTAR
#NO LOGRE CREAR UN MENU PARA EJECUTAR LOS EJERCICIO POR CONSOLA, ESTE TEMA SE HABIA ACORDADO EN ENSEÑAR EN CLASES Y NO SUCEDIO, UNA DISCULPA.
from types import coroutine
class Ejercicios:
    def Ejercicio1_4(self):
        numero1 = int(input("ingrese 1er numero: "))
        numero2 = int(input("ingrese 2do numero: "))
    
        suma = numero1+numero2
        rest = numero1-numero2
        multip = numero1*numero2
        division = numero1/numero2
        mod = numero1%numero2
        print("La suma es {}, la resta es {}, la multiplicación {}, la división {} y el módulo {}.".format(suma,rest,multip,division,mod))
    
    def Ejercicio1_5(self):
        numeroa = int(input("ingrese 1er numero: "))
        numerob = int(input("ingrese 2do numero: "))
        numeroc = int(input("ingrese 3er numero: "))

        resolv1 = (-numerob + (((numerob**2)-(4*numeroa*numeroc))**(0.5)))/(2*numeroa)
        resolv2 = (-numerob - (((numerob**2)-(4*numeroa*numeroc))**(0.5)))/(2*numeroa)

        print("Sus valores son:{} y {}".format(resolv1,resolv2))

    def Ejercicio1_6(self):
        
        ladoa = int(input("Ingrese 1er lado (en cm): "))
        ladob = int(input("Ingrese 2do lado (en cm): "))

        hipot = (((ladoa**2)+(ladob**2))**(0.5)) 

        print("Su hipotenusa es: ",hipot)

    def Ejercicio1_7(self):
    
        digito = int(input("Ingrese un número: "))
        binario = digito%2
        
        if binario == 0:
            print("0")
        else:
            print("1")
        
    def Ejercicio1_9(self):
        digito1 = input("Ingrese un número binario de 4 dígitos: ")

        b = int(digito1[0]) + int(digito1[1]) + int(digito1[2])+ int(digito1[3])

        rb = b%2
        if rb == 0:
            digito1 = digito1 + "0"
        else:
            digito1 = digito1 + "1"
        print(digito1)

    def Ejercicio1_10(self):
        digitbin = input("Ingrese número binario de cuatro dígitos: ")
        print(digitbin)
        bin = ((2*(int(digitbin[0])))**3) + ((2*(int(digitbin[1])))**2) + ((2*(int(digitbin[2])))**1) + ((2*(int(digitbin[3])))**0)
        print(bin)

    def Ejercicio1_11(self):
        digito4= input("Ingrese número binario de cuatro dígitos: ")

        print("Unidades: ",(digito4[3]))
        print("Decenas: ",(digito4[2]))
        print("Centenas: ",(digito4[1]))
        print("Unidades de mil: ",(digito4[0]))
        
    def Ejercicio2_1(self):
        fecha = int(input("Ingrese fecha (ddmmaaaa): "))
        conv = str(fecha)
        c = int(conv[4] + conv[5] + conv[6] + conv[7])
        lb = [(c%400),(c%4),(c%100)]
        
        res = False
        if lb[1] == 0 and not(lb[2] == 0):
            res = True

        if lb[0] == 0 or res:
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")

    def Ejercicio2_3(self):
        digit5 = int(input("Ingrese un número de 5 dígitos: "))
        conv5 = str(digit5)
    
        if conv5[0] == conv5[4] and conv5[1] == conv5[3]:
            print("Es un número capicúa, hasta luego.")
        else:
            print("No es un número capicúa, hasta luego.")

    def Ejercicio2_4(self):
        horas = int(input("Ingrese las horas: "))
        minutos = int(input("Ingrese los minutos: "))
        print("Su resultado es: {} segundos",((horas*3600)+(minutos*60)))

    def Ejercicio2_5(self):
        valor = int(input("Ingrese valor (en segundos): "))
        while valor <= 0:
            valor = int(input("Por favor, ingrese un valor positivo (en segundos): "))
        
        valorb = [(valor/60),(valor/3600),(valor/86400)]

        print("El equivalente en minutos es {}, en horas son {} y en días es {}.".format(valorb[0],valorb[1],valorb[2]))

    def Ejercicio2_6(self):
        ns = [0]*3
        ab = ["primer","segundo","tercer"]
        ct= 0

        while ct <= 2:
            ns[ct] = int(input("Ingrese "+ ab[ct] + " número: "))
            ct= ct + 1
        
        if ns[0] > ns[1] and ns[0] > ns[2]:
            pn = ns[0]
            if ns[1] > ns[2]:
                sn = ns[1]
            else: 
                sn = ns[2]
        else:
            if ns[1] > ns[0] and ns[1] > ns[2]:
                pn = ns[1]
                if ns[0] > ns[2]:
                    sn = ns[0]
                else:
                    sn = ns[2]
            else:
                pn = ns[2]
                if ns[0] > ns[1]:
                    sn = ns[0]
                else:
                    sn = ns[1]

        print("El primer valor mayor es: {} y el segundo mayor es: {}.".format(pn,sn))

    def Ejercicio2_7(self):
        t1 = [0, 0, "", 0, 0, ""]
        t2 = [0]*2
        pbs = ["Hora de entrada", "Minutos excedentes de entrada", 2, "Hora de salida", "Minutos excedentes de salida", 5]
        ct = 0

        for i in pbs:
            if (ct != 2 or ct != 5):
                if (i != 2 and i != 5):
                    t1[ct] = int(input("Ingrese {}: ".format(i)))
                ct += 1
            if ct == 2 or ct == 5:
                a = input("La hora que ingresó es AM o PM? ")
                t1[(pbs[ct])] = a
        
        t2[0] = (t1[0] * 3600) + (t1[1] * 60)
        t2[1] = (t1[3] * 3600) + (t1[4] * 60)

        if t1[2] == t1[5]:
            nhp = t2[1] - t2[0]
        else:
            nhp = (43200 - t2[0]) + t2[1]
        
        t2[0] = (nhp-(nhp % 3600)) / 3600
        t2[1] = (nhp%3600)/60
        print(t2)
        mp = t2[0] * 4

        if t2[1] >= 30:
            mp = mp + 2.50
        print("El dueño del vehículo deberá pagar Bs. ",mp)    

    def Ejercicio2_8(self):
        Cl = ["No está cumpli8endo con el criterio de ingreso", "posee infra peso", "posee bajo peso", "posee peso normal", "posee sobrepeso", "tiene obesidad pre-mórbida", "tiene obesidad mórbida","tiene obesidad híper-mórbida"]
        peso = int(input("Ingrese su peso en libras: "))
        estat = int(input("Ingrese su estatura en centímetros: "))
        
        imc = (peso * 0.453592) / ((estat*0.01)**2)

        if imc > 45:
            i = Cl[7]
        elif imc > 40:
            i = Cl[6]
        elif imc > 30:
            i = Cl[5]
        elif imc > 25:
            i = Cl[4]
        elif imc > 18.5:
            i = Cl[3]
        elif imc > 17:
            i = Cl[2]
        elif imc > 16:
            i = Cl[1]
        else:
            i = Cl[0]
        
        print("Su peso en kilogramos es {} y por ende su IMC es de {} significa que {}.".format((peso*0.453592), imc, i))

    def Ejercicio2_9(self):
        ma = {"ENERO": 31, "FEBRERO": 59, "MARZO": 90, "ABRIL": 120, "MAYO": 151, "JUNIO": 181, "JULIO": 212, "AGOSTO": 243, "SEPTIEMBRE": 273, "OCTUBRE": 304, "NOVIEMBRE": 334, "DICIEMBRE": 365}
        fechadia = int(input("Ingrese el día: "))
        fechames = input("Ingrese el mes: ").upper()
    
        for i in ma:   
            if i == fechames:
                print("Han pasado {} días.".format(((ma[i])+fechadia)))

    def Ejercicio2_10(self):
        meses = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8, "Septiembre":9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12}

        numeromes = int(input("Ingrese un número del 1 al 12: "))

        for i in meses:
            if numeromes == meses[i]:
                print("El Mes correspondiente es: ",i)

    def Ejercicio3_1(self):
        montop = int(input("Ingrese su monto a pagar: "))
        t = montop
        if montop > 1000:
            t = t - (montop * 0.2)
        print("Su monto a pagar es Bs ",t)

    def Ejercicio3_1(self):
        digit = int(input("Ingrese su número: "))
        digit = str(digit)
        print("{} tiene {} dígitos".format(digit, len(digit)))

    def Ejercicio3_2(self):
        numcop = int(input("Ingrese su número: "))
        t = True
        cti = 0
        numcop = str(numcop)
        ctf = len(str(numcop)) - 1
        
        while t:
            if ctf - cti == 1 or ctf - cti == 2:
                t = False
    
            if numcop[cti] == numcop[ctf]:
                det = True
            else:
                det = False
            cti += 1
            ctf -= 1
        if det:
            print("Es un número capicúa.")
        else:
            print("No es un número capicúa.")

    def Ejercicio3_3(self):
        nump = int(input("Ingrese un número: "))
        i = "No es primo"

        if nump%2 != 0:
            i = "Es primo"
        print("El número ingresado",i)

    def Ejercicio3_4(self):
        numfac = int(input("Ingrese número factorial "))
        r = 1
        for i in range(1, numfac+1, 1):
            r = i * r
        print(r)

    def Ejercicio3_5(self):
        numcontraseña = 0
        r = True
        while r:
            if len((str(numcontraseña))) < 10: 
                numcontraseña = int(input("Ingrese la contraseña: "))
                if len((str(numcontraseña))) == 10:
                    r = False
        print("Su contraseña cumple con los requisitos correctamente, hasta luego. :)")

    def Ejercicio3_6(self):
        numva = 1
        cont = -1
        b = []
        valorm = 0
        valormn = valorm
        while numva != 0:
            numva = int(input("Ingrese un número: "))
            b.append(numva)
            cont += 1
            if cont == 1:
                if numva > valorm:
                    valormn = valorm
                    valorm = numva
                else:
                    valormn = numva
            elif cont ==0:
                valorm = b[0]
            
            if cont >= 1:
                if numva != 0:
                    if numva > valorm:
                        valorm = numva       
                    if numva < valormn:
                        valormn = numva
                else:
                    break

        print("El número menor es: {} y el número mayor es: {}. Hasta luego.".format(valormn,valorm))


    def Ejercicio3_7(self):
        valora = 0
        p = ["La edad", "El peso(En Kg.)", "La estatura(En Cm.)"]
        lm = [24, 74, 182, 30, 70, 170, 41, 60, 169, 22, 75, 183, 31, 83, 178, 35, 76, 172, 22, 68, 164, 23, 77, 163,
            23, 58, 163, 26, 89, 185, 23, 55, 162, 26, 47, 160, 26, 60, 163, 22, 54, 170, 23, 58, 165, 26, 75, 178,
            24, 65, 170, 28, 82, 177, 42, 85, 183, 25, 75, 174, 35, 53, 150, 19, 60, 169, 35, 59, 160, 45, 74, 162,
            40, 58, 160, 33, 69, 167, 55, 70, 158, 24, 64, 160, 29, 79, 180, 52, 69, 160, 42, 78, 169, 34, 63, 152, 0] 
        per = [0, 0, 0,0]
        ac = [0, 0, 0]
        ct = 0
        while valora < 3: 
            ac[valora] = ac[valora] + lm[ct]
            
            if lm[ct] == lm[96] or lm[ct] == lm[95] or lm[ct] == lm[94]:
                valora += 1
                ct = 0
                ct += valora
            else:
                if valora == 0:
                    if lm[ct]>18 and lm[ct]<25:
                        per[0] += 1
                        per[3] += lm[ct+1]
                elif lm[ct]>36:
                        per[1] += 1
                ct += 3
        
        for i in p:
            ct+=1
            print("{} promedio de todas las personas en la muestra es {}".format(i,round(((ac[ct-4])/32))))

        print("Hay {} personas con edad entre los 18 y 25 años con un peso promedio de {}".format(per[0],round((per[3]/per[0]))))
        print("Hay {} personas mayores a 36 años".format(per[1]))


    def Ejercicio3_8(self):
        for a in range(1, 11, 1):
            for d in range (1, 13, 1):
                print("{} * {} = {}".format(a, d, (a*d)))
            print("*"*34)

    def Ejercicio3_9(self):
        a = 0
        ct = 0

        for s in range(0, 7, 1):
            for j in range(s,7,1):
                print(s," ", j) 
            
    def Ejercicio3_10(self):
        nump = 1
        t = 0
        ct = 0
        a = ["Ingrese", "Error, Ingrese"]
        b = 0
        while nump != 0:
            nump = int(input(a[b] + " un número positivo: "))
            if nump>1:
                b = 0
                t += nump
                ct += 1 
            else:
                b = 1

        print("Su promedio de la serie dada es: ",(t/(ct)))
        
    def Ejercicio4_1(self):
        decision = input("Hola! :) , ¿Desea ingresar datos? Sí (y) o No (n) ")
        
        if decision.lower() == "y":
            print("Si desea salir, ingrese una 'x'")
            promedio = Ejercicios()
            pro = promedio.SoliUser(decision)
            if pro != 0:
                print("El promedio de las edades mayores a 18 años es: ",pro)
            elif pro == 0:
                print("No hay edades mayores a 18 años.")
            else:
                print("Dado que no ha dado valores, no hay promedio.")
        else:
            print("Hasta luego ;).")

    def SoliUser(self,a):
        le = []
        while a.lower() != "x":
            b = input("Ingrese edad: ")
            if b  == "x":
                a = "x"
            elif b != "x" and int(b) <= 0:
                print("Ingrese un valor acorde por favor, o 'x' para dejar de ingrear datos.")
            elif int(b) > 18: 
                le.append(int(b))
                

        if len(le) > 0:
            print(le)
            pr = (sum(le))/len(le)
        else:
            pr = 0
        
        return pr

    def Ejercicio4_2(self):
        numerobase = int(input("Ingrese la base: "))
        numelevar = int(input("Ingrese su exponente: "))
        exp = Ejercicios()
        ex = exp.Eleva(numerobase,numelevar)
        print("El resultado de elevar {} a la {} es {}".format(numerobase,numelevar,ex))
        
    def Eleva(self,ba,ex):
        re = ba**ex
        return re

    def Ejercicio4_3(self):
        la = int(input("Ingrese el lado del polígono: "))
        per = Ejercicios()
        pe = per.PerPenta(la)
        print("El perímetro del pentágono es: {}".format(pe))
        
    def PerPenta(self,la):
        res = la*5
        return res

    def Ejercicio4_4(self):
        id = {}
        acp = Ejercicios()

        while len(id) <= 4:
            a = input("Ingrese su identificación(nombre): ")
            id[a] = int(input("Ingrese horas trabajadas{}: ".format(a)))
        th = int(input("Ingrese el monto por hora: "))

        ss = acp.CalSalSem(id,th)
        for i in ss:
            print(i,"cobrará",ss[i][1])

    def CalSalSem(self,a,re):
        Cacp = Ejercicios()
        for i in a:
            if a[i] <= 40:
                a[i] = [a[i],(a[i]*re)]
            else:
                a[i] = [a[i],(40*re)]
                a[i][1] = Cacp.CalIngHExt(a[i],re)
        print("*"*20)
        return a

    def CalIngHExt(self,k,et):
        extr = k[1] + ((k[0]-40) *(et + (et * 0.35)))
        return extr

    def Ejercicio4_5(self):
        Cal = Ejercicios()
        dp = ["primer","segundo","tercer","cuarto"]
        ct = 0
        while ct < 5:
            aciudad = input("Ingrese el {} par de Ciudad:\n1. ".format(dp[ct]))
            bciudad = input("2. ")
            ccd = int(input("Ingrese la distancia entre la ciudad {} y {}: ".format(aciudad,bciudad)))
            Cmk = Cal.Calmikm(aciudad,bciudad,ccd)
            print("Entre la ciudad de {} y la de {} hay {} Km".format(aciudad,bciudad,round(Cmk,2)))
            ct+=1

    def Calmikm(self,a,b,c):
        kmc = 1.60935
        res = c * kmc
        return res

sauce = Ejercicios()
sauce.Ejercicio3_8() #REEMPLACE "EJERCICIO3_8" POR UNO ESPECIFICO 
#PARA PODER CAMBIAR LA EJECUCION DE UN EJERCICIO EN ESPECIFICO SOLO SE NECESITA CAMBIAR EL NOMBRE DEL EJERCICIO AL QUE QUEREMOS EJECUTAR
#EN LA LINEA 475 DEBEMOS CAMBIAR EL NOMBRE AL EJERCICIO QUE QUEREMOS INVOCAR Y EJECUTAMOS
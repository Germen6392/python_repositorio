print("Factura de electricidad")


def menu():
    print("opcion 1: tarifa residencial")
    print("opcion 2: tarifa comercial")
    print("opcion 3: salir")

    
menu()


#el periodo que se toma entre lecturas es bimestral pero despues se facturara mensual
#es valido en tarifa comercial o residencial


opcion = int(input("ingrese una opcion del menu (en numero): "))

def salir():
    if opcion == 3:
        print("usted decidio salir. gracias por utilizar el programa")
# datos
precio_kw = [4.47,7.54]
cargo_fijo=[61.44,85.22]
impuesto=1.21
alum_pb=[950,1010]
ing_bruto=0.25
iva=1.21
# opciones del programa
if opcion == 1:
    print("tarifa residencial")
    
    lectura_anterior =int(input("ingrese lectura periodo anterior: "))
    lectura_actual =int(input("ingrese lectura periodo actual: "))
    consumo = lectura_actual - lectura_anterior
    subtotal = cargo_fijo[0] + impuesto + alum_pb[0]

    monto = precio_kw[0] * consumo + subtotal

    monto_mens = monto / 2

    if consumo <= 400:
        bonif = 250
        tot_mens = round(monto_mens - bonif,2)

#monto_mens = monto mensual
#tot_mens = total mensual
#bonif = bonificacion

    
        print(f"su factura es de {consumo}kw, tiene ahorro y debe abonar ${tot_mens}")

    else:
        print(f"su factura es de {consumo}kw, esta excedido y debe abonar ${monto_mens}")


elif opcion == 2:
   print("tarifa comercial")
    
   lectura_anterior =int(input("ingrese lectura periodo anterior: "))
   lectura_actual =int(input("ingrese lectura periodo actual: "))
   consumo = lectura_actual - lectura_anterior
   
   subtotal = cargo_fijo[1] + alum_pb[1] + iva + ing_bruto

   monto = precio_kw[1] * consumo + subtotal

   monto_mens = monto / 2

   if consumo <= 500:
        bonif = 180
        tot_mens = round(monto_mens - bonif,2)


        print(f"su factura es de {consumo}kw, tiene ahorro y debe abonar ${tot_mens}")

   else:
        print(f"su factura es de {consumo}kw, esta excedido y debe abonar ${monto_mens}")
else:
   salir() 

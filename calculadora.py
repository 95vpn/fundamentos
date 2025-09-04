def validar(message):
    #while se ejecutará varias veces, finalizará cuando se ejecute return 
    while True:
        try:
            #En esta linea pedimos un valor de tipo flotante
            data = float(input("Coloca " + message));
            #Si el valor es de tipo flotante regresamos el valor
            return data;
        except ValueError:
            #Se imprime el mensaje cuando surge un error en el try
            print("El dato debe de ser entero o decimal")

#Datos de entrada
largo = validar(("Coloca el largo en metros: "));
ancho = validar(("Coloca el ancho em metros: "));
m2Xcaja = validar(("Coloca los metros cuadrados por caja: "));
precioXm2 = validar(("Coloca el precio por metro cuadrado: "));

"""Regla de tres
1m2=$162
1.5m2=$
"""
precioXcaja = (m2Xcaja * precioXm2);
#Estamos obteniendo los metros cuadrados
m2Cuarto = largo * ancho;
cajas = m2Cuarto/m2Xcaja;
precioTotal = cajas * precioXcaja;
print("Total de cajas que se necesitan ", cajas);
print("Precio total: ", precioTotal);


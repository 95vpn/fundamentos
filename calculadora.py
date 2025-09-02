def validar(message):
    while True:
        try:
            data = float(input("Coloca " + message));
            return data;
        except ValueError:
            print("El dato debe de ser entero o decimal")


largo = validar(("Coloca el largo en metros: "));
ancho = validar(("Coloca el ancho em metros: "));
m2Xcaja = validar(("Coloca los metros cuadrados por caja: "));
precioXm2 = validar(("Coloca el precio por metro cuadrado: "));

precioXcaja = (m2Xcaja * precioXm2);
m2Cuarto = largo * ancho;
cajas = m2Cuarto/m2Xcaja;
precioTotal = cajas * precioXcaja;
print("Total de cajas que se necesitan ", cajas);
print("Precio total: ", precioTotal);


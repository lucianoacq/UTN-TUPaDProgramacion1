# TP integrador – Repetitivas, Condicionales y Secuenciales.


# Ejercicio 1— “Caja del Kiosco”

nombre_cliente = input("Porfavor, ingrese su nombre: ")
while not nombre_cliente.isalpha() or not nombre_cliente:
    nombre_cliente = input("Porfavor, ingrese su nombre: ")

cantidad_de_productos = input("Ingrese la cantidad de productos que va a comprar: ")
while not cantidad_de_productos.isdigit() or int(cantidad_de_productos) <= 0:
    cantidad_de_productos = input("Ingrese la cantidad de productos que va a comprar: ")
cantidad_de_productos = int(cantidad_de_productos)

total_sin_descuento = 0
total_con_descuento = 0
productos = ""

for n in range (1, cantidad_de_productos + 1):
    
    precio_producto = input(f"Ingrese el precio del producto {n}: ")
    while  not precio_producto.isdigit() or int(precio_producto) <= 0:
        precio_producto = input(f"Ingrese el precio del producto {n}: ")
    precio_producto = int(precio_producto)

    descuento = input(f"Ingrese si el producto {n} tiene descuento (S/N): ")
    while descuento.upper() != "S" and descuento.upper() != "N":
        descuento = input(f"Ingrese si el producto {n} tiene descuento (S/N): ")
    
    descuento = descuento.upper()

    if descuento == "S":
        precio_final = precio_producto * 0.10
        precio_final = precio_producto - precio_final
    else:
        precio_final = precio_producto
    

    total_sin_descuento += precio_producto
    total_con_descuento += precio_final

    productos += f"Producto {n} - Precio: {precio_producto} Descuento (S/N): {descuento}\n"


ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_de_productos

print(f"Nombre del cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_de_productos}")
print(productos, end="")
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

acceso = False

for n in range (1, 3 + 1):
    print(f"Intento {n}/3 - ", end="")
    usuario = input("Ingrese su usuario: ")
    clave_actual = input("Ingrese su clave: ")

    if usuario == "alumno" and clave_actual == "python123" :
        print("Acceso concedido.")
        acceso = True
        break
    elif n < 3:
        print("Error: credenciales inválidas.")
    else:
        print("Cuenta bloqueada")

if acceso == True:
    while True:
            print("1)Estado | 2)Cambiar Clave | 3)Mensaje | 4)Salir")
            opcion = input("Opcion: ")
            while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
                    print("Error: ingrese un número válido.")
                    opcion = input("Opcion: ")
            opcion = int(opcion)
            if opcion == 1:
                print("Inscripto")
            elif opcion == 2: 
                nueva_clave = input("Nueva clave: ")
                while len(nueva_clave) < 6 :
                    print("Error: mínimo 6 caracteres.")
                    nueva_clave = input("Nueva clave: ")
            elif opcion == 3:
                print("No importa cuán despacio vayas, siempre y cuando no te detengas")
            elif opcion == 4:
                break


# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

operador = input("Ingrese el nombre del operador: ")
while not operador.isalpha():
    print("Error: ingrese su nombre correctamente")
    operador = input("Ingrese el nombre del operador: ")

lunes1, lunes2, lunes3, lunes4 = "", "", "", ""
martes1, martes2, martes3 = "", "", ""

while True:
    print("1) Reservar turno | 2) Cancelar turno | 3)  Ver agenda del día | 4) Ver resumen general | 5) Cerrar sistema ")
    accion = input("Opcion: ")
    while not accion.isdigit() or int(accion) < 1 or int(accion) > 5:
        print("Error: ingrese una opcion válida.")
        accion = input("Opcion: ")
    accion = int(accion)

    if accion == 1:
        dia_seleccionado = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia_seleccionado.isdigit() or int(dia_seleccionado) < 1 or int(dia_seleccionado) > 2:
            print("Error, elija una de las opciones correctamente")
            dia_seleccionado = input("Elegir día (1=Lunes, 2=Martes): ")
        dia_seleccionado = int(dia_seleccionado)

        nombre_paciente = input("Indique su nombre: ")
        if dia_seleccionado == 1:
            while not nombre_paciente.isalpha() or nombre_paciente.upper() == lunes1 or nombre_paciente.upper() == lunes2 or nombre_paciente.upper() == lunes3 or nombre_paciente.upper() == lunes4:
                print("Error: nombre inválido o ya existe en este día")
                nombre_paciente = input("Indique su nombre: ")
            if lunes1 == "":
                lunes1 = nombre_paciente.upper()
                print("Turno reservado")
            elif lunes2 == "":
                lunes2 = nombre_paciente.upper()
                print("Turno reservado")
            elif lunes3 == "":
                lunes3 = nombre_paciente.upper()
                print("Turno reservado")
            elif lunes4 == "":
                lunes4 = nombre_paciente.upper()
                print("Turno reservado")
            else:
                print("No hay turnos disponibles este dia")

        if dia_seleccionado == 2:
            while not nombre_paciente.isalpha() or nombre_paciente.upper() == martes1 or nombre_paciente.upper() == martes2 or nombre_paciente.upper() == martes3:
                print("Error: nombre inválido o ya existe en este día")
                nombre_paciente = input("Indique su nombre: ")
            if martes1 == "":
                martes1 = nombre_paciente.upper()
                print("Turno reservado")
            elif martes2 == "":
                martes2 = nombre_paciente.upper()
                print("Turno reservado")
            elif martes3 == "":
                martes3 = nombre_paciente.upper()
                print("Turno reservado")
            else:
                print("No hay turnos disponibles este dia")

    if accion == 2:
        dia_seleccionado = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia_seleccionado.isdigit() or int(dia_seleccionado) < 1 or int(dia_seleccionado) > 2:
            print("Error, elija una de las opciones correctamente")
            dia_seleccionado = input("Elegir día (1=Lunes, 2=Martes): ")
        dia_seleccionado = int(dia_seleccionado)

        nombre_paciente = input("Indique su nombre: ")
        if dia_seleccionado == 1:
            while not nombre_paciente.isalpha():
                print("Error: nombre inválido")
                nombre_paciente = input("Indique su nombre: ")
            if lunes1 == nombre_paciente.upper():
                lunes1 = ""
                print("Turno cancelado")
            elif lunes2 == nombre_paciente.upper():
                lunes2 = ""
                print("Turno cancelado")
            elif lunes3 == nombre_paciente.upper():
                lunes3 = ""
                print("Turno cancelado")
            elif lunes4 == nombre_paciente.upper():
                lunes4 = ""
                print("Turno cancelado")
            else:
                print("Nombre no encontrado en este día")

        if dia_seleccionado == 2:
            while not nombre_paciente.isalpha():
                print("Error: nombre inválido")
                nombre_paciente = input("Indique su nombre: ")
            if martes1 == nombre_paciente.upper():
                martes1 = ""
                print("Turno cancelado")
            elif martes2 == nombre_paciente.upper():
                martes2 = ""
                print("Turno cancelado")
            elif martes3 == nombre_paciente.upper():
                martes3 = ""
                print("Turno cancelado")
            else:
                print("Nombre no encontrado en este día")

    if accion == 3:
        dia_seleccionado = input("Elegir día (1=Lunes, 2=Martes): ")
        while not dia_seleccionado.isdigit() or int(dia_seleccionado) < 1 or int(dia_seleccionado) > 2:
            print("Error, elija una de las opciones correctamente")
            dia_seleccionado = input("Elegir día (1=Lunes, 2=Martes): ")
        dia_seleccionado = int(dia_seleccionado)

        if dia_seleccionado == 1:
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        if dia_seleccionado == 2:
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    if accion == 4:

        ocupado_lunes = 0
        if lunes1 != "":
            ocupado_lunes += 1
        if lunes2 != "":
            ocupado_lunes += 1
        if lunes3 != "":
            ocupado_lunes += 1
        if lunes4 != "":
            ocupado_lunes += 1

        ocupado_martes = 0
        if martes1 != "":
            ocupado_martes += 1
        if martes2 != "":
            ocupado_martes += 1
        if martes3 != "":
            ocupado_martes += 1

        libres_lunes = 4 - ocupado_lunes        
        libres_martes = 3 - ocupado_martes

        print(f"Lunes: {ocupado_lunes} ocupados, {libres_lunes} libres")
        print(f"Martes: {ocupado_martes} ocupados, {libres_martes} libres")

        if ocupado_lunes > ocupado_martes:
            print("El dia con mas turnos es el lunes")
        elif ocupado_lunes < ocupado_martes:
            print("El dia con mas turnos es el martes")
        else:
            print("Empate")

    if accion == 5:
        break


# Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

nombre_agente = input("Ingrese el nombre del agente: ")
while not nombre_agente.isalpha():
    print("Error, ingrese el nombre correctamente")
    nombre_agente = input("Ingrese el nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:    
    if alarma and tiempo <= 3:
        print("SISTEMA BLOQUEADO POR ALARMA")
        break
    
    print(f"ESTADO ACTUAL\nEnergia: {energia}\nTiempo: {tiempo}\nCerraduras Abiertas: {cerraduras_abiertas}\nAlarma: {alarma}")

    menu = input("1) FORZAR CERRADURA | 2) HACKEAR PANEL | 3) DESCANSAR: ")
    while not menu.isdigit() or menu not in("1","2","3"):
        print("Error, ingrese una opcion correctamente")
        menu = input("1) FORZAR CERRADURA | 2) HACKEAR PANEL | 3) DESCANSAR: ")
    menu = int(menu)
    if menu == 1:
        print("Forzando cerradura...")
        forzar_seguidas += 1
        energia = energia - 20
        tiempo = tiempo - 2

        if forzar_seguidas == 3:
            alarma = True
            forzar_seguidas = 0
            print("Se bloqueo la cerradura")
        else:
            if energia <= 40:
                print("Energia baja! Hay riesgo de activar la alarma.")
                pedir_numero = input("INGRESE UN NUMERO DEL 1 AL 3: ")
                while not pedir_numero.isdigit() or pedir_numero not in("1","2","3"):
                    print("Error, ingrese un numero correctamente")
                    pedir_numero = input("INGRESE UN NUMERO DEL 1 AL 3: ")
                pedir_numero = int(pedir_numero)
                if pedir_numero == 3:
                    alarma = True
                    print("Fallaste! Se activo la alarma!")
                else:
                    cerraduras_abiertas += 1
                    print("Cerradura abierta con exito.")
                    forzar_seguidas = 0
            else:
                cerraduras_abiertas += 1
                print("Cerradura abierta con exito")
                forzar_seguidas = 0

    elif menu == 2:
        forzar_seguidas = 0
        print("Hackeando panel...")
        energia = energia - 10
        tiempo = tiempo - 3

        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta con exito")
            codigo_parcial = ""

    elif menu == 3:
        forzar_seguidas = 0
        print("Descansando...")
        energia = energia + 15
        if energia > 100:
            energia = 100
        tiempo = tiempo - 1
        if alarma == True:
            energia = energia - 10
            print("Alarma activa: se consumió energía extra")
    
if cerraduras_abiertas == 3:
    print("¡VICTORIA! La bóveda está abierta")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: te quedaste sin recursos")
elif alarma == True and tiempo <= 3:
    print("DERROTA")


# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

print("--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input("Ingrese el nombre del gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error, ingrese un nombre correctamente")
    nombre_gladiador = input("Ingrese el nombre del gladiador: ")
print("=== INICIO DEL COMBATE ===")

vida_gladiador = 100.0
vida_enemigo = 100.0
pociones = 3
ataque_pesado = 15
golpe_critico = ataque_pesado * 1.5
ataque_enemigo = 12
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    panel = input("Elige accion: \n1. Ataque pesado\n2. Rafaga veloz\n3. Curar\nOpcion: ")
    while not panel.isdigit() or panel not in("1", "2", "3"):
        print("Error: Ingrese un número válido.")
        panel = input("Elige accion: \n1. Ataque pesado\n2. Rafaga veloz\n3. Curar\nOpcion: ")
    panel = int(panel)

    if panel == 1:
        if vida_enemigo < 20:
            vida_enemigo -= golpe_critico
            print(f"GOLPE CRITICO! Atacaste al enemigo por {golpe_critico:.1f} puntos de daño")
        else:
            vida_enemigo -= ataque_pesado
            print(f"Atacaste al enemigo por {ataque_pesado} puntos de daño")
        
        vida_gladiador -= ataque_enemigo
        print("¡El enemigo contraataca por 12 puntos!")
        print("=== NUEVO TURNO ===")

    elif panel == 2:
        for i in range(3):
            vida_enemigo -= 5
            print("¡Golpe conectado por 5 de daño!")

        vida_gladiador -= ataque_enemigo
        print("¡El enemigo contraataca por 12 puntos!")
        print("=== NUEVO TURNO ===")

    elif panel == 3:
        if pociones > 0:
            vida_gladiador += 30
            if vida_gladiador > 100:
                vida_gladiador = 100
            pociones -= 1
            print("Tu gladiador se curo 30 de vida")
        else:
            print("¡No quedan pociones!")
        vida_gladiador -= ataque_enemigo
        print("¡El enemigo ataca por 12 puntos!")
        print("=== NUEVO TURNO ===")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")

elif vida_enemigo > 0:
    print("DERROTA. Has caído en combate.")
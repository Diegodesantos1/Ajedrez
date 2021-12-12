def ajedrez_partida():
    tablero_inicial = "♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖"
    tablero = []
    for i in tablero_inicial.split("\n"):
            tablero.append(i.split("\t"))
    print(tablero_inicial)
    movimiento =  0
    while True: #Creo el bucle para preguntar si quiere hacer más movimientos el jugador
        continuar = input("¿Deseas hacer otro movimiento? si o no ")
        if continuar != "si":
            break
        else:
            fila_origen = int(input("Introduce la fila de la pieza a mover: "))
            columna_origen = int(input("Introduce la columna de la pieza a mover: "))
            if fila_origen and columna_origen == "♜" or "♞" or "♝" or "♛" or "♚" or "♟" or "♙" or "♖" or "♘" or "♗" or "♕" or "♔":
                print ("Hay ficha")
                fila_destino = int(input("Introduce la fila de destino: "))
                columna_destino = int(input("Introduce la columna de destino: "))
            else:
                print("No hay ficha, seleccione otro movimiento")
                break
            tablero[fila_destino - 1][columna_destino - 1] = tablero[fila_origen - 1][
                columna_origen - 1
            ]
            tablero[fila_origen - 1][columna_origen - 1] = ""
            movimiento += 1
            for i in tablero: # Con esto convierto las listas en una cadena formada por los elementos de la lista.
                print('\t'.join(i) + '\n') #Cohesionado todo
            print(f"Llevas {movimiento} movimientos")
ajedrez_partida()
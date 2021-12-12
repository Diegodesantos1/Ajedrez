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
            fila_destino = int(input("Introduce la fila de destino: "))
            columna_destino = int(input("Introduce la columna de destino: "))
ajedrez_partida()

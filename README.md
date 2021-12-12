## Ajedrez
1. [Introducción](#Introducción)
2. [Flowchart](#Flowchart)
3. [Código](#Código)
***


<h1 align="center">1.Introducción</h1>

<B>Este es el link del [Repositorio](https://github.com/Diegodesantos1/Ajedrez)</B>

*He creado un programa en cual es capaz de printear un tablero de ajedrez y después poder mover las fichas a la posición que quieras, teniendo en cuenta si hay ficha o no hay ficha, con un contador de movimientos incluido*
***

<h1 align="center">2.Diagrama de flujo</h1>

<center><img src="https://github.com/Diegodesantos1/Ajedrez/blob/main/Flowchart%20ajedrez.drawio.png" alt="Flowchart"></center>

*Para verlo más claro pincha [aquí](https://github.com/Diegodesantos1/Ajedrez/blob/main/Flowchart%20ajedrez.drawio.png)*

***
<h1 align="center">3.Código</h1>

```python
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
                print(" ".join(i))
            print(f"Llevas {movimiento} movimientos")
ajedrez_partida()

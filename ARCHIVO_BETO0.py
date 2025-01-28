################################# AJEDREZ COMPLETO ? #################################
import time
import copy


columnas = ["A","B","C","D","E","F","G","H"]
letras = ["A","B","C","D","E","F","G","H"]
filas = [0,1,2,3,4,5,6,7,8]

#ASIGNACION DE PIEZAS##########
peon_blanco = "♙"
peon_negro = "♟"

torre_blanca = "♖"
torre_negra = "♜"

caballo_blanco = "♘"
caballo_negro = "♞"

alfil_blanco = "♗"
alfil_negro = "♝"

reina_blanca = "♕"
reina_negra = "♛"

rey_negro = "♚"
rey_blanco = "♔"
###############################
global movimientos
movimientos=0
fichas_negras= { "♚" : "ficha_negra", "♛" : "ficha_negra","♝" : "ficha_negra","♞" : "ficha_negra","♜" : "ficha_negra","♟" : "ficha_negra"}


def renovar_tablero(): #Esta funcion renueva el tablero, vacia las jugadas y vuelve a situar
                       #las piezas en su posicion original.
    tablero=[["_ " for i in range(8)]for j in range(8)]      # CREA UN TABLERO VACIO #




                                                         #Rellena el tablero con las piezas#
    for m in range(8):
            tablero[1][m]=peon_negro
            tablero[6][m]=peon_blanco

    tablero[0][0] = tablero[0][7] = torre_negra
    tablero[7][0] = tablero[7][7] = torre_blanca
        
    tablero[0][1] = tablero[0][6] = caballo_negro
        
    tablero[7][1] = tablero[7][6] = caballo_blanco
        
    tablero[0][2] = tablero[0][5] = alfil_negro
    tablero[7][2] = tablero[7][5] = alfil_blanco
        
    tablero[0][3] = reina_negra
    tablero[7][3] = reina_blanca
        
    tablero[0][4] = rey_negro
    tablero[7][4] = rey_blanco

                                                    #Nos devuelve el tablero lleno#
    return tablero


tablero=renovar_tablero()

#Asignamos el resultado de la función "renovar_tablero" a la variable tablero#





# Esta funcion lo que hace es mostrar la lista de tablero en forma de tablero #

def mostrar_tablero():
    print("\n\n\n")
    print("            ",columnas)

    variable=-1
    for m in range(len(tablero)):

        variable+=1
        print("          ",variable,tablero[m])

    print("            ",columnas)

###############################################################################
mostrar_tablero()

def pedir_movimientos():

    while True:

        
        columna = input("""

    introduzca la letra donde se encuentre la ficha que desea mover:""").upper()
        if columna in letras:
            break
        print("""No existe la letra que ha introducido.

                        ꧁༺ཌ♛ɆⱤⱤØⱤ♛ད༻꧂""")



    
    while True:
        fila = int(input("    introduzca la fila donde se encuentre la ficha que desea mover:"))
        if fila in filas:
            break
        print("""No existe la fila que ha introducido.

                        ꧁༺ཌ♛ɆⱤⱤØⱤ♛ད༻꧂""")



        
    while True:
        destino_col = input("    introduzca la letra donde desee mover la ficha:").upper()
        if destino_col in letras:
            break
        print("""No existe la fila que ha introducido.

                        ꧁༺ཌ♛ɆⱤⱤØⱤ♛ད༻꧂""")



        
    while True:
        destino_fil = int(input("    introduzca la fila donde desee mover:"))
        if destino_fil in filas:
            break
        print("""No existe la letra que ha introducido.

                        ꧁༺ཌ♛ɆⱤⱤØⱤ♛ད༻꧂""")
        



    return columna, fila, destino_col, destino_fil

def sabedor_de_indices(columna, fila, destino_col, destino_fil):
        for i in range(len(letras)):
            if columna == letras[i]:
                col=i
                break
        for j in range(0,8):
            if fila == j:
                fil=j
                break
        for x in range(len(letras)):
        
            if destino_col == letras[x]:
                des_col=x
                break
        for y in range(0,8):
            
            if destino_fil == y:
                des_fil=y
                break
        return col,fil,des_col,des_fil


def mover_fichas(col,fil,des_col,des_fil):
    if tablero[fil][col] == peon_negro:
        print(tablero[fil][col])
        print("la ficha", tablero[fil][col], "mueve a la casilla", tablero[des_fil][des_col])
        movimiento_peon_negro(col, fil, des_col, des_fil)
    elif tablero[fil][col] == peon_blanco:
        print(tablero[fil][col])
        print("la ficha", tablero[fil][col], "mueve a la casilla", tablero[des_fil][des_col])
        movimiento_peon_blanco(col,fil,des_col, des_fil)
        





def movimiento_peon_negro(col,fil,des_col,des_fil):
    comer=False
    mover=False
    if des_fil == fil-1 :
        mover=True 
    elif des_fil == fil-1 and des_fil != "_ " and col-1 != "_ " or col+1!="_ ":
        comer=True

    while mover:
        tablero[fil][col], tablero[des_fil][des_col] = tablero[des_fil][des_col], tablero[fil][col]
        break
    
    while comer:
        tablero[des_fil][des_col], tablero[fil][col] = tablero[fil][col], "_ "
        break

def movimiento_peon_blanco(col,fil,des_col,des_fil):
    comer=False
    mover=False
    if des_fil == fil-1 and des_fil == "_ ":
        mover=True 
    elif des_fil == fil-1 and des_fil != "ficha_negra" and col-1 != "ficha_negra" or col+1!= "ficha_negra":
        comer=True

    while mover:
        tablero[fil][col], tablero[des_fil][des_col] = tablero[des_fil][des_col], tablero[fil][col]
        break
    
    while comer:
        tablero[des_fil][des_col], tablero[fil][col] = tablero[fil][col], "_ "
        break

        
    
juego=True

while juego:

    print("estoy en juego")

  

    columna,fila,destino_col,destino_fil=pedir_movimientos()
    
    print(columna, fila, destino_col, destino_fil,"los movimientos")
    
    col,fil,des_col,des_fil = sabedor_de_indices(columna,fila,destino_col,destino_fil)
    
    mover_fichas(col,fil,des_col,des_fil)
    
    print("Aqui se mueven las fichas")
    
    movimientos+=1
    
    print("""
            Aquí muestro tablero: 

""")
    mostrar_tablero()




####for i in range(8):
####    for j in range (8):
####        if tablero[fil-1][col] == "_ ":
####            movimiento_valido=True
####        elif tablero[fil-1][col] == ficha_negra:
####            movimiento_valido=False
####
####        if tablero[fil-1][col-1] == ficha_negra or tablero[fil-1][col+1] == ficha_negra:
####            movimiento_comer=True
####        else:
####            movimiento_comer=False
####            print( "Eso no es un movimiento valido" )
####            pedir_movimientos()

import time
import random


print("""

                    BIENVENIDO AL TRES EN RAYA


      😈​😈​😈​😈​😈​     VAS A JUGAR CONTRA MI       😈​😈​😈​😈​😈​""")



time.sleep(0.5)
print("\n")

tablero=[["_" for i in range(3)]for i in range(3)]

def mostrar_tablero(): 
    for m in tablero:
        print("                       ",m)

dificultad=int(input("""
                            1. Modo fácil
                            2. Modo difícil
                            3. Modo extremo
                            4. MODO DIABLO 😈​

            Introduzca la dificultad con la que se quiere enfrentar:
"""))

while dificultad > 4 or dificultad < 1:
    print("ERROR, no hay esa dificultad")
    dificultad=int(input("""
                            1. Modo fácil
                            2. Modo difícil
                            3. Modo extremo
                            4. MODO DIABLO 😈​

            Introduzca la dificultad con la que se quiere enfrentar:
"""))
turno=random.randint(1,2)

def intentos_jugador():
    
    print("Tu turno, jugador 1")
    vertical=int(input("Vertical: "))
    horizontal=int(input("Horizontal: "))
    intento=True
    while intento:
           
            if  tablero[vertical][horizontal]== "_":
                tablero [vertical][horizontal]="O"
                mostrar_tablero()
                intento=False
                
            else:
                print("ERROR, YA ESTÁ OCUPADO\n")
                vertical=int(input("Vertical: "))
                horizontal=int(input("Horizontal: "))



def intentos_de_maquina_facil(fila,columna):
    
    if tablero[fila][columna] == "_":
        tablero[columna][fila] = "X"


def comprobador_de_juego():

    juego=True

#COMPROBAR CON INDICES +1 +2 ?
    #COMPROBAR COLUMNAS

    # RECORRER I, RECCORRER J Y DIAGONALES POR UNA PARTE
# QUE SEAN IGUALE Y AU
    print(tablero[0][0],tablero[0][1],tablero[0][2])

    if tablero[0][0] == tablero[0][1]== tablero[0][2]:
        juego=False
    elif tablero [1][0] == "X" and tablero [1][1]== "X" and tablero [1][2] == "X":
        juego=False
    elif tablero [2][0] == "X" and tablero [2][1]== "X" and tablero [2][2] == "X":
        juego=False
    elif tablero [0][0] == "X" and tablero [1][1]== "X" and tablero [2][2] == "X":
        juego=False
    elif tablero [0][2] == "X" and tablero [1][1]== "X" and tablero [2][0] == "X":
        juego=False

    if tablero [0][0] == "O" and tablero [0][1]== "O" and tablero [0][2] == "O":
        juego=False
    elif tablero [1][0] == "O" and tablero [1][1]== "O" and tablero [1][2] == "O":
        juego=False
    elif tablero [2][0] == "O" and tablero [2][1]== "O" and tablero [2][2] == "O":
        juego=False
    elif tablero [0][0] == "O" and tablero [1][1]== "O" and tablero [2][2] == "O":
        juego=False
    elif tablero [0][2] == "O" and tablero [1][1]== "O" and tablero [2][0] == "O":
        juego=False


    return juego


def juego_en_facil(turno):

    juego=True
    

    while juego:
        
        if turno == 1:
            columna=random.randint(0,2)
            fila=random.randint(0,2)
            time.sleep(0.3)
            print("Hmm... buen intento...")
            time.sleep(0.3)
            print("Mi turno")
            intentos_de_maquina_facil(fila,columna)
            mostrar_tablero()
            turno=2
            juego=comprobador_de_juego()
        elif turno == 2:
            intentos_jugador()
            turno=1

        juego=comprobador_de_juego()


    return juego
            

    
juego=True


while juego:
    
    if dificultad == 1:
        fila=random.randint(0,2)
        columna=random.randint(0,2)
        juego=juego_en_facil(turno)




print("FIN DEL JUEGO")



        
                    

        

##        
##elif dificultad == 2:
##    juego_en_dificil()
##elif dificultad == 3:
##    juego_en_extremo()
##else:
##    modo_diablo()


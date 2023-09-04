def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")
 
 
# Uso la funcion 'def' para imprimir el tablero 
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              TABLERO       ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")
 
# Se usa la funcion para comprobar el jugador ganador 
def check_win(player_pos, cur_player):
 
    # Todas las combinaciones posibles para ganar 
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
 
    # Bucle para comprobar alguna combinación ganadora 
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):
 
            # Regresa 'True' si alguna combinación es ganadora 
            return True
    # Regresa 'Falso' cuando no satisface ninguna combinación 
    return False       
 
# Función que se aplica para comprobar que el juego esta empatado 
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False       
 
# Se aplica la función para un solo juego 
def single_game(cur_player):
 
    # Bucle que representa el juego 
    values = [' ' for x in range(9)]
     
    # Guarda las posiciones ocupadas por 'X' y 'Y' 
    player_pos = {'X':[], 'O':[]}
     
    # Bucle del programa para que sea un solo juego 
    while True:
        print_tic_tac_toe(values)
         
        # Se utliza 'try' para escoger el movimiento del jugador  
        try:
            print("Jugador ", cur_player, ". Escoge un cuadrante: ", end="")
            move = int(input()) 
        except ValueError:
            print("Error!!! Vuelve a intentarlo")
            continue
 
        # Verifica si el movimiento esta dentro del rango 
        if move < 1 or move > 9:
            print("Error!!! Vuelve a intentarlo")
            continue
 
        # Verifica si el lugar esta ocupado 
        if values[move-1] != ' ':
            print("Lugar Ocupado. Vuelve a intentarlo!!")
            continue
 
        # En esta parte del bucle se actualiza la información del juego 
 
        # Actualización del estado del juego  
        values[move-1] = cur_player
 
        # Actualiza los lugares ocupados de los jugadores 
        player_pos[cur_player].append(move)
 
        # Función que verifica al ganador 
        if check_win(player_pos, cur_player):
            print_tic_tac_toe(values)
            print("Jugador ", cur_player, " GANASTE!!")     
            print("\n")
            return cur_player
 
        # Función que verifica si el juego esta empatado 
        if check_draw(player_pos):
            print_tic_tac_toe(values)
            print("IGUANAS")
            print("\n")
            return 'D'
 
        # Cambia los movimientos del jugador 
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
 
if __name__ == "__main__":
 
    print("Jugador 1")
    player1 = input("Ingrese el nombre : ")
    print("\n")
 
    print("Jugador 2")
    player2 = input("Ingrese el nombre : ")
    print("\n")
     
    # Guarda el jugador que elige 'X' y 'O'
    cur_player = player1
 
    # Guarda la elección de los jugadores 
    player_choice = {'X' : "", 'O' : ""}
 
    # Guarda las opciones a elegir 
    options = ['X', 'O']
 
    # Guarda el tablero 
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)
 
    # Bucle del juego para una serie de TIC TAC TOE 
    # Se efectua el bucle hasta que los jugadores renuncien  
    while True:
 
        # Imprime el Menú de las opciones que tiene el jugador 
        print("Turno de elegir para", cur_player)
        print("Ingrese 1 para X")
        print("Ingrese 2 para O")
        print("Ingrese 3 para Salir")
 
        # Se utiliza ´try´ para elegir la entrada 
        try:
            choice = int(input())   
        except ValueError:
            print("Error!!! Vuelve a intentarlo")
            continue
 
        # Condiciones del juego para elegir   
        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
 
        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Puntuación Final")
            print_scoreboard(score_board)
            break  
 
        else:
            print("Error!!! Vuelve a intentarlo")
 
        # Guarda al ganador de la partida de Tic Tac Toe
        winner = single_game(options[choice-1])
         
        # Edita el tablero con el ganador 
        if winner != 'D' :
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
 
        print_scoreboard(score_board)
        # El siguiente jugador elige 'X' u 'O'
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1

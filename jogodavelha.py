tabuleiro = [[" " , " " , " "],
             [" " , " " , " "],
             [" " , " " , " "]]

jogador = "X"
vencedor = None
empate = False


while True:
    
    print()
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

    print(f"\nVez do jogador {jogador}")

    
    linha = input("Escolha a LINHA (1, 2 ou 3): ")
    coluna = input("Escolha a COLUNA (1, 2 ou 3): ")

   
    if linha.isdigit() and coluna.isdigit():
        linha = int(linha) - 1  
        coluna = int(coluna) - 1
        if 0 <= linha <= 2 and 0 <= coluna <= 2:
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador
            else:
                print("Essa posição já está ocupada. Tente outra.")
                continue
        else:
            print("Linha ou coluna fora do intervalo. Tente de novo.")
            continue
    else:
        print("Digite apenas números válidos.")
        continue

    
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
            vencedor = jogador
            break

    
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != " ":
            vencedor = jogador
            break

    
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        vencedor = jogador
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        vencedor = jogador

    
    espacos_vazios = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                espacos_vazios += 1

    if vencedor:
        print()
        for linha in tabuleiro:
            print(" | ".join(linha))
            print("-" * 9)
        print(f"\nParabéns! Jogador {jogador} venceu!")
        break
    elif espacos_vazios == 0:
        print()
        for linha in tabuleiro:
            print(" | ".join(linha))
            print("-" * 9)
        print("\nEmpate! Ninguém venceu.")
        break

    
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

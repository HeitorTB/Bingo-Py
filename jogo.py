import random
niveis = {
    0: {"players": 2, "linhas": 2, "colunas": 3, "Qnt": 6},  # Qnt é o número total de números na cartela
    1: {"players": 4, "linhas": 3, "colunas": 4, "Qnt": 12}
}

def exibir_matriz(matriz):
    for linha in matriz:
        print('  '.join(f"{num}" for num in linha))
intervalos = ((1, 10), (11, 20), (21, 30), (31, 40))

def criar_cartelas(nivel):
    matriz = []
    usados = []
    for i in range(niveis[nivel]["linhas"]):
        linha = []
        for c in range(niveis[nivel]["colunas"]):
            intervalo = intervalos[c]
            num = random.randint(intervalo[0], intervalo[1])
            while num in usados:
                num = random.randint(intervalo[0], intervalo[1])
            usados.append(num)
            linha.append(num)
        matriz.append(linha)
    return matriz

def sortear_numero(nivel, numeros_sorteados):
    config = niveis[nivel]
    colunas = config["colunas"] * 10
    while True:
        numSorted = random.randint(1, colunas)
        if numSorted not in numeros_sorteados:
            numeros_sorteados.append(numSorted)
            return numSorted

def verificar_vitoria(cartela, total_numeros):
    marcados = 0
    for linha in cartela:
        for num in linha:
            if isinstance(num, str):
                marcados += 1
    return marcados==total_numeros

def jogo(nivel):
    config = niveis[nivel]
    sorted_dezenas = []
    numeros_sorteados = []
    num_sorteado = sortear_numero(nivel, numeros_sorteados)
    cartelas = []

    for c in range(1, config["players"] + 1):
        cartela = criar_cartelas(nivel)
        cartelas.append(cartela)
    print("\n--- Cartelas dos Jogadores ---")
    for c in range(1, config["players"] + 1):
        print(f"\nCartela do Jogador {c}:")
        matriz = cartelas[c - 1]
        exibir_matriz(matriz)
    print("\nO primeiro número será sorteado agora...\n")
    while True:
        print(f"-> Número sorteado: {num_sorteado}")
        sorted_dezenas.append(num_sorteado)
        sorted_dezenas = sorted(sorted_dezenas)

        for c in range(1, config["players"] + 1):
            print(f"\nCartela do Jogador {c}:")
            matriz = cartelas[c - 1]
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] == num_sorteado:
                        matriz[i][j] = f"\033[91m{num_sorteado}\033[0m" 
            exibir_matriz(matriz)
            
            if verificar_vitoria(matriz, config["Qnt"]):
                print(f"Jogador {c} Venceu!")
                return 
        print("Dezenas sorteadas até o momento:", sorted_dezenas)

        continuar = input("Clique enter para continuar o jogo (ou 's' para sair): ")
        if continuar.lower() == 's':
            print("Jogo finalizado!")
            return
        else:
            num_sorteado = sortear_numero(nivel, numeros_sorteados)

pergunta = int(input('Indique o modo de jogo:\n0 - Rápido\n1 - Demorado \n'))
jogo(pergunta)












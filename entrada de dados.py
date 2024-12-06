def obter_notas():
    print("Bem-vindo à Calculadora de Média Escolar!")
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número.")
    return notas

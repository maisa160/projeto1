def main():
    notas = obter_notas()
    media = calcular_media(notas)
    status = verificar_aprovacao(media)
    exibir_resultado(media, status)

if __name__ == "__main__":
    main()
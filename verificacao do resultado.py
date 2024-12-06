def verificar_aprovacao(media, limite=7.0):
    if media >= limite:
        return "Aprovado"
    elif media >= limite - 0.5:  # Margem de 0.5 para mensagem personalizada
        return "Quase Aprovado (recuperação recomendada)"
    else:
        return "Reprovado"

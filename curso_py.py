dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
temperaturas = [22, 25, 23, 28, 30, 27, 24]


def media_temperatura(temperaturas):
    if not temperaturas:
        return 0
    return sum(temperaturas) / len(temperaturas)


def temperatura_maxima(temperaturas):
    if not temperaturas:
        return None
    return max(temperaturas)


def temperatura_minima(temperaturas):
    if not temperaturas:
        return None
    return min(temperaturas)


def dias_acima_da_media(dias, temperaturas):
    media = media_temperatura(temperaturas)
    dias_acima = []

    for dia, temp in zip(dias, temperaturas):
        if temp > media:
            dias_acima.append((dia, temp))

    return dias_acima, media


def resumo_semana(dias, temperaturas):
    media = media_temperatura(temperaturas)
    maior = temperatura_maxima(temperaturas)
    menor = temperatura_minima(temperaturas)
    dias_acima, _ = dias_acima_da_media(dias, temperaturas)

    print("=== Resumo da temperatura da semana ===")
    print(f"Média: {media:.1f}°C")
    print(f"Temperatura mais alta: {maior}°C")
    print(f"Temperatura mais baixa: {menor}°C")

    if dias_acima:
        print("Dias acima da média:")
        for dia, temp in dias_acima:
            print(f"- {dia}: {temp}°C")
    else:
        print("Nenhum dia ficou acima da média.")

    if media >= 25:
        print("Condição: Semana quente.")
    elif media >= 18:
        print("Condição: Semana agradável.")
    else:
        print("Condição: Semana fria.")


if __name__ == "__main__":
    resumo_semana(dias_da_semana, temperaturas)

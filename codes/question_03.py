import json

with open("files/dados.json","r") as file:
    data = list(json.load(file))

def calc_max(data: list) -> dict:
    """Função que retorna o maior faturamento em um dia do mês"""
    max, day_max = 0, 0
    for invoicing in data:

        if invoicing["valor"] > max:
            max = invoicing["valor"]
            day_max = invoicing["dia"]

    return {"dia": day_max, "valor": max}


def calc_min(data: list) -> dict:
    """Função que retorna o menor faturamento em um dia do mês considerando o 0.0 """
    min = calc_max(data)["valor"]
    day_min = 0
    for invoicing in data:

        if invoicing["valor"] < min:
            min = invoicing["valor"]
            day_min = invoicing["dia"]

    return {"dia": day_min, "valor": min}


def calc_average(data: list) -> float:
    """Função que retorna a média o faturamento mensal desconsiderando os dias de fauramento igual a 0.0"""
    counter, values = 0, 0
    for invoicing in data:
        if invoicing['valor'] > 0:
            values += invoicing['valor']
            counter += 1
    return values / counter    


def calc_highest_average_daily_revenue(data: list) -> int:
    """Função que retorna o número de dias com faturamento diário superior à média mensal"""
    monthly_average = calc_average(data)
    above_average_days = 0
    for invoicing in data:
        if invoicing["valor"] > monthly_average:
            above_average_days += 1

    return above_average_days


print(f'Maior: {calc_max(data)}')
print(f'Menor: {calc_min(data)}')
print(f'Dias com faturamento diário superior à média mensal: {calc_highest_average_daily_revenue(data)}')
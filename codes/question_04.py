
def representation_percentage_calculation() -> None:
    """Função que faz cálculo de percentual de representação por cada estado no valor total mensal"""
    invoicing = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    total = sum(invoicing.values())

    for state, value in invoicing.items():
        percentual = (value / total) * 100
        print(f"{state}, {percentual:.2f}")

representation_percentage_calculation()
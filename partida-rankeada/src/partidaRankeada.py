qtd_victory = 10
qtd_defeat = 10


def number_victorys(qtd_victory, qtd_defeat):
    balance_victory = qtd_victory - qtd_defeat
    return balance_victory


balance_victory = number_victorys(qtd_victory, qtd_defeat)
rank = ""
if balance_victory < 10:
    rank = "Ferro"
elif balance_victory >= 11 and balance_victory <= 20:
    rank = "Bronze"
elif balance_victory >= 21 and balance_victory <= 50:
    rank = "Prata"
elif balance_victory >= 51 and balance_victory <= 80:
    rank = "Ouro"
elif balance_victory >= 81 and balance_victory <= 90:
    rank = "Diamante"
elif balance_victory >= 91 and balance_victory <= 100:
    rank = "Lendario"
else:
    rank = "Imortal"


match rank:
    case "Ferro":
        print(
            f"O Herói tem de saldo de **{balance_victory}** está no nível de **{rank}"
        )
    case "Bronze":
        print(
            f"O Herói tem de saldo de **{balance_victory}** está no nível de **{rank}"
        )
    case "Prata":
        print(
            f"O Herói tem de saldo de **{balance_victory}** está no nível de **{rank}"
        )
    case "Ouro":
        print(
            f"O Herói tem de saldo de **{balance_victory}** está no nível de **{rank}"
        )
    case "Diamante":
        print(
            f"O Herói tem de saldo de **{balance_victory}** está no nível de **{rank}"
        )
    case "Lendario":
        print(
            f"O Herói tem de saldo de **{balance_victory}** está no nível de **{rank}"
        )
    case "Imortal":
        print(
            f"O Herói tem de saldo de **{balance_victory}** está no nível de **{rank}"
        )
    case _:
        print(f"Valor invalido")

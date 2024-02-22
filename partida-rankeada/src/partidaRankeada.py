"""
Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"
"""

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

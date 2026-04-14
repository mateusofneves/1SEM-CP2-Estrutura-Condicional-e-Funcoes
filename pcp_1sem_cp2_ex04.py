#PEGANDO VALORES! :O
nome = input("Digite o nome do coloborador: ")
cargo = input("Digite o cargo do funcionario: ")
salario_base = float(input("Digite o valor do seu salario: "))
horas_ex = input("Digite o número de horas extras trabalhadas: ")
faltas = input("Digite o número de faltas do mês: ")
bonus = bool(input("recebeu bonûs por desempenho (s/n): ").lower().startswith('s'))

#TOTAL DE BONUS COM HORAS EXTRAS E CARGO
def bonus_geral (bonus_h, bonus_c):
    acrescimos = bonus_h + bonus_c
    print(f"Seu total de acréscimos de bonûs é de: R${acrescimos:.2f}")

# CONFIGURANDO BONUS SE TIVER
if bonus:
#TABELINHA COM OS VALORES E CARGOS PERMITIDOS
    bonus_c = {
    "gerente": 1000,
    "analista": 500,
    "assistente": 300,
    "estagiario": 100
    }
#SE O CARGO EXISTIR NA TABELA BONUS RETORNA O VALOR BONUS ATRIBUIDO
if cargo in bonus_c:
    valor = bonus_c[cargo]
    print(f"Bônus de R$ {valor} atribuído ao {cargo}.")
else:
    print("sem bonûs atribuído")

#CALCULO DO BONUS POR HORA EXTRA
def bonus_por_hora_extra (salario_base, horas_ex):
    bonus_h= salario_base * 1.5 * horas_ex
    print(f"O bonûs de hora extra trabalhada é de: R${bonus_h:.2f}")




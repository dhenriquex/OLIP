import sys
#estrai o sufixo do patronimico
def extrairP(patronimico):
    terminacao_patronimico = ["evich", "ovich", "ich", "evna", "ovna", "ichna"]
    for sufixo in terminacao_patronimico:
        if patronimico.endswith(sufixo):
            return patronimico[:-len(sufixo)]
    return patronimico
#estrai o sufixo do sobrenome de familia
def extrairF(familia):
    terminacao_familia = ["eva", "ova", "ina", "ev", "ov", "in"]
    for sufixo in terminacao_familia:
        if familia.endswith(sufixo):
            return familia[:-len(sufixo)]
    return familia
# lê o nome, patronimico e sobrenome do usuário
meu_nome, meu_patronimico,meu_sobrenome= sys.stdin.readline().strip().split()
# extrai o patronimico e sobrenome do usuário
meu_patronimico = extrairP(meu_patronimico)
meu_sobrenome = extrairF(meu_sobrenome)
# lê o número de pessoas
n = int(sys.stdin.readline().strip())
# inicializa contadores para familiares e irmãos
cont_familiares = 0
cont_irmaos = 0
for _ in range(n):
    # lê o nome, patronimico e sobrenome de cada pessoa
    nome, patronimico, familia = sys.stdin.readline().strip().split()
    # extrai o patronimico e sobrenome de cada pessoa
    patronimico_base = extrairP(patronimico)
    familia_base = extrairF(familia)
    # verifica se o sobrenome e patronimico coincidem com os do usuário
    if familia_base == meu_sobrenome:
        cont_familiares += 1
        # verifica se o patronimico coincide com o do usuário
        if patronimico_base == meu_patronimico:
            cont_irmaos += 1

print(f"{cont_familiares} {cont_irmaos}")
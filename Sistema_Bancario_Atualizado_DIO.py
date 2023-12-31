import textwrap

def menu():
    menu = """
    ============== Menu ==============
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova Conta
        [lc]\tListar Contatos
        [nu]\tNovo Usuario
        [q]\tSair 
        →"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n "
    else:
        print("operação falhou: o valor informado é invalido")
    return saldo, extrato

def sacar(*, saldo, valor, extrato,limite,numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operacoes falhou! Você não tem saldo suficiente")

    elif excedeu_limite:
        print("Operção falhou! O valor do saque excedeu o limite")

    elif excedeu_saques:
        print("Operação falhou! Numero maximo de saques excedidos.")

    elif valor > 0:
        saldo += valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação Falhou! O valor informado é invalido")
    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato  ):
    print("\n ===============EXTRATO===============")
    print("Não foram realizadas movimentaçoes." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("=============================================")

def criar_usuario(usuarios):
    cpf = input("informe o cpf(somente numeros):")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\n @@@ já Existe usuario com esse CPF! @@@")
        return

    nome = input("Informe o nome Completo: ")
    data_nascimento = input("Informe a data de nascimento ( dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logadouro, nro - bairro - cidade/sigla estado):")

    usuarios.append({"nome":nome, "datade nascimento":data_nascimento, "CPF":cpf, "Endereço":endereco})
    print("================= Usuario criado com sucesso =================")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numeros_contas, usuarios):
    cpf = input("informe o CPF do usuario")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n === Conta Criada com sucesso! ===")
        return {"agencia": agencia, "numero conta": numeros_contas, "usuario": usuario}
    print("\n Usuario não encontrado, fluxo de criação de conta encerrado!")


def lista_contas(contas):
    for conta in contas :
        linha = f"""\
        Agencia:\t {conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent((linha)))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "001"


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("informar o valor do deposito: "))
            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saques,
                limite_saque=LIMITE_SAQUES,
            )


        elif opcao == "e":
           exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            lista_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalidad por favor selecione novamente a operção desejada")
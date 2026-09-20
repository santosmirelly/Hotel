#Funções
status_quartos = ["livre", "ocupado", "em limpeza"]
quartos = [{
    "num_quarto": 1,
    "nome_hospede": "0",
    "idade_hospede": "",
    "diaria":0,
    "dias":0,
    "status": status_quartos[2]
},{
    "num_quarto": 2,
    "nome_hospede": "0",
    "idade_hospede": "",
     "diaria":0,
     "dias":0,
    "status": status_quartos[0]
},{
    "num_quarto": 3,
    "nome_hospede": "0",
    "idade_hospede": "",
    "diaria":0,
    "dias":0,
    "status": status_quartos[1]
},{
    "num_quarto": 4,
    "nome_hospede": "0",
    "idade_hospede": "",
    "diaria":0,
    "dias":0,
    "status": status_quartos[1]
}, {
    "num_quarto": 5,
    "nome_hospede": "0",
    "idade_hospede": "",
     "diaria":0,
     "dias":0,
    "status": status_quartos[0]
}
]
resposta = None
def check_in():

    nome= str(input("Nome do hóspede: "))
    try:
        idade=int(input('Idade do hóspede: '))
    except ValueError:
        print("Digite uma idade válida!")
        return

    if idade <= 0:
        print("Digite uma idade válida!")
        return

    if idade < 18:
        print("O hóspede deve ser maior de idade!")
        return

    print("====QUARTOS DISPONIVEIS====\n")

    for item in quartos:
        if item["status"] == status_quartos[0]:
            print(f"Quarto {item['num_quarto']} está {item['status']}")
    try:
        escolha = int(input("\nEscolha o quarto a ser hospedado: "))
    except ValueError:
        print("Digite um número de quarto válido!")


    quarto_encontrado= False

    for item in quartos:
        if item["num_quarto"]== escolha:
            quarto_encontrado= True

            if item["status"] != "livre":
                print("\nQuarto não disponível para hospedagem.")
                continue
            try:
                diaria = int(input("Digite o valor da diária: "))
            except ValueError:
                print("Digite um valor válido para a diária!")
                continue
            if diaria <= 0:
                print("Digite um valor positivo para a diária!")
                continue
            try:
                dias = int(input("Digite a quantidade de dias de hospedagem: "))
            except ValueError:
                print("Digite uma quantidade válida de dias!")
                continue
            if dias <= 0:
                print("A quantidade de dias deve ser positiva!")
                continue

            item['nome_hospede'] = nome
            item["idade_hospede"] = idade
            item["diaria"] = diaria
            item["dias"] = dias
            item["status"] = "ocupado"
            print(
                f"\nQuarto {item['num_quarto']} foi ocupado pelo hóspede "
                f"{item['nome_hospede']}")

            print(f"Diária: R$ {item['diaria']:.2f}")
            print(f"Quantidade de dias de hospedagem: {item['dias']}")

            if quarto_encontrado == False:
                print("Esse quarto não existe. Escolha um quarto válido.")

def mapa_quartos():
    print(" =============== MAPA DE QUARTOS =============\n")
    for item in quartos:
        if item["status"] == status_quartos[0] or item["status"] == status_quartos[2]:

            print(f"O Quarto {item['num_quarto']} está {item['status']}")

        else:
            print(
                f"O Quarto {item['num_quarto']} se encontra ocupado pelo hóspede "
                 f"pelo hóspede: {item['nome_hospede']}.")

def status_quarto():
    print("\n =========== ALTERAR STATUS DO QUARTO ===============")

    for item in quartos:

        print(f"Quarto {item['num_quarto']} - {item['status']}. ")
    try:
        escolha = int(input('\n Escolha o quarto que deseja alterar: '))
    except ValueError:
        print("Coloque um número de quarto válido!")
        return
        
    quarto_encontrado = False

    for item in quartos:
        if item["num_quarto"] == escolha:
            quarto_encontrado = True

            print('''
    [1] Livre
    [2] Ocupado
    [3] Em Limpeza
                          ''')
            novo_status =input("Escolha o novo status: ")
            if novo_status == "1":
                item["status"] = "livre"

            elif novo_status == "2":
                item["status"] = "ocupado"

            elif novo_status == "3":
                item["status"] = "em limpeza"

            else:
                print("Opção Inválida!!")
                continue

            print(
                f"O quarto {item['num_quarto']} agora está: "
                f" {item['status']}."
                        )

        if quarto_encontrado == False:
            print("Esse quarto não existe.")
            
def check_out():
    print("\n============= CHECK-OUT ============") 
    for item in quartos:
        if item["status"] == "ocupado":
            print(
                f"Quarto {item['num_quarto']} - "
                f" Hóspede: {item['nome_hospede']}"
                )
    try:     
        escolha = int(input("\n Escolha o número do quarto para o Check-out: "))
    except ValueError:
        print("Digite um número de quarto válido!")
        return
    quarto_encontrado = False   

    for item in quartos:
        if item["num_quarto"] == escolha:
            quarto_encontrado = True
            if item["status"] == "ocupado":
                valor_total = int(item["diaria"]) * int(item["dias"])
                print(
                    f"Check out do hóspede"
                    f"{item['nome_hospede']} realizado."
                )

                print(f"Diária: R$ {item['diaria']:.2f}")
                print(f"Quantidade de dias de hospedagem: {item['dias']}")
                print(f"Valor total a ser pago: R$ {valor_total:.2f}")

                item["nome_hospede"] = "0"
                item["idade_hospede"] = ""
                item["diaria"] = 0
                item["dias"] = 0
                item["status"] = "em limpeza"

                print("O quarto agora está em limpeza.")

            else:
                print("Esse quarto não está ocupado.")
    if quarto_encontrado == False:
        print("Esse quarto não existe.")

def liberar_quarto():
    print("\n============== LIBERAR QUARTO ================")
    for item in quartos:
        if item["status"] == "em limpeza":
            print(f"Quarto {item['num_quarto']} está em limpeza")
    try:
        escolha = int(input("Escolha o quarto para ser liberado: "))
    except ValueError:
        print("Digite um número de quarto válido!")
        return
    quarto_encontrado = False

    for item in quartos:
        if item["num_quarto"] == escolha:
            quarto_encontrado = True
            if item["status"]  == "em limpeza":
                item["status"] = "livre"
                print(
                    f"\n Quarto {item['num_quarto']} foi liberado"
                    f" e está livre.")
            else:
                print("\n Esse quarto não está em limpeza.")

    if quarto_encontrado == False:
        print("Esse quarto não existe.")


    
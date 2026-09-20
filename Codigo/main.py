from utils import check_in, mapa_quartos, status_quarto, check_out

opcao = None

while opcao != 0:
  print('''
  [1] Realizar check-in
  [2] Exibir mapa de quartos 
  [3] Alterar status do quarto
  [4] Realizar check-out 
  [5] Liberar quarto após limpeza 
  [0] Sair 
        ''')

  opcao = int(input("Digite uma das opções acima: "))

  if opcao == 1:
    check_in()
    break

  elif opcao == 2:
    mapa_quartos()
    break

  elif opcao == 3:
    status_quarto()
    break

  elif opcao == 4:
    check_out()
    break
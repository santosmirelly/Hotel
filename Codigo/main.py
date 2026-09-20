from utils import (
  carregar_dados,
  check_in,
  mapa_quartos,
  status_quarto,
  check_out,
  liberar_quarto
)

opcao = None

carregar_dados()

while opcao != 0:
  print('''
  [1] Realizar check-in
  [2] Exibir mapa de quartos 
  [3] Alterar status do quarto
  [4] Realizar check-out 
  [5] Liberar quarto após limpeza 
  [0] Sair 
        ''')

  try:
    opcao = int(input("Digite uma das opções acima: "))
  except ValueError:
    print("Digite uma opção válida.")
    continue

  if opcao == 1:
    check_in()

  elif opcao == 2:
    mapa_quartos()

  elif opcao == 3:
    status_quarto()

  elif opcao == 4:
    check_out()

  elif opcao == 5:
    liberar_quarto()

  elif opcao != 0:
    print("Opção inválida.")
                                        #  variaveis - Carlos
agenda = {}
horarios_disponiveis = ["09:00", "10:00", "11:00", "13:00", "14:00", "15:00"]


def exibir_menu():
    print("\n--- Sistema de Agendamento de Consultas ---")
    print("1. Agendar Consulta")
    print("2. Visualizar Agenda")
    print("3. Cancelar Consulta")
    print("4. Sair")

                                        # funcoes, estruturas logicas e condicionais - Joao e Lucas
def agendar_consulta():
    nome = input("nome do paciente: ")
    print("horarios disponiveis:")
    for horario in horarios_disponiveis:
        if horario not in agenda:
            print(horario)
    horario_escolhido = input("escolha um horario: ")
    if horario_escolhido in horarios_disponiveis and horario_escolhido not in agenda:
        agenda[horario_escolhido] = nome
        print("consulta agendada.")
    else:
        print("horario indisponível ou invalido.")

def visualizar_agenda():
    if not agenda:
        print("nenhuma consulta agendada.")
    else:
        print("\nAgenda de Consultas:")
        for horario in sorted(agenda):
            print(f"{horario} - {agenda[horario]}")

def cancelar_consulta():
    horario = input("informe o horario da consulta a ser cancelada: ")
    if horario in agenda:
        del agenda[horario]
        print("consulta cancelada.")
    else:
        print("nenhuma consulta agendada nesse horario.")


                            # estrutura de repetição - Murilo
while True:
    exibir_menu()
    opcao = input("escolha uma opcao: ")
    
    if opcao == "1":
        agendar_consulta()
    elif opcao == "2":
        visualizar_agenda()
    elif opcao == "3":
        cancelar_consulta()
    elif opcao == "4":
        print("encerrando o sistema.")
        break
    else:
        print("opcaoo invalida.")

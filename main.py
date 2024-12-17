# Projeto: Gerenciador de Tarefas Simples
# Este projeto permite adicionar, listar e remover tarefas de forma simples.

# Lista para armazenar as tarefas
tarefas = []

def exibir_menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a descrição da tarefa: ")
    if tarefa.strip():
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    else:
        print("A tarefa não pode ser vazia.")

def listar_tarefas():
    if tarefas:
        print("\n=== Lista de Tarefas ===")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("\nNenhuma tarefa cadastrada.")

def remover_tarefa():
    listar_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa que deseja remover: "))
            if 1 <= indice <= len(tarefas):
                tarefa_removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

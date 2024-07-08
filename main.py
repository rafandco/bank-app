# App de banca creada por Rafael Díaz García (rafandco)

def show_balance(balance):
    print("\n----------------------------------------\n")
    print(f"Tu balance es {balance:.2f} €")
    print("\n----------------------------------------\n")

def deposit():
    amount = float(input("Introduce una cantidad a depositar: "))

    if amount < 0:
        print("\n----------------------------------------\n")
        print("No es una cantidad válida")
        print("\n----------------------------------------\n")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Introduce una cantidad a retirar: "))

    if amount < 0:
        print("\n----------------------------------------\n")        
        print("No es una cantidad válida")
        print("\n----------------------------------------\n")
        return 0
    elif amount > balance:
        print("\n----------------------------------------\n")
        print("Dinero insuficiente en el balance")
        print("\n----------------------------------------\n")
        return 0

    else:
        return amount

def main():

    balance = 0.0
    is_running = True

    while is_running:
        
        print("\n****************************************\n")
        print("\t\tBanca App")
        print("\n****************************************\n")
        print("1. Mostrar balance")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        print("\n****************************************\n")

        choice = input("Ingresa tu opción (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("\n----------------------------------------\n")
            print("No es un opción válida\n")
            print("\n----------------------------------------\n")

    print("Gracias por usar Banca App, ¡Hasta pronto!")

if __name__ == '__main__':
    main()

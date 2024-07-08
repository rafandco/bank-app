# App de banca creada por Rafael Díaz García (rafandco)

def show_balance(balance):
    print(f"Tu balance es {balance:.2f} €")

def deposit():
    amount = float(input("Introduce una cantidad a depositar: "))

    if amount < 0:
        print("No es una cantidad válida")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Introduce una cantidad a retirar: "))

    if amount < 0:
        print("No es una cantidad válida")
        return 0
    elif amount > balance:
        print("Dinero insuficiente en el balance")
        return 0

    else:
        return amount

def main():

    balance = 0.0
    is_running = True

    while is_running:
        print("Programa de banca")
        print("1. Mostrar balance")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

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
            print("No es un opción válida")

    print("Gracias por usar Banca App, ¡Hasta pronto!")

if __name__ == '__main__':
    main()

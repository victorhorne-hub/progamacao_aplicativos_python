class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado! Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado! Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente")

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


# --- Programa Principal ---

# Criando conta sem saldo inicial (assume 0 por padrão)
conta1 = ContaBancaria("Ana")

# Criando conta com saldo inicial de R$ 500
conta2 = ContaBancaria("Carlos", 500)

print("--- Extratos Iniciais ---")
conta1.extrato()
conta2.extrato()

print("\n--- Operações na Conta da Ana ---")
conta1.depositar(200)
conta1.sacar(50)    # Saque bem-sucedido
conta1.sacar(300)   # Saque recusado (saldo insuficiente)

print("\n--- Operações na Conta do Carlos ---")
conta2.depositar(150)
conta2.sacar(600)   # Saque bem-sucedido
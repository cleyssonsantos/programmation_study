class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        # print(f"{"Titular da conta".ljust(25)} | {"Saldo da conta".ljust(25)} | Status da conta")
        return f"{self.titular.ljust(25)} | {self.saldo.ljust(25)} | {self._ativo}"
    
    # @classmethod Maneira gambiarra
    # def ativar_conta(cls, conta):
    #     conta._ativo = True
    @property
    def titular(self):
        return self.titular
    
    @property
    def saldo(self):
        return self.saldo
    
    @property
    def ativo(self):
        return self._ativo


conta_um = ContaBancaria("Cleysson Santos", "1.000.000.00")
# conta_um.ativar_conta(conta_um)
conta_um.ativar_conta()
conta_dois = ContaBancaria("Julia Alvares", "1.000.000.00")

print(conta_um)
print(conta_dois)
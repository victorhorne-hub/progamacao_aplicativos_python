#2. Herança

class gerente(funcionario):

    def __init__(self, nome, salario, equipe):
        super().__init__(nome, salario)#super() chama construtor da classe
        self.equipe = equipe #atributo novo

def mostrar_equipe(self):
    print(f"{self.nome}gerencia{self.equipe}pessoas.")

class Estagiario(funcionario):
     def __init__(self, nome, salario, curso):
         super().__init__(nome, salario)
            self.curso = curso

fulano=gerente("Fulano", 150,"Fulano")
caio=Estagiario("Caio", 150,"Cairo")
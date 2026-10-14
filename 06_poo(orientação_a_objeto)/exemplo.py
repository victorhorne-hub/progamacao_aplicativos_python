#1. Classe: o modelo (planta)
from types import coroutine


class Celular:
    def __init__(self, marca, modelo, cor, bateria ):
        #Atributos: as caracteristicas do objeto
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

#4. Metodos: os comportamentos do objetos
    def ligar(self):
        # 0 metodo consulta um atributo do próprio objeto
        if self.bateria == 0:
            print("sem bateria! coloque para carregar!")
        else:
            self.ligado = True
            print("Ligado")

    def desligar(self):
        self.ligado = False
        print("Desligado")

#5. objetos: Criados apartir da classe(as casas)
celular1 = Celular("Samsung", "Galaxy s23", "preto")
celular2 = Celular("Motorola", "Moto g54", "azul", 30)

#6. Acessando e alterando atributos
#usamos objeto.atributo
print(celular1.marca)
print(celular1.modelo)
print(celular2.bateria)

#7. Chamando Métodos
#Usamos objeto.metodo() para pedir que o objeto faça algo
celular2.ligar()
celular2.desligar()
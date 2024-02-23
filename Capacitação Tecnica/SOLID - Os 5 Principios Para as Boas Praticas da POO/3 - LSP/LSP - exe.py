# 3. Liskov Substitution Principle (Princípio da Substituição de Liskov)
# Este princípio, nomeado em homenagem a Barbara Liskov, afirma que objetos de uma classe base devem poder ser substituídos por objetos de 
# classes derivadas sem quebrar a aplicação. Isso implica que as classes derivadas devem se comportar de maneira compatível com as 
# classes base das quais herdam. Violações deste princípio geralmente ocorrem quando uma subclasse altera o comportamento (não apenas estendendo) da classe base.


# Considere um sistema de gerenciamento de veículos para um jogo ou simulação que inclui diferentes tipos de veículos, como Carro, 
# Caminhao, e Bicicleta. Todos esses veículos têm métodos como acelerar e frear, mas alguns veículos, como Bicicleta, possuem comportamentos
# específicos que não se aplicam a outros, como pedalar e não podem executar ações como ligarMotor, presentes em veículos motorizados.

class Veiculo:
    def ligarMotor(self):
        print("Motor ligado")

    def acelerar(self):
        print("Veículo acelerado")

    def frear(self):
        print("Veículo freado")

class Carro(Veiculo):
    def acelerar(self):
        super().ligarMotor()  # Necessário para carros
        print("Carro acelerado")

class Bicicleta(Veiculo):
    def acelerar(self):
        print("Bicicleta acelerada com pedaladas")

    def ligarMotor(self):
        # Implementação vazia ou lançamento de exceção, pois bicicletas não têm motor
        raise NotImplementedError("Bicicletas não têm motor")

class Veiculo:
    def acelerar(self):
        print("Veículo acelerado")

    def frear(self):
        print("Veículo freado")

class Veiculo_Motorizado(Veiculo):
    def ligarMotor(self):
        print("Motor ligado")

class Carro(Veiculo_Motorizado):
    def acelerar(self):
        super().ligarMotor()
        print("Carro acelerado")

class Bicicleta(Veiculo):
    def acelerar(self):
        print("Bicicleta acelerada com pedaladas")

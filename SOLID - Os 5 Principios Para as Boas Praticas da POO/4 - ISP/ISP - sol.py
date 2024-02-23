class Dispositivo:
    def ligar(self):
        pass

    def desligar(self):
        pass

class DispositivoComVolume:
    def ajustarVolume(self, volume):
        pass

class DispositivoComBrilho:
    def ajustarBrilho(self, brilho):
        pass

class DispositivoComCanal:
    def mudarCanal(self, canal):
        pass

class Lampada(Dispositivo, DispositivoComBrilho):
    def ligar(self):
        print("Lâmpada ligada")

    def desligar(self):
        print("Lâmpada desligada")

    def ajustarBrilho(self, brilho):
        print(f"Ajustando brilho para {brilho}")

class CameraSeguranca(Dispositivo, DispositivoComCanal):
    def ligar(self):
        print("Câmera ligada")

    def desligar(self):
        print("Câmera desligada")

    def mudarCanal(self, canal):
        print(f"Ajustando canal para {canal}")
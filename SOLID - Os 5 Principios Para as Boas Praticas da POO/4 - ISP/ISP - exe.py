# Contexto
# Considere um sistema de sensores para uma estação meteorológica inteligente que coleta diferentes 
# tipos de dados ambientais, como temperatura, umidade, e velocidade do vento. O sistema atual implementa 
# uma interface genérica Sensor com métodos para cada tipo de medição, independentemente do fato de que nem todos os 
# sensores suportam todos os tipos de medição.

# Atividade Proposta
# Implementação Inicial: Comece com uma implementação que viola o ISP, onde uma única interface Sensor define métodos para várias medições.

# Identificação de Problemas: Analise o código para identificar onde o ISP pode ser violado.

# Refatoração Conforme o ISP: Refatore o código para criar interfaces específicas para cada tipo de medição, garantindo que os 
# sensores implementem apenas os métodos relevantes para suas capacidades.

class DispositivoInteligente:
    def ligar(self):
        pass

    def desligar(self):
        pass

    def ajustarVolume(self, volume):
        pass

    def mudarCanal(self, canal):
        pass

    def ajustarBrilho(self, brilho):
        pass

class Lampada(DispositivoInteligente):
    def ligar(self):
        print("Lâmpada ligada")

    def desligar(self):
        print("Lâmpada desligada")

    # Lampada não usa os métodos abaixo, violando o ISP
    def ajustarVolume(self, volume):
        pass

    def mudarCanal(self, canal):
        pass

    def ajustarBrilho(self, brilho):
        print(f"Ajustando brilho para {brilho}")

class CameraSeguranca(DispositivoInteligente):
    def ligar(self):
        print("Câmera ligada")

    def desligar(self):
        print("Câmera desligada")

    # Lampada não usa os métodos abaixo, violando o ISP
    def ajustarVolume(self, volume):
        pass

    def mudarCanal(self, canal):
        print(f"Ajustando canal para {canal}")

    def ajustarBrilho(self, brilho):
        pass
    
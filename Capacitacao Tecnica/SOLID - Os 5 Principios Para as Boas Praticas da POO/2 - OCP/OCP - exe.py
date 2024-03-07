# 2. Open/Closed Principle (Princípio Aberto/Fechado)
# Este princípio sugere que as entidades de software (classes, módulos, funções, etc.) devem estar abertas para extensão,
# mas fechadas para modificação. Isso significa que você pode adicionar novas funcionalidades estendendo uma classe, mas 
# sem alterar o código existente. Isso é útil para minimizar o risco de introduzir erros em código já testado e funcional.


# Imagine que você está construindo um sistema de processamento de pedidos para uma loja online. 
# Este sistema precisa calcular o preço total de um pedido, que pode incluir diferentes tipos de itens, como produtos físicos, serviços, 
# e assinaturas digitais. Cada tipo de item tem uma lógica de cálculo de preço diferente.

# Atividade Proposta
# Implementação Inicial: Comece com uma implementação que viola o OCP, onde uma única função ou classe tenta lidar 
# com o cálculo de preço para todos os tipos de itens usando condicionais.

# Refatoração Conforme o OCP: Refatore o código para usar o OCP, de modo que seja fácil adicionar novos tipos de itens no futuro sem modificar o código existente.

# Instruções para a Atividade
# Passo 1: Identifique o problema com o design atual em relação ao OCP.

# Passo 2: Crie uma classe abstrata ou interface OrderItem, com um método calculate_price que será implementado de forma diferente por cada tipo de item.

# Passo 3: Refatore as classes Product, Service, e Subscription para que cada uma herde de OrderItem e implemente seu próprio método calculate_price.

# Passo 4: Modifique a classe Order para que utilize o novo método calculate_price de cada item, eliminando a necessidade de condicionais no cálculo do preço total.

# Critérios de Avaliação
# Adesão ao OCP: O sistema deve ser facilmente extensível para suportar novos tipos de itens sem necessidade de modificar o código existente.
# Coesão e Encapsulamento: Cada tipo de item deve encapsular sua própria lógica de cálculo de preço.
# Simplicidade e Clareza: O código deve ser fácil de entender e manter.


class OrderItem:
    def __init__(self, type, price):
        self.type = type
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            if item.type == "product":
                total_price += item.price
            elif item.type == "service":
                total_price += item.price * 1.2  # Taxa de serviço de 20%
            elif item.type == "subscription":
                total_price += item.price * 0.9  # Desconto de 10% para assinaturas
        return total_price

# Contexto
# Imagine que você está desenvolvendo um sistema para uma biblioteca que gerencia livros e as transações de empréstimo. O sistema inicial que você herdou está implementado em uma única classe que realiza múltiplas tarefas, incluindo o gerenciamento de livros (adicionar, remover livros), o gerenciamento de usuários (adicionar, remover usuários) e o gerenciamento de empréstimos (realizar e devolver empréstimos).

# Atividade Proposta
# Análise do Código Existente: Você começará com um código que viola o SRP, onde uma única classe realiza todas as tarefas mencionadas acima.

# Identificação das Responsabilidades: Identifique claramente as diferentes responsabilidades dentro do código existente.

# Refatoração Conforme o SRP: Refatore o código para separar essas responsabilidades em classes distintas, cada uma com uma única responsabilidade.

# Instruções para a Atividade
# Passo 1: Divida o LibrarySystem em pelo menos três classes separadas que refletem as responsabilidades de gerenciamento de livros, usuários e empréstimos.

# Passo 2: Crie uma classe BookManager para gerenciar as operações relacionadas a livros.

# Passo 3: Crie uma classe UserManager para gerenciar as operações relacionadas a usuários.

# Passo 4: Crie uma classe LoanManager para gerenciar as operações de empréstimo, garantindo que ela interaja apropriadamente com BookManager e UserManager.

# Passo 5: Certifique-se de que cada classe segue o SRP, com métodos e propriedades claramente focados em uma única responsabilidade.

# Critérios de Avaliação
# Adesão ao SRP: Cada classe deve ter uma única responsabilidade.
# Coesão: Métodos dentro de cada classe devem ser fortemente relacionados às responsabilidades da classe.
# Acoplamento: Tente minimizar o acoplamento direto entre as classes, preferindo interações baseadas em abstrações (interfaces) quando possível.
# Esta atividade irá ajudá-lo a praticar a identificação e separação de responsabilidades dentro de um sistema, um passo crucial para escrever código limpo e manutenível. Boa sorte!

class LibrarySystem:
    def __init__(self):
        self.books = []  # Lista de todos os livros
        self.users = []  # Lista de todos os usuários
        self.loans = []  # Lista de todos os empréstimos

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def loan_book(self, user, book):
        if book in self.books:
            self.loans.append((user, book))
            print(f"{book} emprestado para {user}.")

    def return_book(self, user, book):
        if (user, book) in self.loans:
            self.loans.remove((user, book))
            print(f"{book} devolvido por {user}.")



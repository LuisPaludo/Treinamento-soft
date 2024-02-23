# 1° A classe possui uma única responsabilidade (adicionar ou remover livros)
# 2° Para BookManager os métodos são fortemente relacionados
# 3° Não há acoplamentos
class BookManager:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

# 1° A classe possui uma única responsabilidade (adicionar ou remover usuários)
# 2° Para UserManager os métodos são fortemente relacionados
# 3° Não há acoplamentos
class UserManager:
    def __init__(self) -> None:
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

# 1° A classe possui uma única responsabilidade (registrar e retornar livros de usuários)
# 2° Para LoanBookManager os métodos são fortemente relacionados
# 3° Há acoplamento com BookManager e UserManager
class LoanBookManager:
    def __init__(self, bookManager:BookManager, userManager: UserManager) -> None:
        self.loans = []
        self.bookManager = bookManager
        self.userManager = userManager

    def loan_book(self, user, book):
        if book in self.bookManager.books and user in self.userManager.users:
            self.loans.append((user, book))
            print(f"{book} emprestado para {user}.")

    def return_book(self, user, book):
        if (user, book) in self.loans:
            self.loans.remove((user, book))
            print(f"{book} devolvido por {user}.")  
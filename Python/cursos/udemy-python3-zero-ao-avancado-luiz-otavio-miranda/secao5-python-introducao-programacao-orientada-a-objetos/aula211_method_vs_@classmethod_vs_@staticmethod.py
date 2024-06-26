# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

# class Connection:
#     def __init__(self, host='localhost'):
#         self.host = host
#         self.user = None
#         self.password = None

#     def set_user(self, user):
#         self.user = user

#     def set_password(self, password):
#         self.password = password

#     @classmethod
#     def create_with_auth(cls, user, password):
#         connection = cls()
#         connection.user = user
#         connection.password = password
#         return connection

#     @staticmethod
#     def log(msg):
#         print('LOG:', msg)


# def connection_log(msg):
#     print('LOG:', msg)


# # c1 = Connection()
# c1 = Connection.create_with_auth('luiz', '1234')
# # c1.set_user('luiz')
# # c1.set_password('123')
# print(Connection.log('Essa é a mensagem de log'))
# print(c1.user)
# print(c1.password)
class Connection:
    def __init__(self, host="localhost") -> None: # Método de instância
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
        return self.user
    
    def set_password(self, password): # Se usar o self, é um método de instância
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user # Semelhante ao self, é como se estivesse setando no self
        connection.password = password

        return connection
    
    @staticmethod # Talvez faça sentido nesse caso de logs, foi um exemplo
    def log(msg):
        print(f"LOG: {msg}")


# c1 = Connection()
# c1.set_user("cleysson.santos1")
# print(c1.user)


c2 = Connection.create_with_auth("cleysson.santos1", "123456")
print(c2.user)
print(c2.password)

c3 = Connection.log("Inserido registro 3 no banco de dados.")
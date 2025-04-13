from abc import ABC, abstractmethod

# Tight Coupling (Bad) - Direct dependency
class MySQLDatabase:  # Low-level module
    def save(self, data): ...

class UserService:    # High-level module
    def __init__(self):
        self.db = MySQLDatabase()  # Directly depends on MySQL
    
    def save_user(self, user):
        self.db.save(user)  # Will break if database changes

# Loose Coupling (Good) - Depends on abstraction
class Database(ABC):  # Abstraction
    @abstractmethod
    def save(self, data): ...

class MySQLDatabase(Database):  # Implementation
    def save(self, data): ...

class UserService:
    def __init__(self, db: Database):  # Depends on interface
        self.db = db
    
    def save_user(self, user):
        self.db.save(user)  # Works with any Database implementation
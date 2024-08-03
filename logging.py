class UserManager:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def addUser(self, name):
        id = self.next_id
        self.users[id] = name
        self.next_id += 1
        return id

    def getUser(self, id):
        return self.users.get(id, None)

    def deleteUser(self, id):
        if id in self.users:
            del self.users[id]
            return True
        return False

    def findUserByName(self, name):
        found_names = []
        for user_id, user_name in self.users.items():
            if user_name == name:
                found_names.append(user_id)
        return found_names

# Пример использования
UserManager = UserManager()

# Добавление пользователей
id1 = UserManager.addUser("Alen")
id2 = UserManager.addUser("Ronaldo")
id3 = UserManager.addUser("Goat")

# Поиск пользователя по id
print(UserManager.getUser(id1))  # Вывод: "Alen"
print(UserManager.getUser(id2))  # Вывод: "Ronaldo"

# Удаление пользователя
print(UserManager.deleteUser(id1))  # Вывод: True
print(UserManager.getUser(id1))     # Вывод: None

# Поиск пользователей по имени
print(UserManager.findUserByName("Alen"))  # Вывод: [0]
print(UserManager.findUserByName("Ronaldo"))    # Вывод: [2]
print(UserManager.findUserByName("Goat"))  # Вывод: [3]

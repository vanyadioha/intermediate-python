class User:
    """Users for a hypothetical App"""

    def __init__(self, name, user_name, age, gender):
        self.name = name
        self.user_name = user_name
        self.age = age
        self.gender = gender


user_1 = User("Victor Anyadioha", "thegr8khallie", 22, "shemale")
print(user_1)

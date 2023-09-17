class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print(f"{self.name} is {self.age} years old.")
    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill
    def special_skill(self):
        print(f"{self.name} has a special hunting skill: {self.hunting_skill}")
    def play_fetch(self):
        print(f"{self.name} loves to play fetch.")
class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength
    def show_strength(self):
        print(f"{self.name} is known for its strength: {self.strength}")
    def snore_loudly(self):
        print(f"{self.name} is known to snore loudly.")
dog1 = Dog("Rex", 3, "Brown")
dog2 = JackRussellTerrier("Max", 2, "White", "Excellent")
dog3 = Bulldog("Buddy", 4, "Brindle", "Very strong")
dog1.description()
dog1.get_info()
dog2.description()
dog2.get_info()
dog2.special_skill()
dog2.play_fetch()
dog3.description()
dog3.get_info()
dog3.show_strength()
dog3.snore_loudly()

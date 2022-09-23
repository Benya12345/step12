from Lesson_1.Charter1 import Character
class Berserk(Character):
    def __init__(self, name, hp, damage, armor):
        Character.__init__(self, name, hp, damage, armor)


    def count_addition_damage(self):
        return(self.max_hp - self.max_hp) / self.max_hp * self.damage
    def attack(self, target):
            target.take_damage(self.damage + self.count_addition_damage())



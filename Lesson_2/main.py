from berserk import Berserk
from Lesson_1.Charter1 import Character
p1 = Berserk(name = 'Taste player', hp = 100, damage = 7, armor = 0)
p2 = Character(name = 'player', hp = 100, damage = 10, armor = 0)
while p1.hp > 0 and p2.hp > 0:
    print(p1)
    print(p2)
    p1.attack(p2)
    p2.attack(p1)
    print()
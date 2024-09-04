
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = int(health_points)
        self.catchphrase = catchphrase
        self.damage = int(damage)
        self.fly = fly

    def info_name(self):
        print('Имя героя:', self.name)

    def double_health(self):
        self.health_points **= 2
        self.fly = True
        print(f'Здоровье героя удвоено: {self.health_points}')

    def true_phrase(self):
        print(f'True in the true phrase: {self.catchphrase}')

    def __str__(self):
        return (f"Прозвище: {self.nickname}\n"
                f"Суперспособность: {self.superpower}\n"
                f"Здоровье: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Stiven Rodjers", "Captain America", "Flight", "200", "I can do this all day", "150")

hero.info_name()
hero.double_health()
print(hero)
print(f"Длина коронной фразы героя: {len(hero)}")


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, endurance='endurance'):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.endurance = endurance


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, speed='speed'):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage=0)
        self.speed = speed


air_hero = AirHero("Clark Kent", "Superman", "Flying", 200, "Up, up and away!", 70)
earth_hero = EarthHero("Joakin Rafael Phoenix", "Joker", "Doing magic tricks", 170, "Compassion is the movie's superpower", speed="80")

air_hero.double_health()
earth_hero.true_phrase()

print(air_hero)
print(earth_hero)


class Villain(AirHero):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, endurance):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, endurance)

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2
        print(f'Возводен в степень урон: {self.damage}')


villain = Villain("Lex Luthor", "Lex", "Genius intellect", 150, "I'm not a villain. I'm just ahead of the curve.", 100, "high")

villain.crit()

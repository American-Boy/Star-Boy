class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def info_name(self):
        print('Имя героя:', self.name)

    def double_health(self):
        self.health_points *= 2
        print(f'Здоровье героя удвоено: {self.health_points}')

    def __str__(self):
        return (f"Прозвище: {self.nickname}\n"
                f"Суперспособность: {self.superpower}\n"
                f"Здоровье: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Stiven Rodjers", "Captain America", "Flight", "200", "I can do this all day")


hero.info_name()
hero.double_health()
print(hero)
print(f"Длина коронной фразы героя: {len(hero)}")
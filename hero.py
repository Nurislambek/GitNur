class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def __str__(self):
        return f'name is {self.name} \n' \
               f'nickname is {self.nickname} \n' \
               f'superpower is {self.superpower} \n' \
               f'health_points is {self.health_points} \n' \
               f'catchphrase is {self.catchphrase}'

    def nick_superpower_health(self):
        print(self.nickname,self.superpower,self.health_points)

    def __len__(self):
        return len(self.catchphrase)

hero_name = SuperHero('SuperMan')
print(hero_name)
hero_health = SuperHero('50%')
print(hero_health * 2)
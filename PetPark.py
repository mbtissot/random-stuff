class Park:
    def __init__(self, max_pets):
        self.max_pets = max_pets
        self.petlist = []

    def add_pet(self, pet):
        vagas = self.max_pets - len(self.petlist)
        if vagas > 0:
            self.petlist.append(pet)
            vagas = self.max_pets - len(self.petlist)
            print(f'Pet {pet.name} adicionado ao parque. Ainda temos {vagas} vagas')
        else:
            print(f'Pet {pet.name} nao adicionado. Já tem pets demais no parque')


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.petlist = []

    def print_name(self):
        print(f'Meu nome é {self.name}')

    def print_age(self):
        print(f'Minha idade é {self.age} anos')

    def change_age(self, age):
        self.age = age
        print('Mudaram minha idade')


'''
Classe Dog e Cat são classe 'filha' da classe 'Pet'. Então aproveita todos os
métodos já definidos por Pet
'''


class Cat(Pet):
    def meow(self):
        print('Miau')


class Dog(Pet):
    def bark(self):
        print('Auau')


d = Dog('Luna', 5)
d.print_name()
d.print_age()
d.bark()
d.change_age(7)
d.print_age()

k = Cat('Kim', 1)
k.print_name()
k.print_age()
k.meow()

b = Dog('Bud', 6)
b.print_name()
b.print_age()
b.bark()

park1 = Park(2)
park1.add_pet(d)  # printando o nome do primeiro pet que tem no parque.

park1.add_pet(k)

park1.add_pet(b)  # falhou ao adicionar o pet pois ja tem pets demais

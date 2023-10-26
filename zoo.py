class Zoo:
    __animals = 0

    def __init__(self, names):
        self.names = names
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, sepcies, name):
        self.species = sepcies
        self.name = name
        if self.species == "mammal":
            self.mammals.append(name)
        elif self.species == "fish":
            self.fishes.append(name)
        elif self.species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        self.species = species
        result_to_print = ""
        if species == "mammal":
            result_to_print += f"Mammals in {self.names}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            result_to_print += f"Fishes in {self.names}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            result_to_print += f"Birds in {self.names}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        return result_to_print


name_of_the_zoo = input()
zoo = Zoo(name_of_the_zoo)
number_lines = int(input())

for line in range(number_lines):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))

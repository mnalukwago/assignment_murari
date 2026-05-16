class House:
    def __init__(self, type, color, location):
        self._type = type
        self.color = color
        self.location = location
    # any property of a class that starts with an underscore is a private property
    def clean_house(self):
        print(f"My {self._type} needs to be cleared twice a week")

# demonstrated the principle of Encapsulation
house1 = House("flat", "brown", "Bunga")
print(house1._type)

house1.clean_house()

# class Hut(self, type, color, location, size, owner):

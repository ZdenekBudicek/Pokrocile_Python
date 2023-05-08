# Máte zadanou tuto classu
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Vytvořte 3 objekty (instance) podle classy
# dokážete vysvětlit, jaký je vztah mezi classou a objektem?
dog_1 = Dog("Max", 3)
dog_2 = Dog("Bady", 150)
dog_3 = Dog("Brit", 5)


# Vytvořte funkci, která určí nejstaršího psa z vámi zadaných

# Definuju že to jsou argumenty a ten ty čísla změní na Tuple, pak mu jen řeknu že vezmi maximum
def oldest(*args):
    return max(args)


result = oldest(dog_1.age, dog_2.age, dog_3.age, 120)

# Vypište výslednou větu "Věk nejstaršího psa: X"
print(f"Věk nejstaršího psa: {result}")

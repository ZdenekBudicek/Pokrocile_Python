# 4 pilíře OOP
# Encapsulation = zapouzdření
# Abstraction = abstrakce = dáváme přístup pouze k tomu, co je zapotřebí
# Inheritance = dědění
# Polymorphism = mnoho forem

class WizardPlayer:

    def __init__(self, name="anonym", age=0):
        self.name = name
        self.age = age

    def attack(self):
        return "Útok 1. stupně!"


class HeadWizard(WizardPlayer):

    def __init__(self, type, name, age):
        # Super vlastně rozšiřuje v tomto případě konstrukto ten init (Je nutno to pak napsat i do toho noveho init(name, age))
        super().__init__(name, age)
        self.type = type

    def attack(self):
        return "Útok 2. stupně!"

    def avada_kedavra(self):
        return "Avada Kedavra"


# player1 = WizardPlayer("david", 25)
# print(player1.attack())

# print("--------------------")

player2 = HeadWizard("good", "david", 35)
print(player2.type)
print(player2.name)
print(player2.age)

# introspection Může vás napadnout, co všechno player2 na sobě má - jaké atributy a jaké metody.
# To zjistíme, když si vyprintujeme funkci dir. Zápis bude vypadat takto.
print(dir(player2))

# print("--------------------")

# print(isinstance(player1, WizardPlayer)) # true
# print(isinstance(player1, HeadWizard))  # false
# print(isinstance(player2, WizardPlayer)) # true
# print(isinstance(player2, HeadWizard)) # true

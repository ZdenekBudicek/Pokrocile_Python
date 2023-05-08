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

    def attack(self):
        return "Útok 2. stupně!"

    def avada_kedavra(self):
        return "Avada Kedavra"


player1 = WizardPlayer("david", 25)
print(player1.attack())

print("--------------------")

player2 = HeadWizard("jana", 18)
print(player2.attack())

# Method resolution order = MRO
print(HeadWizard.mro())
print(HeadWizard.__mro__)
print(WizardPlayer.mro())
print(WizardPlayer.__mro__)

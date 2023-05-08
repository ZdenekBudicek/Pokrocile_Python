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
    # Když pojmenujeme stejně funkci která vychází z předchozí classy tak se prostě přepíše
    def attack(self):
        return "Útok 2. stupně!"

    def avada_kedavra(self):
        return "Avada Kedavra"

player1 = WizardPlayer("david", 25)
print(player1.attack())

print("--------------------")

player2 = HeadWizard("jana", 18)
print(player2.attack())

# print("--------------------")

# print(isinstance(player1, WizardPlayer)) # true
# print(isinstance(player1, HeadWizard))  # false
# print(isinstance(player2, WizardPlayer)) # true
# print(isinstance(player2, HeadWizard)) # true

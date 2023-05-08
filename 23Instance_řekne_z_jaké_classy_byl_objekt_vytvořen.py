# 4 pilíře OOP
# Encapsulation = zapouzdření
# Abstraction = abstrakce = dáváme přístup pouze k tomu, co je zapotřebí
# Inheritance = dědění

class WizardPlayer:

    def __init__(self, name="anonym", age=0):
        self.name = name
        self.age = age

    def attack(self):
        return "Útok!"


class HeadWizard(WizardPlayer):

    def avada_kedavra(self):
        return "Avada Kedavra"


player1 = WizardPlayer("david", 25)
print(player1.name)
print(player1.age)
print(player1.attack())

print("--------------------")

player2 = HeadWizard("jana", 18)
print(player2.name)
print(player2.age)
print(player2.attack())
print(player2.avada_kedavra())

print("--------------------")

# isinstance nám řekne z jaké classy byl objekt vytvořen (odpoví true/false)
print(isinstance(player1, WizardPlayer))  # true
print(isinstance(player1, HeadWizard))  # false
print(isinstance(player2, WizardPlayer))  # true
print(isinstance(player2, HeadWizard))  # true
